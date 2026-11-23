# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-23 11:51 UTC  
**Listas generadas:** 2026-11-23T16:59:00Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 274 | Caza programada, no alerta directa |
| Dominio | 1107 | Caza programada, no alerta directa |
| URL | 126 | Caza programada, no alerta directa |
| Hash | 839 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 21 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (97 de 2443)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 97 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown Webinject | 876 |
| Unknown malware | 479 |
| Mirai | 158 |
| Raven Stealer | 102 |
| malware_download | 100 |
| Vidar | 87 |
| Unknown Loader | 83 |
| XWorm | 55 |
| SNOWLIGHT | 41 |
| ClearFake | 41 |
| NjRAT | 38 |
| Infostealer riding the AI Train | 37 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 274 |
| `wazuh/cti_dominio` | 1107 |
| `wazuh/cti_url` | 126 |
| `wazuh/cti_hash` | 839 |
| `wazuh/cti_cve_kev` | 21 |
| `splunk/cti_ip.csv` | 274 |
| `splunk/cti_dominio.csv` | 1107 |
| `splunk/cti_url.csv` | 126 |
| `splunk/cti_hash.csv` | 839 |
| `splunk/cti_cve_kev.csv` | 21 |
| `sentinel/CTI_Ip.csv` | 274 |
| `sentinel/CTI_Dominio.csv` | 1107 |
| `sentinel/CTI_Url.csv` | 126 |
| `sentinel/CTI_Hash.csv` | 839 |
| `elastic/cti_ip.ndjson` | 274 |
| `elastic/cti_dominio.ndjson` | 1107 |
| `elastic/cti_url.ndjson` | 126 |
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
