# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-10 05:46 UTC  
**Listas generadas:** 2026-11-10T14:02:13Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 112 | Caza programada, no alerta directa |
| Dominio | 232 | Caza programada, no alerta directa |
| URL | 206 | Caza programada, no alerta directa |
| Hash | 622 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (53 de 1225)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 53 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Mirai | 255 |
| malware_download | 100 |
| Unknown Loader | 85 |
| SNOWLIGHT | 79 |
| Unknown malware | 62 |
| ClearFake | 58 |
| Vidar | 53 |
| IClickFix | 52 |
| SalatStealer | 44 |
| Prometei | 42 |
| php.shin_webshell | 33 |
| XWorm | 29 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 112 |
| `wazuh/cti_dominio` | 232 |
| `wazuh/cti_url` | 206 |
| `wazuh/cti_hash` | 622 |
| `wazuh/cti_cve_kev` | 15 |
| `splunk/cti_ip.csv` | 112 |
| `splunk/cti_dominio.csv` | 232 |
| `splunk/cti_url.csv` | 206 |
| `splunk/cti_hash.csv` | 622 |
| `splunk/cti_cve_kev.csv` | 15 |
| `sentinel/CTI_Ip.csv` | 112 |
| `sentinel/CTI_Dominio.csv` | 232 |
| `sentinel/CTI_Url.csv` | 206 |
| `sentinel/CTI_Hash.csv` | 622 |
| `elastic/cti_ip.ndjson` | 112 |
| `elastic/cti_dominio.ndjson` | 232 |
| `elastic/cti_url.ndjson` | 206 |
| `elastic/cti_hash.ndjson` | 622 |

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
