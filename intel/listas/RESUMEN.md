# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-26 04:38 UTC  
**Listas generadas:** 2026-09-26T10:35:22Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 99 | Caza programada, no alerta directa |
| Dominio | 1485 | Caza programada, no alerta directa |
| URL | 240 | Caza programada, no alerta directa |
| Hash | 39 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (217 de 2110)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 130 |
| nivel bajo | 87 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown Loader | 717 |
| IClickFix | 603 |
| malware_download | 100 |
| ClearFake | 99 |
| Unknown malware | 88 |
| php.shin_webshell | 26 |
| AsyncRAT | 19 |
| Cobalt Strike | 15 |
| Mozi | 15 |
| Trust and the enticing consultancy offer | 14 |
| Vidar | 13 |
| Remcos | 11 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 99 |
| `wazuh/cti_dominio` | 1485 |
| `wazuh/cti_url` | 240 |
| `wazuh/cti_hash` | 39 |
| `wazuh/cti_cve_kev` | 17 |
| `splunk/cti_ip.csv` | 99 |
| `splunk/cti_dominio.csv` | 1485 |
| `splunk/cti_url.csv` | 240 |
| `splunk/cti_hash.csv` | 39 |
| `splunk/cti_cve_kev.csv` | 17 |
| `sentinel/CTI_Ip.csv` | 99 |
| `sentinel/CTI_Dominio.csv` | 1485 |
| `sentinel/CTI_Url.csv` | 240 |
| `sentinel/CTI_Hash.csv` | 39 |
| `elastic/cti_ip.ndjson` | 99 |
| `elastic/cti_dominio.ndjson` | 1485 |
| `elastic/cti_url.ndjson` | 240 |
| `elastic/cti_hash.ndjson` | 39 |

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
