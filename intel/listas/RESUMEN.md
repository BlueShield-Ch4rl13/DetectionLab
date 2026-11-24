# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-24 08:07 UTC  
**Listas generadas:** 2026-11-24T16:47:22Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 4594 | Caza programada, no alerta directa |
| Dominio | 253 | Caza programada, no alerta directa |
| URL | 165 | Caza programada, no alerta directa |
| Hash | 635 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 19 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (188 de 5835)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 188 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown malware | 4791 |
| Mirai | 105 |
| malware_download | 99 |
| magecart | 92 |
| Unknown Loader | 73 |
| Vidar | 60 |
| ClearFake | 41 |
| Raven Stealer | 38 |
| VShell | 30 |
| IClickFix | 27 |
| Agent Tesla | 24 |
| SNOWLIGHT | 18 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 4594 |
| `wazuh/cti_dominio` | 253 |
| `wazuh/cti_url` | 165 |
| `wazuh/cti_hash` | 635 |
| `wazuh/cti_cve_kev` | 19 |
| `splunk/cti_ip.csv` | 4594 |
| `splunk/cti_dominio.csv` | 253 |
| `splunk/cti_url.csv` | 165 |
| `splunk/cti_hash.csv` | 635 |
| `splunk/cti_cve_kev.csv` | 19 |
| `sentinel/CTI_Ip.csv` | 4594 |
| `sentinel/CTI_Dominio.csv` | 253 |
| `sentinel/CTI_Url.csv` | 165 |
| `sentinel/CTI_Hash.csv` | 635 |
| `elastic/cti_ip.ndjson` | 4594 |
| `elastic/cti_dominio.ndjson` | 253 |
| `elastic/cti_url.ndjson` | 165 |
| `elastic/cti_hash.ndjson` | 635 |

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
