# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-19 04:16 UTC  
**Listas generadas:** 2026-09-19T10:03:24Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 151 | Caza programada, no alerta directa |
| Dominio | 318 | Caza programada, no alerta directa |
| URL | 192 | Caza programada, no alerta directa |
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

## Que se descarto del feed (81 de 787)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 81 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown malware | 133 |
| malware_download | 100 |
| Remcos | 75 |
| ClearFake | 70 |
| VShell | 60 |
| php.shin_webshell | 26 |
| Remus | 25 |
| AMOS | 21 |
| Cobalt Strike | 15 |
| Quasar RAT | 15 |
| PureRAT | 14 |
| XWorm | 13 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 151 |
| `wazuh/cti_dominio` | 318 |
| `wazuh/cti_url` | 192 |
| `wazuh/cti_hash` | 0 |
| `wazuh/cti_cve_kev` | 21 |
| `splunk/cti_ip.csv` | 151 |
| `splunk/cti_dominio.csv` | 318 |
| `splunk/cti_url.csv` | 192 |
| `splunk/cti_hash.csv` | 0 |
| `splunk/cti_cve_kev.csv` | 21 |
| `sentinel/CTI_Ip.csv` | 151 |
| `sentinel/CTI_Dominio.csv` | 318 |
| `sentinel/CTI_Url.csv` | 192 |
| `sentinel/CTI_Hash.csv` | 0 |
| `elastic/cti_ip.ndjson` | 151 |
| `elastic/cti_dominio.ndjson` | 318 |
| `elastic/cti_url.ndjson` | 192 |
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
