# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-22 04:20 UTC  
**Listas generadas:** 2026-10-22T10:55:57Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 243 | Caza programada, no alerta directa |
| Dominio | 1151 | Caza programada, no alerta directa |
| URL | 564 | Caza programada, no alerta directa |
| Hash | 143 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 20 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (613 de 2737)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 577 |
| nivel bajo | 36 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| IClickFix | 591 |
| Vidar | 351 |
| Unknown Loader | 336 |
| Midnight Mimosa Malware Campaign Exploits Android Firmware Supply Chain | 120 |
| VShell | 105 |
| ClearFake | 100 |
| malware_download | 98 |
| StrelaStealer | 73 |
| Unknown malware | 38 |
| php.shin_webshell | 36 |
| Remus | 32 |
| Remcos | 25 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 243 |
| `wazuh/cti_dominio` | 1151 |
| `wazuh/cti_url` | 564 |
| `wazuh/cti_hash` | 143 |
| `wazuh/cti_cve_kev` | 20 |
| `splunk/cti_ip.csv` | 243 |
| `splunk/cti_dominio.csv` | 1151 |
| `splunk/cti_url.csv` | 564 |
| `splunk/cti_hash.csv` | 143 |
| `splunk/cti_cve_kev.csv` | 20 |
| `sentinel/CTI_Ip.csv` | 243 |
| `sentinel/CTI_Dominio.csv` | 1151 |
| `sentinel/CTI_Url.csv` | 564 |
| `sentinel/CTI_Hash.csv` | 143 |
| `elastic/cti_ip.ndjson` | 243 |
| `elastic/cti_dominio.ndjson` | 1151 |
| `elastic/cti_url.ndjson` | 564 |
| `elastic/cti_hash.ndjson` | 143 |

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
