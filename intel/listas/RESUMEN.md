# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-14 04:33 UTC  
**Listas generadas:** 2026-10-14T10:56:49Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 138 | Caza programada, no alerta directa |
| Dominio | 592 | Caza programada, no alerta directa |
| URL | 1220 | Caza programada, no alerta directa |
| Hash | 159 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 12 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (456 de 2594)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 415 |
| nivel bajo | 41 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Vidar | 1006 |
| Unknown Loader | 282 |
| malware_download | 100 |
| ClearFake | 99 |
| Kimsuky attacks targeting Ukrainian experts in diplomacy  security  and international policy | 99 |
| Coruna | 97 |
| The phone was compromised before the user turned it on: the rise of Midnight Mimosa | 60 |
| Unknown Stealer | 57 |
| Unknown malware | 47 |
| php.shin_webshell | 40 |
| Remcos | 25 |
| WARDENStealer | 24 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 138 |
| `wazuh/cti_dominio` | 592 |
| `wazuh/cti_url` | 1220 |
| `wazuh/cti_hash` | 159 |
| `wazuh/cti_cve_kev` | 12 |
| `splunk/cti_ip.csv` | 138 |
| `splunk/cti_dominio.csv` | 592 |
| `splunk/cti_url.csv` | 1220 |
| `splunk/cti_hash.csv` | 159 |
| `splunk/cti_cve_kev.csv` | 12 |
| `sentinel/CTI_Ip.csv` | 138 |
| `sentinel/CTI_Dominio.csv` | 592 |
| `sentinel/CTI_Url.csv` | 1220 |
| `sentinel/CTI_Hash.csv` | 159 |
| `elastic/cti_ip.ndjson` | 138 |
| `elastic/cti_dominio.ndjson` | 592 |
| `elastic/cti_url.ndjson` | 1220 |
| `elastic/cti_hash.ndjson` | 159 |

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
