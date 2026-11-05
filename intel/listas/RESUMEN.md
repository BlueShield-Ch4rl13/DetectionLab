# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-04 10:30 UTC  
**Listas generadas:** 2026-11-04T13:34:24Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 161 | Caza programada, no alerta directa |
| Dominio | 168 | Caza programada, no alerta directa |
| URL | 444 | Caza programada, no alerta directa |
| Hash | 729 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 13 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (64 de 1566)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 64 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Vidar | 321 |
| AMOS | 300 |
| malware_download | 95 |
| VShell | 67 |
| Mirai | 65 |
| Unknown malware | 56 |
| ClearFake | 51 |
| WARDENStealer | 37 |
| php.shin_webshell | 30 |
| ValleyRAT | 29 |
| SalatStealer | 27 |
| Yoba Malware Campaign Abuses Signed AI Applications to Evade Detection | 27 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 161 |
| `wazuh/cti_dominio` | 168 |
| `wazuh/cti_url` | 444 |
| `wazuh/cti_hash` | 729 |
| `wazuh/cti_cve_kev` | 13 |
| `splunk/cti_ip.csv` | 161 |
| `splunk/cti_dominio.csv` | 168 |
| `splunk/cti_url.csv` | 444 |
| `splunk/cti_hash.csv` | 729 |
| `splunk/cti_cve_kev.csv` | 13 |
| `sentinel/CTI_Ip.csv` | 161 |
| `sentinel/CTI_Dominio.csv` | 168 |
| `sentinel/CTI_Url.csv` | 444 |
| `sentinel/CTI_Hash.csv` | 729 |
| `elastic/cti_ip.ndjson` | 161 |
| `elastic/cti_dominio.ndjson` | 168 |
| `elastic/cti_url.ndjson` | 444 |
| `elastic/cti_hash.ndjson` | 729 |

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
