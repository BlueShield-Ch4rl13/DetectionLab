# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-03 04:56 UTC  
**Listas generadas:** 2026-10-03T10:53:54Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 148 | Caza programada, no alerta directa |
| Dominio | 444 | Caza programada, no alerta directa |
| URL | 265 | Caza programada, no alerta directa |
| Hash | 123 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (1678 de 2710)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 1607 |
| nivel bajo | 71 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| IClickFix | 324 |
| malware_download | 100 |
| Gaming the system: how a Chinese-speaking actor turned Brazilian government sites into an SEO weapon | 89 |
| ClearFake | 86 |
| Unknown malware | 58 |
| Remus | 36 |
| Vidar | 33 |
| Unknown Loader | 27 |
| php.shin_webshell | 21 |
| Warlock Ransomware Attackers Hit Water and Telecom Operators | 16 |
| AdaptixC2 | 15 |
| Potassium | 15 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 148 |
| `wazuh/cti_dominio` | 444 |
| `wazuh/cti_url` | 265 |
| `wazuh/cti_hash` | 123 |
| `wazuh/cti_cve_kev` | 17 |
| `splunk/cti_ip.csv` | 148 |
| `splunk/cti_dominio.csv` | 444 |
| `splunk/cti_url.csv` | 265 |
| `splunk/cti_hash.csv` | 123 |
| `splunk/cti_cve_kev.csv` | 17 |
| `sentinel/CTI_Ip.csv` | 148 |
| `sentinel/CTI_Dominio.csv` | 444 |
| `sentinel/CTI_Url.csv` | 265 |
| `sentinel/CTI_Hash.csv` | 123 |
| `elastic/cti_ip.ndjson` | 148 |
| `elastic/cti_dominio.ndjson` | 444 |
| `elastic/cti_url.ndjson` | 265 |
| `elastic/cti_hash.ndjson` | 123 |

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
