# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-08 04:10 UTC  
**Listas generadas:** 2026-09-08T10:22:07Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 189 | Caza programada, no alerta directa |
| Dominio | 447 | Caza programada, no alerta directa |
| URL | 318 | Caza programada, no alerta directa |
| Hash | 41 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 20 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (227 de 1235)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 142 |
| tipo no usado | 85 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| ClearFake | 262 |
| Unknown malware | 138 |
| VShell | 106 |
| IClickFix | 105 |
| malware_download | 100 |
| Unknown Stealer | 55 |
| php.shin_webshell | 29 |
| Remcos | 26 |
| Kimsuky Uses the AI Agent 'opencode' to Create Decoys as Its GitHub PAT-Based LNK Attacks Evolve | 17 |
| Cobalt Strike | 16 |
| Mozi | 13 |
| PEEP: A Browser RAT Posing as a Chrome Extension | 13 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 189 |
| `wazuh/cti_dominio` | 447 |
| `wazuh/cti_url` | 318 |
| `wazuh/cti_hash` | 41 |
| `wazuh/cti_cve_kev` | 20 |
| `splunk/cti_ip.csv` | 189 |
| `splunk/cti_dominio.csv` | 447 |
| `splunk/cti_url.csv` | 318 |
| `splunk/cti_hash.csv` | 41 |
| `splunk/cti_cve_kev.csv` | 20 |
| `sentinel/CTI_Ip.csv` | 189 |
| `sentinel/CTI_Dominio.csv` | 447 |
| `sentinel/CTI_Url.csv` | 318 |
| `sentinel/CTI_Hash.csv` | 41 |
| `elastic/cti_ip.ndjson` | 189 |
| `elastic/cti_dominio.ndjson` | 447 |
| `elastic/cti_url.ndjson` | 318 |
| `elastic/cti_hash.ndjson` | 41 |

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
