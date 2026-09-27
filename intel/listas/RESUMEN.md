# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-27 04:56 UTC  
**Listas generadas:** 2026-09-27T11:07:30Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 94 | Caza programada, no alerta directa |
| Dominio | 898 | Caza programada, no alerta directa |
| URL | 279 | Caza programada, no alerta directa |
| Hash | 37 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (244 de 1565)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 127 |
| nivel bajo | 117 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown Loader | 517 |
| IClickFix | 162 |
| ClearFake | 119 |
| malware_download | 100 |
| Unknown malware | 94 |
| ACR Stealer | 58 |
| Vidar | 36 |
| Mozi | 25 |
| Cobalt Strike | 18 |
| AMOS | 14 |
| VShell | 12 |
| Lumma Stealer | 11 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 94 |
| `wazuh/cti_dominio` | 898 |
| `wazuh/cti_url` | 279 |
| `wazuh/cti_hash` | 37 |
| `wazuh/cti_cve_kev` | 17 |
| `splunk/cti_ip.csv` | 94 |
| `splunk/cti_dominio.csv` | 898 |
| `splunk/cti_url.csv` | 279 |
| `splunk/cti_hash.csv` | 37 |
| `splunk/cti_cve_kev.csv` | 17 |
| `sentinel/CTI_Ip.csv` | 94 |
| `sentinel/CTI_Dominio.csv` | 898 |
| `sentinel/CTI_Url.csv` | 279 |
| `sentinel/CTI_Hash.csv` | 37 |
| `elastic/cti_ip.ndjson` | 94 |
| `elastic/cti_dominio.ndjson` | 898 |
| `elastic/cti_url.ndjson` | 279 |
| `elastic/cti_hash.ndjson` | 37 |

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
