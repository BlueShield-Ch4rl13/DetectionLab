# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-08 04:06 UTC  
**Listas generadas:** 2026-11-08T12:32:39Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 136 | Caza programada, no alerta directa |
| Dominio | 370 | Caza programada, no alerta directa |
| URL | 320 | Caza programada, no alerta directa |
| Hash | 824 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (52 de 1702)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 52 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| AMOS | 270 |
| Unknown Loader | 180 |
| WARDENStealer | 157 |
| ClearFake | 121 |
| Mirai | 116 |
| malware_download | 99 |
| Vidar | 76 |
| VShell | 69 |
| Unknown malware | 65 |
| RN Stealer | 40 |
| SNOWLIGHT | 38 |
| Raven Stealer | 37 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 136 |
| `wazuh/cti_dominio` | 370 |
| `wazuh/cti_url` | 320 |
| `wazuh/cti_hash` | 824 |
| `wazuh/cti_cve_kev` | 13 |
| `splunk/cti_ip.csv` | 136 |
| `splunk/cti_dominio.csv` | 370 |
| `splunk/cti_url.csv` | 320 |
| `splunk/cti_hash.csv` | 824 |
| `splunk/cti_cve_kev.csv` | 13 |
| `sentinel/CTI_Ip.csv` | 136 |
| `sentinel/CTI_Dominio.csv` | 370 |
| `sentinel/CTI_Url.csv` | 320 |
| `sentinel/CTI_Hash.csv` | 824 |
| `elastic/cti_ip.ndjson` | 136 |
| `elastic/cti_dominio.ndjson` | 370 |
| `elastic/cti_url.ndjson` | 320 |
| `elastic/cti_hash.ndjson` | 824 |

## Como se instala cada una

Ver `deploy/<siem>/INSTALAR.md`. En resumen:

```bash
# Wazuh: copiar SIN la extension, declarar en ossec.conf y reiniciar
for f in intel/listas/wazuh/*.cdb; do
  sudo install -o root -g wazuh -m 660 "$f" "/var/ossec/etc/lists/$(basename "$f" .cdb)"
done
sudo systemctl restart wazuh-manager

# Splunk: como lookups de la app
cp intel/listas/splunk/*.csv $SPLUNK_HOME/etc/apps/TA-detection-lab/lookups/

# Sentinel: Watchlists > New > importar el CSV, alias sin el prefijo CTI_
# Elastic: bulk al indice de indicadores
curl -XPOST 'localhost:9200/logs-ti_newscti-default/_bulk' \
     -H 'Content-Type: application/x-ndjson' \
     --data-binary @intel/listas/elastic/cti_ip.ndjson
```
