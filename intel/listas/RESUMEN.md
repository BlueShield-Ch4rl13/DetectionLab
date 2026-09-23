# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-23 04:25 UTC  
**Listas generadas:** 2026-09-23T10:33:32Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 138 | Caza programada, no alerta directa |
| Dominio | 584 | Caza programada, no alerta directa |
| URL | 348 | Caza programada, no alerta directa |
| Hash | 60 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 22 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (398 de 1588)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 295 |
| nivel bajo | 103 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| ClearFake | 332 |
| IClickFix | 151 |
| Unknown malware | 103 |
| malware_download | 100 |
| Remus | 73 |
| Unknown Loader | 62 |
| php.shin_webshell | 25 |
| Cobalt Strike | 23 |
| VShell | 23 |
| Vidar | 22 |
| PureRAT | 17 |
| Remcos | 14 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 138 |
| `wazuh/cti_dominio` | 584 |
| `wazuh/cti_url` | 348 |
| `wazuh/cti_hash` | 60 |
| `wazuh/cti_cve_kev` | 22 |
| `splunk/cti_ip.csv` | 138 |
| `splunk/cti_dominio.csv` | 584 |
| `splunk/cti_url.csv` | 348 |
| `splunk/cti_hash.csv` | 60 |
| `splunk/cti_cve_kev.csv` | 22 |
| `sentinel/CTI_Ip.csv` | 138 |
| `sentinel/CTI_Dominio.csv` | 584 |
| `sentinel/CTI_Url.csv` | 348 |
| `sentinel/CTI_Hash.csv` | 60 |
| `elastic/cti_ip.ndjson` | 138 |
| `elastic/cti_dominio.ndjson` | 584 |
| `elastic/cti_url.ndjson` | 348 |
| `elastic/cti_hash.ndjson` | 60 |

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
