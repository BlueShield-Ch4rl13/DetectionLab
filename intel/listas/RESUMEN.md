# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-04 05:29 UTC  
**Listas generadas:** 2026-10-04T11:36:09Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 110 | Caza programada, no alerta directa |
| Dominio | 1065 | Caza programada, no alerta directa |
| URL | 174 | Caza programada, no alerta directa |
| Hash | 106 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (1200 de 2690)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 1114 |
| nivel bajo | 86 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown Loader | 925 |
| malware_download | 100 |
| IClickFix | 70 |
| Node.js: Old Technique Makes a Comeback | 53 |
| Unknown malware | 46 |
| ClearFake | 29 |
| Contagious Interview steps outside the developer workflow | 28 |
| Potassium | 26 |
| Chinese-Speaking Operator Uses AI Agents to Target Government and Education Systems Across Asia | 25 |
| php.shin_webshell | 24 |
| Remus | 21 |
| AsyncRAT | 13 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 110 |
| `wazuh/cti_dominio` | 1065 |
| `wazuh/cti_url` | 174 |
| `wazuh/cti_hash` | 106 |
| `wazuh/cti_cve_kev` | 17 |
| `splunk/cti_ip.csv` | 110 |
| `splunk/cti_dominio.csv` | 1065 |
| `splunk/cti_url.csv` | 174 |
| `splunk/cti_hash.csv` | 106 |
| `splunk/cti_cve_kev.csv` | 17 |
| `sentinel/CTI_Ip.csv` | 110 |
| `sentinel/CTI_Dominio.csv` | 1065 |
| `sentinel/CTI_Url.csv` | 174 |
| `sentinel/CTI_Hash.csv` | 106 |
| `elastic/cti_ip.ndjson` | 110 |
| `elastic/cti_dominio.ndjson` | 1065 |
| `elastic/cti_url.ndjson` | 174 |
| `elastic/cti_hash.ndjson` | 106 |

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
