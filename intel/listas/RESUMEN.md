# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-08 05:41 UTC  
**Listas generadas:** 2026-10-08T12:34:17Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 139 | Caza programada, no alerta directa |
| Dominio | 354 | Caza programada, no alerta directa |
| URL | 227 | Caza programada, no alerta directa |
| Hash | 39 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (376 de 1156)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 216 |
| nivel bajo | 160 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown Stealer | 158 |
| malware_download | 100 |
| ClearFake | 75 |
| IClickFix | 55 |
| ContagiousDrop | 35 |
| Vidar | 29 |
| Unknown Loader | 29 |
| php.shin_webshell | 24 |
| Iranian State-Aligned Threat Actor Masquerading as Dubai Airports IT Department Delivering Trojanized Coding Challenges - Blinder Tunnel Campaign Targeting Iraqi Critical Infrastructure | 24 |
| PureRAT | 22 |
| Unknown malware | 21 |
| Remus | 17 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 139 |
| `wazuh/cti_dominio` | 354 |
| `wazuh/cti_url` | 227 |
| `wazuh/cti_hash` | 39 |
| `wazuh/cti_cve_kev` | 13 |
| `splunk/cti_ip.csv` | 139 |
| `splunk/cti_dominio.csv` | 354 |
| `splunk/cti_url.csv` | 227 |
| `splunk/cti_hash.csv` | 39 |
| `splunk/cti_cve_kev.csv` | 13 |
| `sentinel/CTI_Ip.csv` | 139 |
| `sentinel/CTI_Dominio.csv` | 354 |
| `sentinel/CTI_Url.csv` | 227 |
| `sentinel/CTI_Hash.csv` | 39 |
| `elastic/cti_ip.ndjson` | 139 |
| `elastic/cti_dominio.ndjson` | 354 |
| `elastic/cti_url.ndjson` | 227 |
| `elastic/cti_hash.ndjson` | 39 |

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
