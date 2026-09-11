# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-11 04:13 UTC  
**Listas generadas:** 2026-09-11T10:21:07Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 189 | Caza programada, no alerta directa |
| Dominio | 1291 | Caza programada, no alerta directa |
| URL | 175 | Caza programada, no alerta directa |
| Hash | 97 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 20 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (3563 de 5331)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 3475 |
| nivel bajo | 88 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown Loader | 869 |
| ClearFake | 177 |
| IClickFix | 164 |
| malware_download | 100 |
| VShell | 99 |
| Unknown malware | 44 |
| PhantomCore and PhantomGraph backdoors delivered via an unpatched TrueConf server | 32 |
| php.shin_webshell | 30 |
| An Evolution of the Botnet | 26 |
| Unknown RAT | 25 |
| KongTuke | 15 |
| Death by a Thousand PaperCuts: AI-Driven Exploitation at Scale | 14 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 189 |
| `wazuh/cti_dominio` | 1291 |
| `wazuh/cti_url` | 175 |
| `wazuh/cti_hash` | 97 |
| `wazuh/cti_cve_kev` | 20 |
| `splunk/cti_ip.csv` | 189 |
| `splunk/cti_dominio.csv` | 1291 |
| `splunk/cti_url.csv` | 175 |
| `splunk/cti_hash.csv` | 97 |
| `splunk/cti_cve_kev.csv` | 20 |
| `sentinel/CTI_Ip.csv` | 189 |
| `sentinel/CTI_Dominio.csv` | 1291 |
| `sentinel/CTI_Url.csv` | 175 |
| `sentinel/CTI_Hash.csv` | 97 |
| `elastic/cti_ip.ndjson` | 189 |
| `elastic/cti_dominio.ndjson` | 1291 |
| `elastic/cti_url.ndjson` | 175 |
| `elastic/cti_hash.ndjson` | 97 |

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
