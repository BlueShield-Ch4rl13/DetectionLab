# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-18 04:08 UTC  
**Listas generadas:** 2026-10-18T10:10:25Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 104 | Caza programada, no alerta directa |
| Dominio | 433 | Caza programada, no alerta directa |
| URL | 498 | Caza programada, no alerta directa |
| Hash | 135 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 15 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (544 de 1755)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 480 |
| nivel bajo | 64 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Vidar | 286 |
| IClickFix | 274 |
| Unknown malware | 125 |
| malware_download | 100 |
| Noodle RAT: A Recipe for Cross Platform Espionage | 53 |
| DeerStealer | 44 |
| php.shin_webshell | 41 |
| VectraRAT: An Undocumented Full-Stack MaaS Built From Scratch | 36 |
| Beware the SparroWock: The backdoor that bites  the commands that catch | 31 |
| Unknown RAT | 23 |
| WARDENStealer | 17 |
| ClearFake | 17 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 104 |
| `wazuh/cti_dominio` | 433 |
| `wazuh/cti_url` | 498 |
| `wazuh/cti_hash` | 135 |
| `wazuh/cti_cve_kev` | 15 |
| `splunk/cti_ip.csv` | 104 |
| `splunk/cti_dominio.csv` | 433 |
| `splunk/cti_url.csv` | 498 |
| `splunk/cti_hash.csv` | 135 |
| `splunk/cti_cve_kev.csv` | 15 |
| `sentinel/CTI_Ip.csv` | 104 |
| `sentinel/CTI_Dominio.csv` | 433 |
| `sentinel/CTI_Url.csv` | 498 |
| `sentinel/CTI_Hash.csv` | 135 |
| `elastic/cti_ip.ndjson` | 104 |
| `elastic/cti_dominio.ndjson` | 433 |
| `elastic/cti_url.ndjson` | 498 |
| `elastic/cti_hash.ndjson` | 135 |

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
