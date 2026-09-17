# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-17 04:34 UTC  
**Listas generadas:** 2026-09-17T10:44:53Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 126 | Caza programada, no alerta directa |
| Dominio | 269 | Caza programada, no alerta directa |
| URL | 230 | Caza programada, no alerta directa |
| Hash | 90 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 19 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (163 de 936)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 104 |
| tipo no usado | 59 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| malware_download | 100 |
| Unknown malware | 68 |
| ClearFake | 68 |
| IClickFix | 64 |
| Remcos | 45 |
| Remus | 38 |
| Vidar | 31 |
| The banana stand: brokering and managing infections across Asia using MQTT | 31 |
| VShell | 28 |
| php.shin_webshell | 26 |
| Quasar RAT | 23 |
| Cobalt Strike | 18 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 126 |
| `wazuh/cti_dominio` | 269 |
| `wazuh/cti_url` | 230 |
| `wazuh/cti_hash` | 90 |
| `wazuh/cti_cve_kev` | 19 |
| `splunk/cti_ip.csv` | 126 |
| `splunk/cti_dominio.csv` | 269 |
| `splunk/cti_url.csv` | 230 |
| `splunk/cti_hash.csv` | 90 |
| `splunk/cti_cve_kev.csv` | 19 |
| `sentinel/CTI_Ip.csv` | 126 |
| `sentinel/CTI_Dominio.csv` | 269 |
| `sentinel/CTI_Url.csv` | 230 |
| `sentinel/CTI_Hash.csv` | 90 |
| `elastic/cti_ip.ndjson` | 126 |
| `elastic/cti_dominio.ndjson` | 269 |
| `elastic/cti_url.ndjson` | 230 |
| `elastic/cti_hash.ndjson` | 90 |

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
