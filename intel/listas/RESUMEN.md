# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-07 09:42 UTC  
**Listas generadas:** 2026-11-07T12:12:39Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 157 | Caza programada, no alerta directa |
| Dominio | 130 | Caza programada, no alerta directa |
| URL | 162 | Caza programada, no alerta directa |
| Hash | 1167 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (71 de 1687)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 71 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown Loader | 344 |
| AMOS | 310 |
| ZStealer | 153 |
| Mirai | 132 |
| malware_download | 100 |
| VShell | 53 |
| Vidar | 49 |
| ClearFake | 40 |
| Armorsteal Unpacked: Breaking Down a Python Malware Kit That Steals Data and Mines Crypto | 31 |
| Sliver | 28 |
| Unknown malware | 27 |
| WARDENStealer | 26 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 157 |
| `wazuh/cti_dominio` | 130 |
| `wazuh/cti_url` | 162 |
| `wazuh/cti_hash` | 1167 |
| `wazuh/cti_cve_kev` | 13 |
| `splunk/cti_ip.csv` | 157 |
| `splunk/cti_dominio.csv` | 130 |
| `splunk/cti_url.csv` | 162 |
| `splunk/cti_hash.csv` | 1167 |
| `splunk/cti_cve_kev.csv` | 13 |
| `sentinel/CTI_Ip.csv` | 157 |
| `sentinel/CTI_Dominio.csv` | 130 |
| `sentinel/CTI_Url.csv` | 162 |
| `sentinel/CTI_Hash.csv` | 1167 |
| `elastic/cti_ip.ndjson` | 157 |
| `elastic/cti_dominio.ndjson` | 130 |
| `elastic/cti_url.ndjson` | 162 |
| `elastic/cti_hash.ndjson` | 1167 |

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
