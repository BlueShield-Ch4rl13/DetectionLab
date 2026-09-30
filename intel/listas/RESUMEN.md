# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-30 05:13 UTC  
**Listas generadas:** 2026-09-30T11:41:23Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 290 | Caza programada, no alerta directa |
| Dominio | 535 | Caza programada, no alerta directa |
| URL | 221 | Caza programada, no alerta directa |
| Hash | 0 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 19 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (259 de 1362)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 259 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| ClearFake | 236 |
| Unknown Loader | 212 |
| AdaptixC2 | 145 |
| malware_download | 100 |
| Unknown malware | 65 |
| Remus | 40 |
| Vidar | 28 |
| php.shin_webshell | 25 |
| Unknown Webinject | 17 |
| Aisuru | 15 |
| VShell | 15 |
| Mozi | 15 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 290 |
| `wazuh/cti_dominio` | 535 |
| `wazuh/cti_url` | 221 |
| `wazuh/cti_hash` | 0 |
| `wazuh/cti_cve_kev` | 19 |
| `splunk/cti_ip.csv` | 290 |
| `splunk/cti_dominio.csv` | 535 |
| `splunk/cti_url.csv` | 221 |
| `splunk/cti_hash.csv` | 0 |
| `splunk/cti_cve_kev.csv` | 19 |
| `sentinel/CTI_Ip.csv` | 290 |
| `sentinel/CTI_Dominio.csv` | 535 |
| `sentinel/CTI_Url.csv` | 221 |
| `sentinel/CTI_Hash.csv` | 0 |
| `elastic/cti_ip.ndjson` | 290 |
| `elastic/cti_dominio.ndjson` | 535 |
| `elastic/cti_url.ndjson` | 221 |
| `elastic/cti_hash.ndjson` | 0 |

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
