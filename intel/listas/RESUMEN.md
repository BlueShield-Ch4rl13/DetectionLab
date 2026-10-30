# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-30 04:09 UTC  
**Listas generadas:** 2026-10-30T11:56:01Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 253 | Caza programada, no alerta directa |
| Dominio | 2063 | Caza programada, no alerta directa |
| URL | 619 | Caza programada, no alerta directa |
| Hash | 671 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 18 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (135 de 3741)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 135 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| IClickFix | 1467 |
| ClearFake | 447 |
| Vidar | 339 |
| Unknown malware | 286 |
| AMOS | 255 |
| SalatStealer | 192 |
| malware_download | 100 |
| Unknown Loader | 60 |
| SEO Poisoning Campaign Targets DeepSeek Users: Chinese Threat Actor Deploys Kong RAT via Multi-Stage Attacks | 57 |
| VShell | 56 |
| php.shin_webshell | 29 |
| StrelaStealer | 26 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 253 |
| `wazuh/cti_dominio` | 2063 |
| `wazuh/cti_url` | 619 |
| `wazuh/cti_hash` | 671 |
| `wazuh/cti_cve_kev` | 18 |
| `splunk/cti_ip.csv` | 253 |
| `splunk/cti_dominio.csv` | 2063 |
| `splunk/cti_url.csv` | 619 |
| `splunk/cti_hash.csv` | 671 |
| `splunk/cti_cve_kev.csv` | 18 |
| `sentinel/CTI_Ip.csv` | 253 |
| `sentinel/CTI_Dominio.csv` | 2063 |
| `sentinel/CTI_Url.csv` | 619 |
| `sentinel/CTI_Hash.csv` | 671 |
| `elastic/cti_ip.ndjson` | 253 |
| `elastic/cti_dominio.ndjson` | 2063 |
| `elastic/cti_url.ndjson` | 619 |
| `elastic/cti_hash.ndjson` | 671 |

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
