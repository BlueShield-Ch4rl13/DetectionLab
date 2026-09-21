# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-21 04:32 UTC  
**Listas generadas:** 2026-09-21T11:36:59Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 162 | Caza programada, no alerta directa |
| Dominio | 180 | Caza programada, no alerta directa |
| URL | 172 | Caza programada, no alerta directa |
| Hash | 190 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 21 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (1124 de 1885)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 1114 |
| nivel bajo | 10 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| SilkParasite: Tracking a China-Nexus APT Across Central Asia | 102 |
| malware_download | 100 |
| Unknown malware | 84 |
| Unknown Loader | 77 |
| ClearFake | 67 |
| 77 Firefox Extensions Linked to Crypto Wallet and Credential Theft | 51 |
| Head Mare APT Group exploits vulnerabilities in unpatched TrueConf server to deliver PhantomCore malware to conference participants | 37 |
| VShell | 34 |
| php.shin_webshell | 25 |
| Cobalt Strike | 20 |
| Aisuru | 11 |
| AsyncRAT | 11 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 162 |
| `wazuh/cti_dominio` | 180 |
| `wazuh/cti_url` | 172 |
| `wazuh/cti_hash` | 190 |
| `wazuh/cti_cve_kev` | 21 |
| `splunk/cti_ip.csv` | 162 |
| `splunk/cti_dominio.csv` | 180 |
| `splunk/cti_url.csv` | 172 |
| `splunk/cti_hash.csv` | 190 |
| `splunk/cti_cve_kev.csv` | 21 |
| `sentinel/CTI_Ip.csv` | 162 |
| `sentinel/CTI_Dominio.csv` | 180 |
| `sentinel/CTI_Url.csv` | 172 |
| `sentinel/CTI_Hash.csv` | 190 |
| `elastic/cti_ip.ndjson` | 162 |
| `elastic/cti_dominio.ndjson` | 180 |
| `elastic/cti_url.ndjson` | 172 |
| `elastic/cti_hash.ndjson` | 190 |

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
