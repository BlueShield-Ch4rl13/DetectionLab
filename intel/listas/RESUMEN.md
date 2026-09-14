# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-14 04:32 UTC  
**Listas generadas:** 2026-09-14T11:22:48Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 149 | Caza programada, no alerta directa |
| Dominio | 365 | Caza programada, no alerta directa |
| URL | 209 | Caza programada, no alerta directa |
| Hash | 64 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 24 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (421 de 1266)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 374 |
| nivel bajo | 47 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| IClickFix | 206 |
| malware_download | 99 |
| AMOS | 75 |
| ClearFake | 69 |
| MacSync | 29 |
| Jackskid | 28 |
| Jewelbug: APT Group Runs Espionage and Crypto Fraud Operations Side by Side | 28 |
| Remus | 26 |
| php.shin_webshell | 26 |
| Cobalt Strike | 25 |
| VShell | 24 |
| Unknown malware | 19 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 149 |
| `wazuh/cti_dominio` | 365 |
| `wazuh/cti_url` | 209 |
| `wazuh/cti_hash` | 64 |
| `wazuh/cti_cve_kev` | 24 |
| `splunk/cti_ip.csv` | 149 |
| `splunk/cti_dominio.csv` | 365 |
| `splunk/cti_url.csv` | 209 |
| `splunk/cti_hash.csv` | 64 |
| `splunk/cti_cve_kev.csv` | 24 |
| `sentinel/CTI_Ip.csv` | 149 |
| `sentinel/CTI_Dominio.csv` | 365 |
| `sentinel/CTI_Url.csv` | 209 |
| `sentinel/CTI_Hash.csv` | 64 |
| `elastic/cti_ip.ndjson` | 149 |
| `elastic/cti_dominio.ndjson` | 365 |
| `elastic/cti_url.ndjson` | 209 |
| `elastic/cti_hash.ndjson` | 64 |

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
