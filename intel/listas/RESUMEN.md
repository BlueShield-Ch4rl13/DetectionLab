# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-09 04:17 UTC  
**Listas generadas:** 2026-09-09T10:31:29Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 161 | Caza programada, no alerta directa |
| Dominio | 1363 | Caza programada, no alerta directa |
| URL | 266 | Caza programada, no alerta directa |
| Hash | 63 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (186 de 2063)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 119 |
| tipo no usado | 67 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown Loader | 1150 |
| Unknown malware | 135 |
| ClearFake | 120 |
| malware_download | 100 |
| VShell | 81 |
| php.shin_webshell | 27 |
| IClickFix | 26 |
| Unknown Stealer | 20 |
| DPRK APTs: Ted backdoor and curlRAT target South Korean media and automotive sectors | 20 |
| Remus | 18 |
| PureRAT | 18 |
| Kimsuky Uses the AI Agent 'opencode' to Create Decoys as Its GitHub PAT-Based LNK Attacks Evolve | 17 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 161 |
| `wazuh/cti_dominio` | 1363 |
| `wazuh/cti_url` | 266 |
| `wazuh/cti_hash` | 63 |
| `wazuh/cti_cve_kev` | 23 |
| `splunk/cti_ip.csv` | 161 |
| `splunk/cti_dominio.csv` | 1363 |
| `splunk/cti_url.csv` | 266 |
| `splunk/cti_hash.csv` | 63 |
| `splunk/cti_cve_kev.csv` | 23 |
| `sentinel/CTI_Ip.csv` | 161 |
| `sentinel/CTI_Dominio.csv` | 1363 |
| `sentinel/CTI_Url.csv` | 266 |
| `sentinel/CTI_Hash.csv` | 63 |
| `elastic/cti_ip.ndjson` | 161 |
| `elastic/cti_dominio.ndjson` | 1363 |
| `elastic/cti_url.ndjson` | 266 |
| `elastic/cti_hash.ndjson` | 63 |

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
