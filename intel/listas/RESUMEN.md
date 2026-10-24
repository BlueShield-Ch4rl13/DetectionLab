# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-24 04:15 UTC  
**Listas generadas:** 2026-10-24T10:03:45Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 147 | Caza programada, no alerta directa |
| Dominio | 395 | Caza programada, no alerta directa |
| URL | 295 | Caza programada, no alerta directa |
| Hash | 615 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 17 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (101 de 1553)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 99 |
| tipo no usado | 2 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| AMOS | 280 |
| IClickFix | 175 |
| Vidar | 173 |
| StrelaStealer | 102 |
| malware_download | 100 |
| Mirai | 69 |
| VShell | 45 |
| ClearFake | 44 |
| php.shin_webshell | 27 |
| Raven Stealer | 24 |
| Unknown malware | 21 |
| SEO Poisoning Campaign Delivers New Armorsteal Malware | 21 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 147 |
| `wazuh/cti_dominio` | 395 |
| `wazuh/cti_url` | 295 |
| `wazuh/cti_hash` | 615 |
| `wazuh/cti_cve_kev` | 17 |
| `splunk/cti_ip.csv` | 147 |
| `splunk/cti_dominio.csv` | 395 |
| `splunk/cti_url.csv` | 295 |
| `splunk/cti_hash.csv` | 615 |
| `splunk/cti_cve_kev.csv` | 17 |
| `sentinel/CTI_Ip.csv` | 147 |
| `sentinel/CTI_Dominio.csv` | 395 |
| `sentinel/CTI_Url.csv` | 295 |
| `sentinel/CTI_Hash.csv` | 615 |
| `elastic/cti_ip.ndjson` | 147 |
| `elastic/cti_dominio.ndjson` | 395 |
| `elastic/cti_url.ndjson` | 295 |
| `elastic/cti_hash.ndjson` | 615 |

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
