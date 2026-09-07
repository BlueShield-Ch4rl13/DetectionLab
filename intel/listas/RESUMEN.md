# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-07 04:09 UTC  
**Listas generadas:** 2026-09-07T11:12:40Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 167 | Caza programada, no alerta directa |
| Dominio | 961 | Caza programada, no alerta directa |
| URL | 189 | Caza programada, no alerta directa |
| Hash | 0 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (38 de 1402)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 38 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| IClickFix | 675 |
| ClearFake | 202 |
| malware_download | 100 |
| Unknown malware | 83 |
| VShell | 57 |
| php.shin_webshell | 37 |
| PureRAT | 32 |
| Unknown Stealer | 19 |
| Remcos | 13 |
| Aisuru | 12 |
| Sliver | 11 |
| AsyncRAT | 10 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 167 |
| `wazuh/cti_dominio` | 961 |
| `wazuh/cti_url` | 189 |
| `wazuh/cti_hash` | 0 |
| `wazuh/cti_cve_kev` | 21 |
| `splunk/cti_ip.csv` | 167 |
| `splunk/cti_dominio.csv` | 961 |
| `splunk/cti_url.csv` | 189 |
| `splunk/cti_hash.csv` | 0 |
| `splunk/cti_cve_kev.csv` | 21 |
| `sentinel/CTI_Ip.csv` | 167 |
| `sentinel/CTI_Dominio.csv` | 961 |
| `sentinel/CTI_Url.csv` | 189 |
| `sentinel/CTI_Hash.csv` | 0 |
| `elastic/cti_ip.ndjson` | 167 |
| `elastic/cti_dominio.ndjson` | 961 |
| `elastic/cti_url.ndjson` | 189 |
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
