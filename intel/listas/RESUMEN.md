# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-13 04:45 UTC  
**Listas generadas:** 2026-11-13T13:43:26Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 134 | Caza programada, no alerta directa |
| Dominio | 587 | Caza programada, no alerta directa |
| URL | 252 | Caza programada, no alerta directa |
| Hash | 856 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (55 de 1884)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 55 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown Loader | 360 |
| Unknown malware | 355 |
| ClearFake | 160 |
| Mirai | 110 |
| malware_download | 100 |
| IClickFix | 72 |
| NjRAT | 57 |
| KAgent | 57 |
| How AI Revived a Stalled Attack on a U.S. Retailer | 50 |
| Remcos | 41 |
| Unknown Stealer | 41 |
| Vidar | 35 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 134 |
| `wazuh/cti_dominio` | 587 |
| `wazuh/cti_url` | 252 |
| `wazuh/cti_hash` | 856 |
| `wazuh/cti_cve_kev` | 15 |
| `splunk/cti_ip.csv` | 134 |
| `splunk/cti_dominio.csv` | 587 |
| `splunk/cti_url.csv` | 252 |
| `splunk/cti_hash.csv` | 856 |
| `splunk/cti_cve_kev.csv` | 15 |
| `sentinel/CTI_Ip.csv` | 134 |
| `sentinel/CTI_Dominio.csv` | 587 |
| `sentinel/CTI_Url.csv` | 252 |
| `sentinel/CTI_Hash.csv` | 856 |
| `elastic/cti_ip.ndjson` | 134 |
| `elastic/cti_dominio.ndjson` | 587 |
| `elastic/cti_url.ndjson` | 252 |
| `elastic/cti_hash.ndjson` | 856 |

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
