# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-24 04:20 UTC  
**Listas generadas:** 2026-09-24T10:51:55Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 125 | Caza programada, no alerta directa |
| Dominio | 2300 | Caza programada, no alerta directa |
| URL | 341 | Caza programada, no alerta directa |
| Hash | 58 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 18 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (465 de 3321)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 386 |
| nivel bajo | 79 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| IClickFix | 1796 |
| Unknown Loader | 271 |
| ClearFake | 170 |
| Unknown malware | 114 |
| malware_download | 100 |
| Remus | 39 |
| Unknown Stealer | 32 |
| Vidar | 31 |
| php.shin_webshell | 24 |
| Remcos | 23 |
| RemControl: AI Built the Overlays. Victims Lose their PINs | 20 |
| Cobalt Strike | 19 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 125 |
| `wazuh/cti_dominio` | 2300 |
| `wazuh/cti_url` | 341 |
| `wazuh/cti_hash` | 58 |
| `wazuh/cti_cve_kev` | 18 |
| `splunk/cti_ip.csv` | 125 |
| `splunk/cti_dominio.csv` | 2300 |
| `splunk/cti_url.csv` | 341 |
| `splunk/cti_hash.csv` | 58 |
| `splunk/cti_cve_kev.csv` | 18 |
| `sentinel/CTI_Ip.csv` | 125 |
| `sentinel/CTI_Dominio.csv` | 2300 |
| `sentinel/CTI_Url.csv` | 341 |
| `sentinel/CTI_Hash.csv` | 58 |
| `elastic/cti_ip.ndjson` | 125 |
| `elastic/cti_dominio.ndjson` | 2300 |
| `elastic/cti_url.ndjson` | 341 |
| `elastic/cti_hash.ndjson` | 58 |

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
