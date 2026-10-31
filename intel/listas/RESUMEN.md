# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-31 03:51 UTC  
**Listas generadas:** 2026-10-31T11:29:32Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 211 | Caza programada, no alerta directa |
| Dominio | 570 | Caza programada, no alerta directa |
| URL | 377 | Caza programada, no alerta directa |
| Hash | 530 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (74 de 1762)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 74 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| IClickFix | 337 |
| AMOS | 286 |
| Vidar | 179 |
| ClearFake | 140 |
| VShell | 105 |
| Unknown malware | 104 |
| malware_download | 100 |
| SalatStealer | 74 |
| 2CLoader: A New Malware Loader Delivering Vidar and Remus | 47 |
| SmartLoader | 46 |
| StrelaStealer | 38 |
| Mirai | 27 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 211 |
| `wazuh/cti_dominio` | 570 |
| `wazuh/cti_url` | 377 |
| `wazuh/cti_hash` | 530 |
| `wazuh/cti_cve_kev` | 18 |
| `splunk/cti_ip.csv` | 211 |
| `splunk/cti_dominio.csv` | 570 |
| `splunk/cti_url.csv` | 377 |
| `splunk/cti_hash.csv` | 530 |
| `splunk/cti_cve_kev.csv` | 18 |
| `sentinel/CTI_Ip.csv` | 211 |
| `sentinel/CTI_Dominio.csv` | 570 |
| `sentinel/CTI_Url.csv` | 377 |
| `sentinel/CTI_Hash.csv` | 530 |
| `elastic/cti_ip.ndjson` | 211 |
| `elastic/cti_dominio.ndjson` | 570 |
| `elastic/cti_url.ndjson` | 377 |
| `elastic/cti_hash.ndjson` | 530 |

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
