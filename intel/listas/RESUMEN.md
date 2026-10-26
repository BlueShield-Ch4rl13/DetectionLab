# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-26 04:22 UTC  
**Listas generadas:** 2026-10-26T12:00:02Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 1681 | Caza programada, no alerta directa |
| Dominio | 1181 | Caza programada, no alerta directa |
| URL | 472 | Caza programada, no alerta directa |
| Hash | 2499 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (66 de 5899)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 66 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| VShell | 1803 |
| Unknown malware | 1393 |
| IClickFix | 737 |
| AMOS | 283 |
| Mirai | 215 |
| SalatStealer | 193 |
| Cobalt Strike | 174 |
| ClearFake | 162 |
| Unknown Loader | 159 |
| Sliver | 104 |
| malware_download | 100 |
| StrelaStealer | 47 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 1681 |
| `wazuh/cti_dominio` | 1181 |
| `wazuh/cti_url` | 472 |
| `wazuh/cti_hash` | 2499 |
| `wazuh/cti_cve_kev` | 17 |
| `splunk/cti_ip.csv` | 1681 |
| `splunk/cti_dominio.csv` | 1181 |
| `splunk/cti_url.csv` | 472 |
| `splunk/cti_hash.csv` | 2499 |
| `splunk/cti_cve_kev.csv` | 17 |
| `sentinel/CTI_Ip.csv` | 1681 |
| `sentinel/CTI_Dominio.csv` | 1181 |
| `sentinel/CTI_Url.csv` | 472 |
| `sentinel/CTI_Hash.csv` | 2499 |
| `elastic/cti_ip.ndjson` | 1681 |
| `elastic/cti_dominio.ndjson` | 1181 |
| `elastic/cti_url.ndjson` | 472 |
| `elastic/cti_hash.ndjson` | 2499 |

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
