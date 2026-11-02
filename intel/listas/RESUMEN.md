# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-02 10:38 UTC  
**Listas generadas:** 2026-11-02T14:23:52Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 161 | Caza programada, no alerta directa |
| Dominio | 998 | Caza programada, no alerta directa |
| URL | 273 | Caza programada, no alerta directa |
| Hash | 877 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (33 de 2342)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 33 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| IClickFix | 350 |
| AMOS | 300 |
| Unknown Loader | 285 |
| ClearFake | 276 |
| Unknown malware | 240 |
| malware_download | 100 |
| Mirai | 77 |
| StrelaStealer | 67 |
| Vidar | 48 |
| 2CLoader: A New Malware Loader Delivering Vidar and Remus | 47 |
| win.icexloader | 42 |
| PureRAT | 36 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 161 |
| `wazuh/cti_dominio` | 998 |
| `wazuh/cti_url` | 273 |
| `wazuh/cti_hash` | 877 |
| `wazuh/cti_cve_kev` | 18 |
| `splunk/cti_ip.csv` | 161 |
| `splunk/cti_dominio.csv` | 998 |
| `splunk/cti_url.csv` | 273 |
| `splunk/cti_hash.csv` | 877 |
| `splunk/cti_cve_kev.csv` | 18 |
| `sentinel/CTI_Ip.csv` | 161 |
| `sentinel/CTI_Dominio.csv` | 998 |
| `sentinel/CTI_Url.csv` | 273 |
| `sentinel/CTI_Hash.csv` | 877 |
| `elastic/cti_ip.ndjson` | 161 |
| `elastic/cti_dominio.ndjson` | 998 |
| `elastic/cti_url.ndjson` | 273 |
| `elastic/cti_hash.ndjson` | 877 |

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
