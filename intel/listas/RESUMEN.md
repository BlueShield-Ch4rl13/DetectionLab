# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-18 11:11 UTC  
**Listas generadas:** 2026-11-18T14:53:34Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 335 | Caza programada, no alerta directa |
| Dominio | 436 | Caza programada, no alerta directa |
| URL | 148 | Caza programada, no alerta directa |
| Hash | 412 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (52 de 1383)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 52 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown malware | 224 |
| IClickFix | 146 |
| Mirai | 137 |
| ClearFake | 125 |
| malware_download | 98 |
| StrelaStealer | 55 |
| Vidar | 51 |
| Unknown Loader | 33 |
| VShell | 27 |
| stealler | 27 |
| Agent Tesla | 27 |
| Aisuru | 21 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 335 |
| `wazuh/cti_dominio` | 436 |
| `wazuh/cti_url` | 148 |
| `wazuh/cti_hash` | 412 |
| `wazuh/cti_cve_kev` | 15 |
| `splunk/cti_ip.csv` | 335 |
| `splunk/cti_dominio.csv` | 436 |
| `splunk/cti_url.csv` | 148 |
| `splunk/cti_hash.csv` | 412 |
| `splunk/cti_cve_kev.csv` | 15 |
| `sentinel/CTI_Ip.csv` | 335 |
| `sentinel/CTI_Dominio.csv` | 436 |
| `sentinel/CTI_Url.csv` | 148 |
| `sentinel/CTI_Hash.csv` | 412 |
| `elastic/cti_ip.ndjson` | 335 |
| `elastic/cti_dominio.ndjson` | 436 |
| `elastic/cti_url.ndjson` | 148 |
| `elastic/cti_hash.ndjson` | 412 |

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
