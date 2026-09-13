# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-13 04:30 UTC  
**Listas generadas:** 2026-09-13T10:52:43Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 161 | Caza programada, no alerta directa |
| Dominio | 117 | Caza programada, no alerta directa |
| URL | 161 | Caza programada, no alerta directa |
| Hash | 69 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 24 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (390 de 924)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 326 |
| nivel bajo | 64 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| malware_download | 100 |
| ClearFake | 75 |
| VShell | 73 |
| Unknown malware | 29 |
| php.shin_webshell | 28 |
| Jewelbug: APT Group Runs Espionage and Crypto Fraud Operations Side by Side | 28 |
| Remus | 23 |
| New Armored Likho tools target Telegram and eavesdropping | 17 |
| Aisuru | 16 |
| PATCHCORD: New malware cluster targets Afghan telecom and South Asian critical infrastructure | 15 |
| Cobalt Strike | 12 |
| Mozi | 11 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 161 |
| `wazuh/cti_dominio` | 117 |
| `wazuh/cti_url` | 161 |
| `wazuh/cti_hash` | 69 |
| `wazuh/cti_cve_kev` | 24 |
| `splunk/cti_ip.csv` | 161 |
| `splunk/cti_dominio.csv` | 117 |
| `splunk/cti_url.csv` | 161 |
| `splunk/cti_hash.csv` | 69 |
| `splunk/cti_cve_kev.csv` | 24 |
| `sentinel/CTI_Ip.csv` | 161 |
| `sentinel/CTI_Dominio.csv` | 117 |
| `sentinel/CTI_Url.csv` | 161 |
| `sentinel/CTI_Hash.csv` | 69 |
| `elastic/cti_ip.ndjson` | 161 |
| `elastic/cti_dominio.ndjson` | 117 |
| `elastic/cti_url.ndjson` | 161 |
| `elastic/cti_hash.ndjson` | 69 |

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
