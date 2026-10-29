# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-29 05:25 UTC  
**Listas generadas:** 2026-10-29T12:03:05Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 201 | Caza programada, no alerta directa |
| Dominio | 538 | Caza programada, no alerta directa |
| URL | 671 | Caza programada, no alerta directa |
| Hash | 941 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (0 de 2351)

| Motivo | Descartados |
|---|---:|

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| ClearFake | 428 |
| Vidar | 329 |
| AMOS | 286 |
| Mirai | 266 |
| Unknown malware | 266 |
| SalatStealer | 190 |
| malware_download | 100 |
| Stealc | 58 |
| Cobalt Strike | 43 |
| Unknown Loader | 43 |
| StrelaStealer | 30 |
| VShell | 25 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 201 |
| `wazuh/cti_dominio` | 538 |
| `wazuh/cti_url` | 671 |
| `wazuh/cti_hash` | 941 |
| `wazuh/cti_cve_kev` | 17 |
| `splunk/cti_ip.csv` | 201 |
| `splunk/cti_dominio.csv` | 538 |
| `splunk/cti_url.csv` | 671 |
| `splunk/cti_hash.csv` | 941 |
| `splunk/cti_cve_kev.csv` | 17 |
| `sentinel/CTI_Ip.csv` | 201 |
| `sentinel/CTI_Dominio.csv` | 538 |
| `sentinel/CTI_Url.csv` | 671 |
| `sentinel/CTI_Hash.csv` | 941 |
| `elastic/cti_ip.ndjson` | 201 |
| `elastic/cti_dominio.ndjson` | 538 |
| `elastic/cti_url.ndjson` | 671 |
| `elastic/cti_hash.ndjson` | 941 |

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
