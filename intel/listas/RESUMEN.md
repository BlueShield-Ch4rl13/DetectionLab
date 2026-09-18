# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-18 04:18 UTC  
**Listas generadas:** 2026-09-18T10:20:02Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 168 | Caza programada, no alerta directa |
| Dominio | 691 | Caza programada, no alerta directa |
| URL | 256 | Caza programada, no alerta directa |
| Hash | 22 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (1337 de 2544)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 1159 |
| nivel bajo | 178 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown Stealer | 227 |
| Unknown malware | 158 |
| malware_download | 98 |
| Remcos | 81 |
| Unknown Loader | 73 |
| ClearFake | 69 |
| IClickFix | 67 |
| Remus | 58 |
| Jackskid | 31 |
| MacSync | 30 |
| php.shin_webshell | 28 |
| Vidar | 22 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 168 |
| `wazuh/cti_dominio` | 691 |
| `wazuh/cti_url` | 256 |
| `wazuh/cti_hash` | 22 |
| `wazuh/cti_cve_kev` | 19 |
| `splunk/cti_ip.csv` | 168 |
| `splunk/cti_dominio.csv` | 691 |
| `splunk/cti_url.csv` | 256 |
| `splunk/cti_hash.csv` | 22 |
| `splunk/cti_cve_kev.csv` | 19 |
| `sentinel/CTI_Ip.csv` | 168 |
| `sentinel/CTI_Dominio.csv` | 691 |
| `sentinel/CTI_Url.csv` | 256 |
| `sentinel/CTI_Hash.csv` | 22 |
| `elastic/cti_ip.ndjson` | 168 |
| `elastic/cti_dominio.ndjson` | 691 |
| `elastic/cti_url.ndjson` | 256 |
| `elastic/cti_hash.ndjson` | 22 |

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
