# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-15 04:15 UTC  
**Listas generadas:** 2026-10-15T10:38:34Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 174 | Caza programada, no alerta directa |
| Dominio | 291 | Caza programada, no alerta directa |
| URL | 1142 | Caza programada, no alerta directa |
| Hash | 120 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (367 de 2140)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 338 |
| nivel bajo | 29 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Vidar | 993 |
| malware_download | 99 |
| Coruna | 97 |
| ClingSTUN Turns Vulnerable Edge Devices Into Attacker Infrastructure | 57 |
| php.shin_webshell | 52 |
| ClearFake | 43 |
| Unknown malware | 41 |
| Remcos | 33 |
| Unknown Loader | 29 |
| WARDENStealer | 28 |
| GHOSTBLADE | 18 |
| 2026 Q3 Linux SSH Server Targeted Malware Statistics Report | 15 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 174 |
| `wazuh/cti_dominio` | 291 |
| `wazuh/cti_url` | 1142 |
| `wazuh/cti_hash` | 120 |
| `wazuh/cti_cve_kev` | 15 |
| `splunk/cti_ip.csv` | 174 |
| `splunk/cti_dominio.csv` | 291 |
| `splunk/cti_url.csv` | 1142 |
| `splunk/cti_hash.csv` | 120 |
| `splunk/cti_cve_kev.csv` | 15 |
| `sentinel/CTI_Ip.csv` | 174 |
| `sentinel/CTI_Dominio.csv` | 291 |
| `sentinel/CTI_Url.csv` | 1142 |
| `sentinel/CTI_Hash.csv` | 120 |
| `elastic/cti_ip.ndjson` | 174 |
| `elastic/cti_dominio.ndjson` | 291 |
| `elastic/cti_url.ndjson` | 1142 |
| `elastic/cti_hash.ndjson` | 120 |

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
