# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-17 06:13 UTC  
**Listas generadas:** 2026-11-17T15:18:10Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 413 | Caza programada, no alerta directa |
| Dominio | 686 | Caza programada, no alerta directa |
| URL | 213 | Caza programada, no alerta directa |
| Hash | 505 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 15 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (79 de 1896)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 79 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown malware | 405 |
| ClearFake | 234 |
| IClickFix | 188 |
| Unknown Loader | 161 |
| malware_download | 100 |
| ZStealer | 87 |
| Stealc | 55 |
| Vidar | 54 |
| Mirai | 53 |
| SCKit abuses ScreenConnect to deploy remote access and target technician sessions | 44 |
| WardenStealer Malware: Turning AI Access into an Underground Commodity | 36 |
| SNOWLIGHT | 35 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 413 |
| `wazuh/cti_dominio` | 686 |
| `wazuh/cti_url` | 213 |
| `wazuh/cti_hash` | 505 |
| `wazuh/cti_cve_kev` | 15 |
| `splunk/cti_ip.csv` | 413 |
| `splunk/cti_dominio.csv` | 686 |
| `splunk/cti_url.csv` | 213 |
| `splunk/cti_hash.csv` | 505 |
| `splunk/cti_cve_kev.csv` | 15 |
| `sentinel/CTI_Ip.csv` | 413 |
| `sentinel/CTI_Dominio.csv` | 686 |
| `sentinel/CTI_Url.csv` | 213 |
| `sentinel/CTI_Hash.csv` | 505 |
| `elastic/cti_ip.ndjson` | 413 |
| `elastic/cti_dominio.ndjson` | 686 |
| `elastic/cti_url.ndjson` | 213 |
| `elastic/cti_hash.ndjson` | 505 |

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
