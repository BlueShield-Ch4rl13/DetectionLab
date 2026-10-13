# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-13 00:32 UTC  
**Listas generadas:** 2026-10-13T13:16:50Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 216 | Caza programada, no alerta directa |
| Dominio | 203 | Caza programada, no alerta directa |
| URL | 462 | Caza programada, no alerta directa |
| Hash | 64 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 11 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (477 de 1451)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 424 |
| nivel bajo | 53 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Vidar | 323 |
| malware_download | 100 |
| DanaBot | 57 |
| Unknown malware | 52 |
| php.shin_webshell | 45 |
| ClearFake | 29 |
| Mirai | 27 |
| Remcos | 27 |
| IClickFix | 23 |
| Casbaneiro: A Banking Trojan with Distributed Data-Receiving Servers | 23 |
| PureRAT | 17 |
| Jackskid | 15 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 216 |
| `wazuh/cti_dominio` | 203 |
| `wazuh/cti_url` | 462 |
| `wazuh/cti_hash` | 64 |
| `wazuh/cti_cve_kev` | 11 |
| `splunk/cti_ip.csv` | 216 |
| `splunk/cti_dominio.csv` | 203 |
| `splunk/cti_url.csv` | 462 |
| `splunk/cti_hash.csv` | 64 |
| `splunk/cti_cve_kev.csv` | 11 |
| `sentinel/CTI_Ip.csv` | 216 |
| `sentinel/CTI_Dominio.csv` | 203 |
| `sentinel/CTI_Url.csv` | 462 |
| `sentinel/CTI_Hash.csv` | 64 |
| `elastic/cti_ip.ndjson` | 216 |
| `elastic/cti_dominio.ndjson` | 203 |
| `elastic/cti_url.ndjson` | 462 |
| `elastic/cti_hash.ndjson` | 64 |

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
