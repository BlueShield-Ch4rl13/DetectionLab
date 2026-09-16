# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-09-16 04:28 UTC  
**Listas generadas:** 2026-09-16T10:35:10Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 137 | Caza programada, no alerta directa |
| Dominio | 1260 | Caza programada, no alerta directa |
| URL | 185 | Caza programada, no alerta directa |
| Hash | 54 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 23 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (1122 de 2837)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 1037 |
| nivel bajo | 85 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown Loader | 1007 |
| malware_download | 99 |
| IClickFix | 77 |
| ClearFake | 63 |
| Unknown malware | 54 |
| Remcos | 45 |
| php.shin_webshell | 25 |
| Vidar | 22 |
| Remus | 21 |
| Cobalt Strike | 20 |
| XWorm | 17 |
| New Armored Likho tools target Telegram and eavesdropping | 17 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 137 |
| `wazuh/cti_dominio` | 1260 |
| `wazuh/cti_url` | 185 |
| `wazuh/cti_hash` | 54 |
| `wazuh/cti_cve_kev` | 23 |
| `splunk/cti_ip.csv` | 137 |
| `splunk/cti_dominio.csv` | 1260 |
| `splunk/cti_url.csv` | 185 |
| `splunk/cti_hash.csv` | 54 |
| `splunk/cti_cve_kev.csv` | 23 |
| `sentinel/CTI_Ip.csv` | 137 |
| `sentinel/CTI_Dominio.csv` | 1260 |
| `sentinel/CTI_Url.csv` | 185 |
| `sentinel/CTI_Hash.csv` | 54 |
| `elastic/cti_ip.ndjson` | 137 |
| `elastic/cti_dominio.ndjson` | 1260 |
| `elastic/cti_url.ndjson` | 185 |
| `elastic/cti_hash.ndjson` | 54 |

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
