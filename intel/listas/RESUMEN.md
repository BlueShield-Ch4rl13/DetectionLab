# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-06 04:09 UTC  
**Listas generadas:** 2026-09-06T10:00:45Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 142 | Caza programada, no alerta directa |
| Dominio | 248 | Caza programada, no alerta directa |
| URL | 162 | Caza programada, no alerta directa |
| Hash | 72 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 21 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (390 de 1046)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 266 |
| nivel bajo | 124 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown Loader | 123 |
| malware_download | 99 |
| ClearFake | 76 |
| VShell | 52 |
| Contagious Interview steps outside the developer workflow | 28 |
| ENDLESSDOORS Is Phoning Home. Pick Up. | 27 |
| Unknown malware | 23 |
| php.shin_webshell | 20 |
| KongTuke | 15 |
| PureRAT | 13 |
| Cobalt Strike | 13 |
| Mozi | 12 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 142 |
| `wazuh/cti_dominio` | 248 |
| `wazuh/cti_url` | 162 |
| `wazuh/cti_hash` | 72 |
| `wazuh/cti_cve_kev` | 21 |
| `splunk/cti_ip.csv` | 142 |
| `splunk/cti_dominio.csv` | 248 |
| `splunk/cti_url.csv` | 162 |
| `splunk/cti_hash.csv` | 72 |
| `splunk/cti_cve_kev.csv` | 21 |
| `sentinel/CTI_Ip.csv` | 142 |
| `sentinel/CTI_Dominio.csv` | 248 |
| `sentinel/CTI_Url.csv` | 162 |
| `sentinel/CTI_Hash.csv` | 72 |
| `elastic/cti_ip.ndjson` | 142 |
| `elastic/cti_dominio.ndjson` | 248 |
| `elastic/cti_url.ndjson` | 162 |
| `elastic/cti_hash.ndjson` | 72 |

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
