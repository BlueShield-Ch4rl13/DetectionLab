# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-02 05:13 UTC  
**Listas generadas:** 2026-10-02T11:40:20Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 145 | Caza programada, no alerta directa |
| Dominio | 775 | Caza programada, no alerta directa |
| URL | 298 | Caza programada, no alerta directa |
| Hash | 107 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (437 de 1795)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 358 |
| nivel bajo | 79 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| IClickFix | 608 |
| Unknown malware | 107 |
| malware_download | 100 |
| ClearFake | 66 |
| Vidar | 60 |
| 2CLoader: A New Malware Loader Delivering Vidar and Remus | 47 |
| Remus | 34 |
| php.shin_webshell | 25 |
| VShell | 21 |
| Unknown Loader | 17 |
| XWorm | 16 |
| PaperCut MF Zero-Day Intrusion: Java Loader  Web Shell  and AdaptixC2 via CVE-2026-82078 and CVE-2026-81578 | 16 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 145 |
| `wazuh/cti_dominio` | 775 |
| `wazuh/cti_url` | 298 |
| `wazuh/cti_hash` | 107 |
| `wazuh/cti_cve_kev` | 18 |
| `splunk/cti_ip.csv` | 145 |
| `splunk/cti_dominio.csv` | 775 |
| `splunk/cti_url.csv` | 298 |
| `splunk/cti_hash.csv` | 107 |
| `splunk/cti_cve_kev.csv` | 18 |
| `sentinel/CTI_Ip.csv` | 145 |
| `sentinel/CTI_Dominio.csv` | 775 |
| `sentinel/CTI_Url.csv` | 298 |
| `sentinel/CTI_Hash.csv` | 107 |
| `elastic/cti_ip.ndjson` | 145 |
| `elastic/cti_dominio.ndjson` | 775 |
| `elastic/cti_url.ndjson` | 298 |
| `elastic/cti_hash.ndjson` | 107 |

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
