# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-10 05:28 UTC  
**Listas generadas:** 2026-10-10T11:40:58Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 123 | Caza programada, no alerta directa |
| Dominio | 823 | Caza programada, no alerta directa |
| URL | 294 | Caza programada, no alerta directa |
| Hash | 78 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 13 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (575 de 1911)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 474 |
| nivel bajo | 101 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| ClearFake | 391 |
| IClickFix | 294 |
| Unknown malware | 128 |
| malware_download | 100 |
| Unknown Loader | 56 |
| php.shin_webshell | 49 |
| Warden Stealer: The Rapid Rise of an Infostealer with an Appetite for AI Agent Data | 27 |
| Vidar | 24 |
| DanaBot | 22 |
| Unknown Stealer | 19 |
| VShell | 17 |
| Suspected TraderTraitor Group Uses Trojanized Terraform Provider to Deliver Cross-Platform Malware | 16 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 123 |
| `wazuh/cti_dominio` | 823 |
| `wazuh/cti_url` | 294 |
| `wazuh/cti_hash` | 78 |
| `wazuh/cti_cve_kev` | 13 |
| `splunk/cti_ip.csv` | 123 |
| `splunk/cti_dominio.csv` | 823 |
| `splunk/cti_url.csv` | 294 |
| `splunk/cti_hash.csv` | 78 |
| `splunk/cti_cve_kev.csv` | 13 |
| `sentinel/CTI_Ip.csv` | 123 |
| `sentinel/CTI_Dominio.csv` | 823 |
| `sentinel/CTI_Url.csv` | 294 |
| `sentinel/CTI_Hash.csv` | 78 |
| `elastic/cti_ip.ndjson` | 123 |
| `elastic/cti_dominio.ndjson` | 823 |
| `elastic/cti_url.ndjson` | 294 |
| `elastic/cti_hash.ndjson` | 78 |

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
