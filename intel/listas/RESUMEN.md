# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-19 04:18 UTC  
**Listas generadas:** 2026-10-19T11:43:50Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 236 | Caza programada, no alerta directa |
| Dominio | 506 | Caza programada, no alerta directa |
| URL | 533 | Caza programada, no alerta directa |
| Hash | 111 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 0 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (428 de 1931)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 340 |
| nivel bajo | 88 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Vidar | 331 |
| Unknown Loader | 220 |
| IClickFix | 173 |
| Unknown malware | 117 |
| malware_download | 100 |
| Mirai | 52 |
| Sliver | 47 |
| VectraRAT: An Undocumented Full-Stack MaaS Built From Scratch | 36 |
| php.shin_webshell | 32 |
| Beware the SparroWock: The backdoor that bites  the commands that catch | 31 |
| ClearFake | 29 |
| SMSspy | 20 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 236 |
| `wazuh/cti_dominio` | 506 |
| `wazuh/cti_url` | 533 |
| `wazuh/cti_hash` | 111 |
| `wazuh/cti_cve_kev` | 0 |
| `splunk/cti_ip.csv` | 236 |
| `splunk/cti_dominio.csv` | 506 |
| `splunk/cti_url.csv` | 533 |
| `splunk/cti_hash.csv` | 111 |
| `splunk/cti_cve_kev.csv` | 0 |
| `sentinel/CTI_Ip.csv` | 236 |
| `sentinel/CTI_Dominio.csv` | 506 |
| `sentinel/CTI_Url.csv` | 533 |
| `sentinel/CTI_Hash.csv` | 111 |
| `elastic/cti_ip.ndjson` | 236 |
| `elastic/cti_dominio.ndjson` | 506 |
| `elastic/cti_url.ndjson` | 533 |
| `elastic/cti_hash.ndjson` | 111 |

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
