# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-25 04:17 UTC  
**Listas generadas:** 2026-10-25T10:28:52Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 182 | Caza programada, no alerta directa |
| Dominio | 681 | Caza programada, no alerta directa |
| URL | 247 | Caza programada, no alerta directa |
| Hash | 619 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (49 de 1778)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 47 |
| tipo no usado | 2 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| ClearFake | 379 |
| AMOS | 270 |
| Unknown Loader | 120 |
| Mirai | 116 |
| StrelaStealer | 114 |
| malware_download | 100 |
| SalatStealer | 68 |
| Unknown malware | 58 |
| Raven Stealer | 38 |
| Vidar | 35 |
| php.shin_webshell | 29 |
| Cobalt Strike | 27 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 182 |
| `wazuh/cti_dominio` | 681 |
| `wazuh/cti_url` | 247 |
| `wazuh/cti_hash` | 619 |
| `wazuh/cti_cve_kev` | 17 |
| `splunk/cti_ip.csv` | 182 |
| `splunk/cti_dominio.csv` | 681 |
| `splunk/cti_url.csv` | 247 |
| `splunk/cti_hash.csv` | 619 |
| `splunk/cti_cve_kev.csv` | 17 |
| `sentinel/CTI_Ip.csv` | 182 |
| `sentinel/CTI_Dominio.csv` | 681 |
| `sentinel/CTI_Url.csv` | 247 |
| `sentinel/CTI_Hash.csv` | 619 |
| `elastic/cti_ip.ndjson` | 182 |
| `elastic/cti_dominio.ndjson` | 681 |
| `elastic/cti_url.ndjson` | 247 |
| `elastic/cti_hash.ndjson` | 619 |

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
