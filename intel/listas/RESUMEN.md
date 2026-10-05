# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-05 05:12 UTC  
**Listas generadas:** 2026-10-05T13:12:20Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 111 | Caza programada, no alerta directa |
| Dominio | 280 | Caza programada, no alerta directa |
| URL | 209 | Caza programada, no alerta directa |
| Hash | 116 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (2252 de 2993)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 2176 |
| nivel bajo | 76 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| ClearFake | 161 |
| malware_download | 100 |
| Unknown Loader | 60 |
| Node.js: Old Technique Makes a Comeback | 52 |
| Vidar | 44 |
| Unknown malware | 39 |
| Remus | 28 |
| Contagious Interview steps outside the developer workflow | 28 |
| php.shin_webshell | 26 |
| Chinese-Speaking Operator Uses AI Agents to Target Government and Education Systems Across Asia | 25 |
| Potassium | 21 |
| Attack Cases in Korea Involving the Installation of Radmin and UltraVNC | 11 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 111 |
| `wazuh/cti_dominio` | 280 |
| `wazuh/cti_url` | 209 |
| `wazuh/cti_hash` | 116 |
| `wazuh/cti_cve_kev` | 18 |
| `splunk/cti_ip.csv` | 111 |
| `splunk/cti_dominio.csv` | 280 |
| `splunk/cti_url.csv` | 209 |
| `splunk/cti_hash.csv` | 116 |
| `splunk/cti_cve_kev.csv` | 18 |
| `sentinel/CTI_Ip.csv` | 111 |
| `sentinel/CTI_Dominio.csv` | 280 |
| `sentinel/CTI_Url.csv` | 209 |
| `sentinel/CTI_Hash.csv` | 116 |
| `elastic/cti_ip.ndjson` | 111 |
| `elastic/cti_dominio.ndjson` | 280 |
| `elastic/cti_url.ndjson` | 209 |
| `elastic/cti_hash.ndjson` | 116 |

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
