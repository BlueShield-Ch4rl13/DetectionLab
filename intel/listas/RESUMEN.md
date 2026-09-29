# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-29 05:24 UTC  
**Listas generadas:** 2026-09-29T11:54:04Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 200 | Caza programada, no alerta directa |
| Dominio | 226 | Caza programada, no alerta directa |
| URL | 237 | Caza programada, no alerta directa |
| Hash | 85 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 18 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (388 de 1175)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 287 |
| nivel bajo | 101 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| ClearFake | 144 |
| malware_download | 100 |
| Unknown malware | 94 |
| Vidar | 84 |
| Remus | 34 |
| php.shin_webshell | 27 |
| PureRAT and PureLogs Campaign Targeting Japanese Organizations | 27 |
| Lunex Unmasked: A New Information Stealer Deployed Through BYOVD | 26 |
| Aisuru | 16 |
| Operation Master: Deconstructing a Multi-Tiered Intrusion and Monetization Pipeline | 14 |
| Remcos | 13 |
| AMOS | 12 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 200 |
| `wazuh/cti_dominio` | 226 |
| `wazuh/cti_url` | 237 |
| `wazuh/cti_hash` | 85 |
| `wazuh/cti_cve_kev` | 18 |
| `splunk/cti_ip.csv` | 200 |
| `splunk/cti_dominio.csv` | 226 |
| `splunk/cti_url.csv` | 237 |
| `splunk/cti_hash.csv` | 85 |
| `splunk/cti_cve_kev.csv` | 18 |
| `sentinel/CTI_Ip.csv` | 200 |
| `sentinel/CTI_Dominio.csv` | 226 |
| `sentinel/CTI_Url.csv` | 237 |
| `sentinel/CTI_Hash.csv` | 85 |
| `elastic/cti_ip.ndjson` | 200 |
| `elastic/cti_dominio.ndjson` | 226 |
| `elastic/cti_url.ndjson` | 237 |
| `elastic/cti_hash.ndjson` | 85 |

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
