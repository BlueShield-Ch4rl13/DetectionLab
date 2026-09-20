# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-20 04:34 UTC  
**Listas generadas:** 2026-09-20T10:22:21Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 126 | Caza programada, no alerta directa |
| Dominio | 131 | Caza programada, no alerta directa |
| URL | 202 | Caza programada, no alerta directa |
| Hash | 189 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (77 de 781)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 66 |
| nivel bajo | 11 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| SilkParasite: Tracking a China-Nexus APT Across Central Asia | 102 |
| malware_download | 100 |
| 77 Firefox Extensions Linked to Crypto Wallet and Credential Theft | 87 |
| VShell | 55 |
| ClearFake | 53 |
| IClickFix | 38 |
| Unknown malware | 34 |
| php.shin_webshell | 26 |
| Cobalt Strike | 25 |
| Aisuru | 13 |
| xmrig | 12 |
| AMOS | 10 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 126 |
| `wazuh/cti_dominio` | 131 |
| `wazuh/cti_url` | 202 |
| `wazuh/cti_hash` | 189 |
| `wazuh/cti_cve_kev` | 21 |
| `splunk/cti_ip.csv` | 126 |
| `splunk/cti_dominio.csv` | 131 |
| `splunk/cti_url.csv` | 202 |
| `splunk/cti_hash.csv` | 189 |
| `splunk/cti_cve_kev.csv` | 21 |
| `sentinel/CTI_Ip.csv` | 126 |
| `sentinel/CTI_Dominio.csv` | 131 |
| `sentinel/CTI_Url.csv` | 202 |
| `sentinel/CTI_Hash.csv` | 189 |
| `elastic/cti_ip.ndjson` | 126 |
| `elastic/cti_dominio.ndjson` | 131 |
| `elastic/cti_url.ndjson` | 202 |
| `elastic/cti_hash.ndjson` | 189 |

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
