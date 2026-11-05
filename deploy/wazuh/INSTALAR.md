# Wazuh — instalacion

## Que hay en esta carpeta

| Carpeta | Contenido | Se regenera |
|---|---|---|
| `reglas/` | 260 reglas XML generadas desde Sigma + 73 de marco + 8 de inteligencia | Sí, con `tools/build.py` |
| `listas/` | Listas CDB de indicadores de News CTI | Sí, con `tools/sync_cti.py` |
| `listas/contexto/` | Las 14 listas de contexto que usan las reglas Zero Trust y de cumplimiento (vacías: las rellenas tú) | No |
| `consultas/` | Caza sobre el indexador (Discover / API) | No, escritas a mano |

## Series de identificadores

No se solapan, así que las tres vías conviven en el mismo manager:

| Serie | Origen |
|---|---|
| 100100 – 100699 | Detecciones Zero Trust escritas a mano |
| 100700 – 100799 | Detecciones de cumplimiento escritas a mano |
| 101000 – 101299 | Generadas desde `rules/` por `tools/sigma_to_wazuh.py` |
| 101300 – 101399 | Inteligencia de News CTI |

Los IDs de las reglas generadas son fijos: `deploy/wazuh/ids.json` guarda el de
cada una, así que añadir o quitar reglas no renumera las demás, y un ID retirado
no se reutiliza. Lo que filtres por ID (active response, paneles, ResponseLab)
sigue apuntando a la misma detección después de cada regeneración.

Si ya tienes reglas propias, comprueba antes que no pisan estos rangos:

```bash
grep -ho 'rule id="[0-9]*"' /var/ossec/etc/rules/*.xml | grep -o '[0-9]*' | sort -n | uniq -d
```

## 1. Reglas

```bash
sudo cp deploy/wazuh/reglas/*.xml /var/ossec/etc/rules/
sudo chown root:wazuh /var/ossec/etc/rules/*.xml
sudo chmod 660 /var/ossec/etc/rules/*.xml

# Validar ANTES de reiniciar: un XML roto deja el manager sin arrancar
sudo /var/ossec/bin/wazuh-logtest -t
```

Si `wazuh-logtest -t` sale limpio:

```bash
sudo systemctl restart wazuh-manager
sudo tail -f /var/ossec/logs/ossec.log
```

## 2. Listas de inteligencia

En el manager, una lista se declara por su ruta **sin extensión**
(`etc/lists/cti_url`) y el fichero de texto se llama igual: el manager compila
él solo el `.cdb` al arrancar. Por eso se copian quitando el `.cdb` del nombre;
copiado tal cual, `cti_url.cdb` no es la lista `etc/lists/cti_url` y las reglas
que la usan no ven nada.

```bash
python3 tools/sync_cti.py                       # refresca desde News CTI
for f in intel/listas/wazuh/*.cdb; do
  sudo install -o root -g wazuh -m 660 "$f" "/var/ossec/etc/lists/$(basename "$f" .cdb)"
done
```

Declara cada lista en `/var/ossec/etc/ossec.conf`, dentro de `<ruleset>`:

```xml
<ruleset>
  <list>etc/lists/cti_hash</list>
  <list>etc/lists/cti_ip</list>
  <list>etc/lists/cti_dominio</list>
  <list>etc/lists/cti_url</list>
  <list>etc/lists/cti_cve_kev</list>
</ruleset>
```

Valida y reinicia (al arrancar, el manager compila las listas; `ossec-makelists`
ya no hace falta):

```bash
sudo /var/ossec/bin/wazuh-logtest -t
sudo systemctl restart wazuh-manager
```

**Ojo con el formato CDB.** Cada línea es una entrada, comentarios incluidos:
por eso los `.cdb` no llevan cabecera. Y la clave se separa del valor en el
primer `:`, así que una clave que lleva `:` (una URL, una IPv6) va entre
comillas: `"http://x.example/a":Mirai|alta`. `sync_cti.py` las escribe así y
`tools/validate.py` falla si alguna no lo está.

### Refresco periódico

Los indicadores caducan. Una IP de mando y control de hace un mes es hoy, con
frecuencia, un servidor legítimo reasignado. Programa el refresco (en el
`crontab` de root):

```cron
0 6 * * * cd /opt/detection-lab && python3 tools/sync_cti.py --max-dias 30 && for f in intel/listas/wazuh/*.cdb; do install -o root -g wazuh -m 660 "$f" "/var/ossec/etc/lists/$(basename "$f" .cdb)"; done && systemctl restart wazuh-manager
```

### Listas de contexto (Zero Trust y cumplimiento)

Las reglas 0900–0960 comparan con listas que describen **tu** organización.
Vienen vacías en `listas/contexto/`: sin ellas, el manager no puede cargar las
reglas que las usan. Instálalas igual que las de inteligencia y declara cada
una en `<ruleset>`:

```bash
for f in deploy/wazuh/listas/contexto/*.cdb; do
  sudo install -o root -g wazuh -m 660 "$f" "/var/ossec/etc/lists/$(basename "$f" .cdb)"
done
```

| Lista | Una línea por | Formato de la clave | Reglas | Si se queda vacía |
|---|---|---|---|---|
| `zta_privileged_accounts` | cuenta privilegiada | `usuario:` | ZTA-ID | no salta |
| `zta_service_accounts` | cuenta de servicio | `usuario:` | ZTA-ID | no salta |
| `zta_admin_jumphosts` | bastión de administración | IP o prefijo (`10.0.99.`) | ZTA-ID-002 | salta con cada acceso privilegiado |
| `zta_asset_inventory` | equipo inventariado | `hostname:` | ZTA-DEV-002 | salta con cada equipo |
| `zta_crown_jewels` | segmento protegido | IP o prefijo | ZTA-NET-001, 004 | no salta |
| `zta_approved_proxies` | proxy de salida | IP o prefijo | ZTA-NET | salta con cada salida directa |
| `zta_threat_intel` | IP de C2 (MISP) | IP | ZTA-NET-006 | no salta (o copia ahí `cti_ip`) |
| `zta_pep_sources` | proxy ZTNA / PEP | IP o prefijo | ZTA-APP-001 | salta con cada acceso |
| `zta_data_classification` | ruta clasificada | ruta completa | ZTA-APP | no salta |
| `zta_allowed_registries` | registro de imágenes aprobado | `registro/imagen` | ZTA-SUP-006 | salta con cada `docker pull` |
| `cmp_datos_personales` | fichero con datos personales | ruta completa | CMP-RGP | no salta |
| `cmp_sistemas_datos_personales` | sistema que trata datos personales | IP o prefijo | CMP-RGP-002 | no salta |
| `cmp_proveedores` | cuenta de proveedor | `usuario:` | CMP-TER-001 | no salta |
| `cmp_paises_adecuados` | país con decisión de adecuación | código ISO (`ES:`) | reservada (aún ninguna regla) | — |

Una clave con `:` (una ruta de Windows `C:\...`, una IPv6) va entre comillas.
Las que "saltan con cada…" son de lista blanca (`not_*_match_key`): rellénalas
antes de poner esas reglas en producción.

## 3. Telemetría que hace falta

Sin esto, las reglas están cargadas pero no ven nada.

**Windows — Sysmon.** El agente tiene que reenviar el canal:

```xml
<localfile>
  <location>Microsoft-Windows-Sysmon/Operational</location>
  <log_format>eventchannel</log_format>
</localfile>
```

Las reglas consumen EID 1 (proceso), 3 (red), 6 (driver), 7 (imagen), 8 (hilo
remoto), 10 (acceso a proceso), 11 (fichero), 12-14 (registro), 17-18 (tubería)
y 22 (DNS).

**Windows — canal Security.** Las 21 reglas de AD y de auditoría lo necesitan,
y varias exigen que la auditoría avanzada esté activada:

```powershell
auditpol /set /subcategory:"Directory Service Changes" /success:enable
auditpol /set /subcategory:"Kerberos Service Ticket Operations" /success:enable /failure:enable
auditpol /set /subcategory:"File Share" /success:enable
auditpol /set /subcategory:"Removable Storage" /success:enable
```

**Linux — Sysmon for Linux.** Las reglas Sigma de Linux miran la línea de
comandos entera (`CommandLine`), y auditd no la tiene: su registro EXECVE parte
los argumentos en `a0`, `a1`... y los pasa a hexadecimal si llevan espacios.
Por eso las reglas generadas usan Sysmon for Linux con el decodificador de
`decodificadores/`:

```bash
# En cada equipo: Sysmon for Linux escribe en syslog (programa "sysmon")
sudo sysmon -accepteula -i config-sysmon-linux.xml
# En el manager:
sudo cp deploy/wazuh/decodificadores/0975-sysmon_linux.xml /var/ossec/etc/decoders/
sudo systemctl restart wazuh-manager
```

`python tools/probar_reglas_wazuh.py` pasa eventos de muestra de Sysmon for
Linux y de auditoría de Kubernetes por el decodificador y las reglas. No
sustituye a `wazuh-logtest` con un evento real de tu `/var/log/syslog`.

**Kubernetes** — el registro de auditoría del API server en JSON, leído con
`<log_format>json</log_format>`. Los campos dentro de listas (contenedores,
volúmenes) se buscan en todo el evento, en cualquier contenedor.

**macOS** — el agente de Wazuh no recoge la creación de procesos ni de
ficheros, así que las reglas de macOS no se generan para Wazuh (ver abajo).

## 4. Comprobar que funciona

```bash
# ¿Cargaron las reglas?
sudo /var/ossec/bin/wazuh-logtest -t 2>&1 | grep -c "rules"

# ¿Se compilaron las listas? (el manager deja un .cdb junto a cada una)
ls -la /var/ossec/etc/lists/cti_* /var/ossec/etc/lists/zta_* /var/ossec/etc/lists/cmp_*

# Probar una regla concreta con un evento de ejemplo
sudo /var/ossec/bin/wazuh-logtest
# y pegar un evento JSON de Sysmon
```

## Lo que Wazuh no puede hacer, y no se disimula

Estas reglas de la biblioteca no tienen equivalente aquí. `tools/build.py` lo
avisa en cada ejecución:

| Regla | Motivo |
|---|---|
| Password spraying contra Entra ID | Correlación `value_count`: `<frequency>` cuenta disparos de regla, no valores distintos de un campo |
| Reutilización de sesión desde redes distintas | Igual |
| Envío masivo desde cuenta interna | Igual |
| Dispositivo no conforme | Compara contra `null`, que Wazuh no comprueba sobre un campo decodificado |
| Correo desde dominio recién registrado | Usa el modificador `\|lt`, comparación numérica que Wazuh no expresa |
| Volumen de subida anómalo | Usa `\|gte` sobre los bytes enviados |
| Patrón de beaconing | Correlación `event_count` agrupada por origen y destino |
| Las 8 reglas de macOS | El agente de Wazuh no recoge procesos ni ficheros en macOS: necesitan la telemetría de un EDR en Splunk, Sentinel o Elastic |

Las tres correlaciones están en Splunk y en `deploy/sentinel/consultas/correlaciones.kql`.
