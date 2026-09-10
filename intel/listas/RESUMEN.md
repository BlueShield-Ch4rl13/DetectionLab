# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-10 04:15 UTC  
**Listas generadas:** 2026-09-10T10:20:57Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 160 | Caza programada, no alerta directa |
| Dominio | 712 | Caza programada, no alerta directa |
| URL | 242 | Caza programada, no alerta directa |
| Hash | 112 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 21 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (150 de 1422)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 86 |
| tipo no usado | 64 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| ClearFake | 323 |
| Unknown RAT | 237 |
| Unknown Stealer | 108 |
| Unknown malware | 106 |
| malware_download | 97 |
| Integrating AI into Attack Operations  From AI-Generated Decoy Documents to a Local LLM | 74 |
| VShell | 56 |
| php.shin_webshell | 31 |
| Vidar | 18 |
| Once in a BlueMoon: Multiple State-Aligned Threat Actors Rapidly Adopt Novel Exploit Chain Using Chrome and Windows Zero-Days | 18 |
| The Permanent Threat: Analyzing Blockchain-Based C2 Operations and Communications | 18 |
| Aisuru | 12 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 160 |
| `wazuh/cti_dominio` | 712 |
| `wazuh/cti_url` | 242 |
| `wazuh/cti_hash` | 112 |
| `wazuh/cti_cve_kev` | 21 |
| `splunk/cti_ip.csv` | 160 |
| `splunk/cti_dominio.csv` | 712 |
| `splunk/cti_url.csv` | 242 |
| `splunk/cti_hash.csv` | 112 |
| `splunk/cti_cve_kev.csv` | 21 |
| `sentinel/CTI_Ip.csv` | 160 |
| `sentinel/CTI_Dominio.csv` | 712 |
| `sentinel/CTI_Url.csv` | 242 |
| `sentinel/CTI_Hash.csv` | 112 |
| `elastic/cti_ip.ndjson` | 160 |
| `elastic/cti_dominio.ndjson` | 712 |
| `elastic/cti_url.ndjson` | 242 |
| `elastic/cti_hash.ndjson` | 112 |

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
