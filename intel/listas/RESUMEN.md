# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-09 10:58 UTC  
**Listas generadas:** 2026-11-09T14:49:59Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 107 | Caza programada, no alerta directa |
| Dominio | 255 | Caza programada, no alerta directa |
| URL | 205 | Caza programada, no alerta directa |
| Hash | 869 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (56 de 1492)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 56 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Mirai | 274 |
| SNOWLIGHT | 106 |
| ClearFake | 102 |
| malware_download | 99 |
| Raven Stealer | 85 |
| Unknown malware | 75 |
| Vidar | 61 |
| IClickFix | 51 |
| VShell | 47 |
| Unknown Loader | 43 |
| Prometei | 42 |
| php.shin_webshell | 37 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 107 |
| `wazuh/cti_dominio` | 255 |
| `wazuh/cti_url` | 205 |
| `wazuh/cti_hash` | 869 |
| `wazuh/cti_cve_kev` | 13 |
| `splunk/cti_ip.csv` | 107 |
| `splunk/cti_dominio.csv` | 255 |
| `splunk/cti_url.csv` | 205 |
| `splunk/cti_hash.csv` | 869 |
| `splunk/cti_cve_kev.csv` | 13 |
| `sentinel/CTI_Ip.csv` | 107 |
| `sentinel/CTI_Dominio.csv` | 255 |
| `sentinel/CTI_Url.csv` | 205 |
| `sentinel/CTI_Hash.csv` | 869 |
| `elastic/cti_ip.ndjson` | 107 |
| `elastic/cti_dominio.ndjson` | 255 |
| `elastic/cti_url.ndjson` | 205 |
| `elastic/cti_hash.ndjson` | 869 |

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
