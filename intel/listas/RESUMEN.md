# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-21 04:20 UTC  
**Listas generadas:** 2026-10-21T10:56:37Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 128 | Caza programada, no alerta directa |
| Dominio | 279 | Caza programada, no alerta directa |
| URL | 727 | Caza programada, no alerta directa |
| Hash | 79 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (1011 de 2244)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 956 |
| nivel bajo | 55 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Vidar | 382 |
| Remus | 175 |
| malware_download | 100 |
| Unknown malware | 99 |
| IClickFix | 79 |
| VShell | 46 |
| php.shin_webshell | 40 |
| ClearFake | 36 |
| Swallowtail: Russian Espionage Group Targets Defense Firms in Two NATO Countries | 34 |
| Unknown Loader | 33 |
| MacSync | 29 |
| Remcos | 19 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 128 |
| `wazuh/cti_dominio` | 279 |
| `wazuh/cti_url` | 727 |
| `wazuh/cti_hash` | 79 |
| `wazuh/cti_cve_kev` | 20 |
| `splunk/cti_ip.csv` | 128 |
| `splunk/cti_dominio.csv` | 279 |
| `splunk/cti_url.csv` | 727 |
| `splunk/cti_hash.csv` | 79 |
| `splunk/cti_cve_kev.csv` | 20 |
| `sentinel/CTI_Ip.csv` | 128 |
| `sentinel/CTI_Dominio.csv` | 279 |
| `sentinel/CTI_Url.csv` | 727 |
| `sentinel/CTI_Hash.csv` | 79 |
| `elastic/cti_ip.ndjson` | 128 |
| `elastic/cti_dominio.ndjson` | 279 |
| `elastic/cti_url.ndjson` | 727 |
| `elastic/cti_hash.ndjson` | 79 |

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
