# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-23 04:24 UTC  
**Listas generadas:** 2026-10-23T10:48:02Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 204 | Caza programada, no alerta directa |
| Dominio | 764 | Caza programada, no alerta directa |
| URL | 575 | Caza programada, no alerta directa |
| Hash | 671 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 15 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (65 de 2279)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 65 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Vidar | 358 |
| AMOS | 325 |
| IClickFix | 253 |
| StrelaStealer | 191 |
| ClearFake | 152 |
| Unknown malware | 125 |
| Mirai | 107 |
| Coinminer | 107 |
| malware_download | 100 |
| VShell | 91 |
| Unknown Loader | 74 |
| Unknown Stealer | 41 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 204 |
| `wazuh/cti_dominio` | 764 |
| `wazuh/cti_url` | 575 |
| `wazuh/cti_hash` | 671 |
| `wazuh/cti_cve_kev` | 15 |
| `splunk/cti_ip.csv` | 204 |
| `splunk/cti_dominio.csv` | 764 |
| `splunk/cti_url.csv` | 575 |
| `splunk/cti_hash.csv` | 671 |
| `splunk/cti_cve_kev.csv` | 15 |
| `sentinel/CTI_Ip.csv` | 204 |
| `sentinel/CTI_Dominio.csv` | 764 |
| `sentinel/CTI_Url.csv` | 575 |
| `sentinel/CTI_Hash.csv` | 671 |
| `elastic/cti_ip.ndjson` | 204 |
| `elastic/cti_dominio.ndjson` | 764 |
| `elastic/cti_url.ndjson` | 575 |
| `elastic/cti_hash.ndjson` | 671 |

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
