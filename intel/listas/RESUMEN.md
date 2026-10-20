# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-20 04:30 UTC  
**Listas generadas:** 2026-10-20T10:44:47Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 131 | Caza programada, no alerta directa |
| Dominio | 185 | Caza programada, no alerta directa |
| URL | 488 | Caza programada, no alerta directa |
| Hash | 101 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 14 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (572 de 1536)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 488 |
| nivel bajo | 84 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Vidar | 327 |
| malware_download | 100 |
| Unknown malware | 88 |
| BREAK THE SILENCE: Tracking Silent Lynx Through Exposed Infrastructure | 69 |
| ClearFake | 41 |
| php.shin_webshell | 32 |
| Remcos | 21 |
| SMSspy | 20 |
| Unknown Loader | 16 |
| VShell | 15 |
| Sliver | 10 |
| Hermes | 10 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 131 |
| `wazuh/cti_dominio` | 185 |
| `wazuh/cti_url` | 488 |
| `wazuh/cti_hash` | 101 |
| `wazuh/cti_cve_kev` | 14 |
| `splunk/cti_ip.csv` | 131 |
| `splunk/cti_dominio.csv` | 185 |
| `splunk/cti_url.csv` | 488 |
| `splunk/cti_hash.csv` | 101 |
| `splunk/cti_cve_kev.csv` | 14 |
| `sentinel/CTI_Ip.csv` | 131 |
| `sentinel/CTI_Dominio.csv` | 185 |
| `sentinel/CTI_Url.csv` | 488 |
| `sentinel/CTI_Hash.csv` | 101 |
| `elastic/cti_ip.ndjson` | 131 |
| `elastic/cti_dominio.ndjson` | 185 |
| `elastic/cti_url.ndjson` | 488 |
| `elastic/cti_hash.ndjson` | 101 |

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
