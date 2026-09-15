# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-15 04:33 UTC  
**Listas generadas:** 2026-09-15T10:46:14Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 428 | Caza programada, no alerta directa |
| Dominio | 546 | Caza programada, no alerta directa |
| URL | 240 | Caza programada, no alerta directa |
| Hash | 78 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 23 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (192 de 1571)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 131 |
| nivel bajo | 61 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| ClearFake | 213 |
| Unknown malware | 192 |
| IClickFix | 127 |
| Vidar | 113 |
| malware_download | 99 |
| Cobalt Strike | 65 |
| Sliver | 48 |
| Remcos | 46 |
| php.shin_webshell | 30 |
| Jewelbug: APT Group Runs Espionage and Crypto Fraud Operations Side by Side | 28 |
| AMOS | 25 |
| AsyncRAT | 23 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 428 |
| `wazuh/cti_dominio` | 546 |
| `wazuh/cti_url` | 240 |
| `wazuh/cti_hash` | 78 |
| `wazuh/cti_cve_kev` | 23 |
| `splunk/cti_ip.csv` | 428 |
| `splunk/cti_dominio.csv` | 546 |
| `splunk/cti_url.csv` | 240 |
| `splunk/cti_hash.csv` | 78 |
| `splunk/cti_cve_kev.csv` | 23 |
| `sentinel/CTI_Ip.csv` | 428 |
| `sentinel/CTI_Dominio.csv` | 546 |
| `sentinel/CTI_Url.csv` | 240 |
| `sentinel/CTI_Hash.csv` | 78 |
| `elastic/cti_ip.ndjson` | 428 |
| `elastic/cti_dominio.ndjson` | 546 |
| `elastic/cti_url.ndjson` | 240 |
| `elastic/cti_hash.ndjson` | 78 |

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
