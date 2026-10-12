# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-12 05:33 UTC  
**Listas generadas:** 2026-10-12T14:03:03Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 210 | Caza programada, no alerta directa |
| Dominio | 206 | Caza programada, no alerta directa |
| URL | 337 | Caza programada, no alerta directa |
| Hash | 146 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 11 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (250 de 1196)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 204 |
| nivel bajo | 46 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Vidar | 233 |
| malware_download | 98 |
| Mantax Otax: Indonesian Mobile Ransomware with Spyware Integration | 90 |
| Unknown malware | 55 |
| php.shin_webshell | 49 |
| DanaBot | 41 |
| Mirai | 31 |
| ClearFake | 28 |
| VShell | 26 |
| Sliver | 25 |
| Casbaneiro: A Banking Trojan with Distributed Data-Receiving Servers | 23 |
| AsyncRAT | 16 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 210 |
| `wazuh/cti_dominio` | 206 |
| `wazuh/cti_url` | 337 |
| `wazuh/cti_hash` | 146 |
| `wazuh/cti_cve_kev` | 11 |
| `splunk/cti_ip.csv` | 210 |
| `splunk/cti_dominio.csv` | 206 |
| `splunk/cti_url.csv` | 337 |
| `splunk/cti_hash.csv` | 146 |
| `splunk/cti_cve_kev.csv` | 11 |
| `sentinel/CTI_Ip.csv` | 210 |
| `sentinel/CTI_Dominio.csv` | 206 |
| `sentinel/CTI_Url.csv` | 337 |
| `sentinel/CTI_Hash.csv` | 146 |
| `elastic/cti_ip.ndjson` | 210 |
| `elastic/cti_dominio.ndjson` | 206 |
| `elastic/cti_url.ndjson` | 337 |
| `elastic/cti_hash.ndjson` | 146 |

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
