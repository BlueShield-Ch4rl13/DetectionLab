# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-06 10:27 UTC  
**Listas generadas:** 2026-11-06T13:31:44Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 205 | Caza programada, no alerta directa |
| Dominio | 239 | Caza programada, no alerta directa |
| URL | 172 | Caza programada, no alerta directa |
| Hash | 1001 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 14 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (42 de 1659)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 42 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown Loader | 351 |
| AMOS | 333 |
| malware_download | 97 |
| Vidar | 71 |
| ValleyRAT | 70 |
| Quasar RAT | 61 |
| SalatStealer | 45 |
| IClickFix | 45 |
| ClearFake | 45 |
| New Lindnor Backdoor and Glut of Security Killers Used in Ransomware Attack on U.S. Org | 42 |
| VShell | 38 |
| Mirai | 25 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 205 |
| `wazuh/cti_dominio` | 239 |
| `wazuh/cti_url` | 172 |
| `wazuh/cti_hash` | 1001 |
| `wazuh/cti_cve_kev` | 14 |
| `splunk/cti_ip.csv` | 205 |
| `splunk/cti_dominio.csv` | 239 |
| `splunk/cti_url.csv` | 172 |
| `splunk/cti_hash.csv` | 1001 |
| `splunk/cti_cve_kev.csv` | 14 |
| `sentinel/CTI_Ip.csv` | 205 |
| `sentinel/CTI_Dominio.csv` | 239 |
| `sentinel/CTI_Url.csv` | 172 |
| `sentinel/CTI_Hash.csv` | 1001 |
| `elastic/cti_ip.ndjson` | 205 |
| `elastic/cti_dominio.ndjson` | 239 |
| `elastic/cti_url.ndjson` | 172 |
| `elastic/cti_hash.ndjson` | 1001 |

## Como se instala cada una

Ver `deploy/<siem>/INSTALAR.md`. En resumen:

```bash
# Wazuh: copiar SIN la extension, declarar en ossec.conf y reiniciar
for f in intel/listas/wazuh/*.cdb; do
  sudo install -o root -g wazuh -m 660 "$f" "/var/ossec/etc/lists/$(basename "$f" .cdb)"
done
sudo systemctl restart wazuh-manager

# Splunk: como lookups de la app
cp intel/listas/splunk/*.csv $SPLUNK_HOME/etc/apps/TA-detection-lab/lookups/

# Sentinel: Watchlists > New > importar el CSV, alias sin el prefijo CTI_
# Elastic: bulk al indice de indicadores
curl -XPOST 'localhost:9200/logs-ti_newscti-default/_bulk' \
     -H 'Content-Type: application/x-ndjson' \
     --data-binary @intel/listas/elastic/cti_ip.ndjson
```
