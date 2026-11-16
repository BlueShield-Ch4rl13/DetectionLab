# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-16 10:43 UTC  
**Listas generadas:** 2026-11-16T14:25:51Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 127 | Caza programada, no alerta directa |
| Dominio | 835 | Caza programada, no alerta directa |
| URL | 268 | Caza programada, no alerta directa |
| Hash | 521 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (93 de 1844)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 93 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown Loader | 514 |
| Unknown malware | 185 |
| IClickFix | 145 |
| Mirai | 134 |
| ClearFake | 118 |
| malware_download | 98 |
| Raven Stealer | 73 |
| BREAK THE SILENCE: Tracking Silent Lynx Through Exposed Infrastructure | 73 |
| Vidar | 63 |
| SalatStealer | 34 |
| Unknown Stealer | 29 |
| ValleyRAT | 21 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 127 |
| `wazuh/cti_dominio` | 835 |
| `wazuh/cti_url` | 268 |
| `wazuh/cti_hash` | 521 |
| `wazuh/cti_cve_kev` | 15 |
| `splunk/cti_ip.csv` | 127 |
| `splunk/cti_dominio.csv` | 835 |
| `splunk/cti_url.csv` | 268 |
| `splunk/cti_hash.csv` | 521 |
| `splunk/cti_cve_kev.csv` | 15 |
| `sentinel/CTI_Ip.csv` | 127 |
| `sentinel/CTI_Dominio.csv` | 835 |
| `sentinel/CTI_Url.csv` | 268 |
| `sentinel/CTI_Hash.csv` | 521 |
| `elastic/cti_ip.ndjson` | 127 |
| `elastic/cti_dominio.ndjson` | 835 |
| `elastic/cti_url.ndjson` | 268 |
| `elastic/cti_hash.ndjson` | 521 |

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
