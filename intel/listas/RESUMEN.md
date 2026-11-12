# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-12 05:32 UTC  
**Listas generadas:** 2026-11-12T14:24:04Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 209 | Caza programada, no alerta directa |
| Dominio | 696 | Caza programada, no alerta directa |
| URL | 197 | Caza programada, no alerta directa |
| Hash | 839 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (47 de 1988)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 47 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown Loader | 322 |
| Unknown malware | 303 |
| IClickFix | 285 |
| SalatStealer | 167 |
| malware_download | 100 |
| ClearFake | 89 |
| Mirai | 83 |
| Not All That Glitters Is Gold: Tracking CopperDragon's Sparrow Framework Around the Globe | 82 |
| StrelaStealer | 77 |
| Vidar | 44 |
| Unknown Stealer | 41 |
| Sliver | 26 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 209 |
| `wazuh/cti_dominio` | 696 |
| `wazuh/cti_url` | 197 |
| `wazuh/cti_hash` | 839 |
| `wazuh/cti_cve_kev` | 17 |
| `splunk/cti_ip.csv` | 209 |
| `splunk/cti_dominio.csv` | 696 |
| `splunk/cti_url.csv` | 197 |
| `splunk/cti_hash.csv` | 839 |
| `splunk/cti_cve_kev.csv` | 17 |
| `sentinel/CTI_Ip.csv` | 209 |
| `sentinel/CTI_Dominio.csv` | 696 |
| `sentinel/CTI_Url.csv` | 197 |
| `sentinel/CTI_Hash.csv` | 839 |
| `elastic/cti_ip.ndjson` | 209 |
| `elastic/cti_dominio.ndjson` | 696 |
| `elastic/cti_url.ndjson` | 197 |
| `elastic/cti_hash.ndjson` | 839 |

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
