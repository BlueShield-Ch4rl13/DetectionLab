# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-16 04:11 UTC  
**Listas generadas:** 2026-10-16T10:25:25Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 190 | Caza programada, no alerta directa |
| Dominio | 444 | Caza programada, no alerta directa |
| URL | 1117 | Caza programada, no alerta directa |
| Hash | 44 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (725 de 2561)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 590 |
| nivel bajo | 135 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Vidar | 989 |
| IClickFix | 159 |
| malware_download | 100 |
| Unknown Loader | 90 |
| vSkimmer | 63 |
| Remus | 50 |
| VShell | 48 |
| php.shin_webshell | 45 |
| Remcos | 31 |
| Unknown malware | 27 |
| ClearFake | 26 |
| Aoki: Infostealer Targets AI Coding Assistant Credentials | 21 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 190 |
| `wazuh/cti_dominio` | 444 |
| `wazuh/cti_url` | 1117 |
| `wazuh/cti_hash` | 44 |
| `wazuh/cti_cve_kev` | 15 |
| `splunk/cti_ip.csv` | 190 |
| `splunk/cti_dominio.csv` | 444 |
| `splunk/cti_url.csv` | 1117 |
| `splunk/cti_hash.csv` | 44 |
| `splunk/cti_cve_kev.csv` | 15 |
| `sentinel/CTI_Ip.csv` | 190 |
| `sentinel/CTI_Dominio.csv` | 444 |
| `sentinel/CTI_Url.csv` | 1117 |
| `sentinel/CTI_Hash.csv` | 44 |
| `elastic/cti_ip.ndjson` | 190 |
| `elastic/cti_dominio.ndjson` | 444 |
| `elastic/cti_url.ndjson` | 1117 |
| `elastic/cti_hash.ndjson` | 44 |

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
