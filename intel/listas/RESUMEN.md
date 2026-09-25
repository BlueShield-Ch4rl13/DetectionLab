# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-25 04:34 UTC  
**Listas generadas:** 2026-09-25T10:54:28Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 95 | Caza programada, no alerta directa |
| Dominio | 1062 | Caza programada, no alerta directa |
| URL | 235 | Caza programada, no alerta directa |
| Hash | 63 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (265 de 1753)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 215 |
| nivel bajo | 50 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown Loader | 848 |
| malware_download | 100 |
| ClearFake | 99 |
| Unknown malware | 72 |
| IClickFix | 69 |
| A new version of the MacSync macOS stealer targets crypto enthusiasts and developers | 29 |
| Tracking PavinLoader across ClickFix and fake download campaigns | 29 |
| php.shin_webshell | 26 |
| Remcos | 21 |
| Cobalt Strike | 18 |
| Remus | 16 |
| Mozi | 16 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 95 |
| `wazuh/cti_dominio` | 1062 |
| `wazuh/cti_url` | 235 |
| `wazuh/cti_hash` | 63 |
| `wazuh/cti_cve_kev` | 18 |
| `splunk/cti_ip.csv` | 95 |
| `splunk/cti_dominio.csv` | 1062 |
| `splunk/cti_url.csv` | 235 |
| `splunk/cti_hash.csv` | 63 |
| `splunk/cti_cve_kev.csv` | 18 |
| `sentinel/CTI_Ip.csv` | 95 |
| `sentinel/CTI_Dominio.csv` | 1062 |
| `sentinel/CTI_Url.csv` | 235 |
| `sentinel/CTI_Hash.csv` | 63 |
| `elastic/cti_ip.ndjson` | 95 |
| `elastic/cti_dominio.ndjson` | 1062 |
| `elastic/cti_url.ndjson` | 235 |
| `elastic/cti_hash.ndjson` | 63 |

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
