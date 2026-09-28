# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-28 04:58 UTC  
**Listas generadas:** 2026-09-28T12:32:01Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 185 | Caza programada, no alerta directa |
| Dominio | 671 | Caza programada, no alerta directa |
| URL | 235 | Caza programada, no alerta directa |
| Hash | 29 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (4165 de 5328)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 3999 |
| nivel bajo | 166 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown Loader | 453 |
| ClearFake | 127 |
| malware_download | 100 |
| Cobalt Strike | 76 |
| Unknown malware | 61 |
| Sliver | 60 |
| php.shin_webshell | 42 |
| VShell | 32 |
| IClickFix | 31 |
| Vidar | 16 |
| Mozi | 15 |
| Aisuru | 10 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 185 |
| `wazuh/cti_dominio` | 671 |
| `wazuh/cti_url` | 235 |
| `wazuh/cti_hash` | 29 |
| `wazuh/cti_cve_kev` | 19 |
| `splunk/cti_ip.csv` | 185 |
| `splunk/cti_dominio.csv` | 671 |
| `splunk/cti_url.csv` | 235 |
| `splunk/cti_hash.csv` | 29 |
| `splunk/cti_cve_kev.csv` | 19 |
| `sentinel/CTI_Ip.csv` | 185 |
| `sentinel/CTI_Dominio.csv` | 671 |
| `sentinel/CTI_Url.csv` | 235 |
| `sentinel/CTI_Hash.csv` | 29 |
| `elastic/cti_ip.ndjson` | 185 |
| `elastic/cti_dominio.ndjson` | 671 |
| `elastic/cti_url.ndjson` | 235 |
| `elastic/cti_hash.ndjson` | 29 |

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
