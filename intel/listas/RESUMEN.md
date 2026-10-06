# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-06 06:00 UTC  
**Listas generadas:** 2026-10-06T12:31:45Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 99 | Caza programada, no alerta directa |
| Dominio | 586 | Caza programada, no alerta directa |
| URL | 202 | Caza programada, no alerta directa |
| Hash | 144 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (1245 de 2307)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 1199 |
| nivel bajo | 46 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| ClearFake | 521 |
| malware_download | 100 |
| Anatomy of BraZetsu: How Cybercriminals Supply the Underground Ecosystem | 48 |
| Attackers Abuse ChatGPT Custom GPTs to Deliver RAT via ClickFix | 45 |
| Unknown malware | 40 |
| SMTP is the key: BPFDoor and AVERAT hitting the network edge | 30 |
| Vidar | 26 |
| php.shin_webshell | 25 |
| Unknown RAT | 22 |
| IClickFix | 22 |
| Remcos | 14 |
| Aisuru | 13 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 99 |
| `wazuh/cti_dominio` | 586 |
| `wazuh/cti_url` | 202 |
| `wazuh/cti_hash` | 144 |
| `wazuh/cti_cve_kev` | 17 |
| `splunk/cti_ip.csv` | 99 |
| `splunk/cti_dominio.csv` | 586 |
| `splunk/cti_url.csv` | 202 |
| `splunk/cti_hash.csv` | 144 |
| `splunk/cti_cve_kev.csv` | 17 |
| `sentinel/CTI_Ip.csv` | 99 |
| `sentinel/CTI_Dominio.csv` | 586 |
| `sentinel/CTI_Url.csv` | 202 |
| `sentinel/CTI_Hash.csv` | 144 |
| `elastic/cti_ip.ndjson` | 99 |
| `elastic/cti_dominio.ndjson` | 586 |
| `elastic/cti_url.ndjson` | 202 |
| `elastic/cti_hash.ndjson` | 144 |

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
