# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-01 05:25 UTC  
**Listas generadas:** 2026-10-01T12:10:21Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 284 | Caza programada, no alerta directa |
| Dominio | 271 | Caza programada, no alerta directa |
| URL | 270 | Caza programada, no alerta directa |
| Hash | 0 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 17 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (345 de 1273)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 345 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| AdaptixC2 | 143 |
| malware_download | 100 |
| ClearFake | 96 |
| Remcos | 94 |
| Remus | 57 |
| Unknown malware | 44 |
| Vidar | 35 |
| AsyncRAT | 32 |
| php.shin_webshell | 25 |
| Mozi | 15 |
| VShell | 14 |
| Mirai | 13 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 284 |
| `wazuh/cti_dominio` | 271 |
| `wazuh/cti_url` | 270 |
| `wazuh/cti_hash` | 0 |
| `wazuh/cti_cve_kev` | 17 |
| `splunk/cti_ip.csv` | 284 |
| `splunk/cti_dominio.csv` | 271 |
| `splunk/cti_url.csv` | 270 |
| `splunk/cti_hash.csv` | 0 |
| `splunk/cti_cve_kev.csv` | 17 |
| `sentinel/CTI_Ip.csv` | 284 |
| `sentinel/CTI_Dominio.csv` | 271 |
| `sentinel/CTI_Url.csv` | 270 |
| `sentinel/CTI_Hash.csv` | 0 |
| `elastic/cti_ip.ndjson` | 284 |
| `elastic/cti_dominio.ndjson` | 271 |
| `elastic/cti_url.ndjson` | 270 |
| `elastic/cti_hash.ndjson` | 0 |

## Como se instala cada una

Ver `deploy/<siem>/INSTALAR.md`. En resumen:

```bash
# Wazuh: copiar, declarar en ossec.conf y compilar
sudo cp intel/listas/wazuh/*.cdb /var/ossec/etc/lists/
sudo /var/ossec/bin/ossec-makelists

# Splunk: como lookups de la app
cp intel/listas/splunk/*.csv $SPLUNK_HOME/etc/apps/TA-detection-lab/lookups/

# Sentinel: Watchlists > New > importar el CSV, alias sin el prefijo CTI_
# Elastic: bulk al indice de indicadores
curl -XPOST 'localhost:9200/logs-ti_newscti-default/_bulk' \
     -H 'Content-Type: application/x-ndjson' \
     --data-binary @intel/listas/elastic/cti_ip.ndjson
```
