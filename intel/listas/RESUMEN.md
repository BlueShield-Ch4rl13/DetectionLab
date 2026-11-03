# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-03 05:08 UTC  
**Listas generadas:** 2026-11-03T13:22:58Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 896 | Caza programada, no alerta directa |
| Dominio | 870 | Caza programada, no alerta directa |
| URL | 253 | Caza programada, no alerta directa |
| Hash | 751 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (25 de 2795)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 25 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown malware | 951 |
| Unknown Loader | 374 |
| AMOS | 291 |
| ClearFake | 248 |
| IClickFix | 121 |
| Shutting the Door on the XCPE Botnet | 105 |
| malware_download | 100 |
| Vidar | 46 |
| VShell | 46 |
| Mirai | 41 |
| SalatStealer | 35 |
| XMRIG | 28 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 896 |
| `wazuh/cti_dominio` | 870 |
| `wazuh/cti_url` | 253 |
| `wazuh/cti_hash` | 751 |
| `wazuh/cti_cve_kev` | 18 |
| `splunk/cti_ip.csv` | 896 |
| `splunk/cti_dominio.csv` | 870 |
| `splunk/cti_url.csv` | 253 |
| `splunk/cti_hash.csv` | 751 |
| `splunk/cti_cve_kev.csv` | 18 |
| `sentinel/CTI_Ip.csv` | 896 |
| `sentinel/CTI_Dominio.csv` | 870 |
| `sentinel/CTI_Url.csv` | 253 |
| `sentinel/CTI_Hash.csv` | 751 |
| `elastic/cti_ip.ndjson` | 896 |
| `elastic/cti_dominio.ndjson` | 870 |
| `elastic/cti_url.ndjson` | 253 |
| `elastic/cti_hash.ndjson` | 751 |

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
