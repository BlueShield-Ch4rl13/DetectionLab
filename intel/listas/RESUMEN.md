# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-01 03:57 UTC  
**Listas generadas:** 2026-11-01T12:26:39Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 258 | Caza programada, no alerta directa |
| Dominio | 600 | Caza programada, no alerta directa |
| URL | 271 | Caza programada, no alerta directa |
| Hash | 616 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (51 de 1796)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 51 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| ClearFake | 289 |
| Mirai | 204 |
| IClickFix | 171 |
| Unknown malware | 147 |
| malware_download | 100 |
| Unknown Loader | 92 |
| SalatStealer | 91 |
| VShell | 86 |
| 2CLoader: A New Malware Loader Delivering Vidar and Remus | 47 |
| SmartLoader | 45 |
| stealler | 40 |
| AMOS | 36 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 258 |
| `wazuh/cti_dominio` | 600 |
| `wazuh/cti_url` | 271 |
| `wazuh/cti_hash` | 616 |
| `wazuh/cti_cve_kev` | 18 |
| `splunk/cti_ip.csv` | 258 |
| `splunk/cti_dominio.csv` | 600 |
| `splunk/cti_url.csv` | 271 |
| `splunk/cti_hash.csv` | 616 |
| `splunk/cti_cve_kev.csv` | 18 |
| `sentinel/CTI_Ip.csv` | 258 |
| `sentinel/CTI_Dominio.csv` | 600 |
| `sentinel/CTI_Url.csv` | 271 |
| `sentinel/CTI_Hash.csv` | 616 |
| `elastic/cti_ip.ndjson` | 258 |
| `elastic/cti_dominio.ndjson` | 600 |
| `elastic/cti_url.ndjson` | 271 |
| `elastic/cti_hash.ndjson` | 616 |

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
