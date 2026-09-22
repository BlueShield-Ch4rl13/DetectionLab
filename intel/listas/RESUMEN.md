# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-22 04:28 UTC  
**Listas generadas:** 2026-09-22T10:42:02Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 132 | Caza programada, no alerta directa |
| Dominio | 267 | Caza programada, no alerta directa |
| URL | 259 | Caza programada, no alerta directa |
| Hash | 118 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 22 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (222 de 1068)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 165 |
| nivel bajo | 57 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| malware_download | 100 |
| vSkimmer | 71 |
| IClickFix | 70 |
| Unknown malware | 62 |
| ClearFake | 55 |
| Vidar | 47 |
| Remus | 43 |
| Head Mare APT Group exploits vulnerabilities in unpatched TrueConf server to deliver PhantomCore malware to conference participants | 37 |
| SilkParasite: Tracking a China-Nexus APT Across Central Asia | 36 |
| php.shin_webshell | 24 |
| VShell | 21 |
| TonRAT | 20 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 132 |
| `wazuh/cti_dominio` | 267 |
| `wazuh/cti_url` | 259 |
| `wazuh/cti_hash` | 118 |
| `wazuh/cti_cve_kev` | 22 |
| `splunk/cti_ip.csv` | 132 |
| `splunk/cti_dominio.csv` | 267 |
| `splunk/cti_url.csv` | 259 |
| `splunk/cti_hash.csv` | 118 |
| `splunk/cti_cve_kev.csv` | 22 |
| `sentinel/CTI_Ip.csv` | 132 |
| `sentinel/CTI_Dominio.csv` | 267 |
| `sentinel/CTI_Url.csv` | 259 |
| `sentinel/CTI_Hash.csv` | 118 |
| `elastic/cti_ip.ndjson` | 132 |
| `elastic/cti_dominio.ndjson` | 267 |
| `elastic/cti_url.ndjson` | 259 |
| `elastic/cti_hash.ndjson` | 118 |

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
