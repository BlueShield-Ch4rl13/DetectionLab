# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-27 03:38 UTC  
**Listas generadas:** 2026-11-27T15:55:12Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 750 | Caza programada, no alerta directa |
| Dominio | 445 | Caza programada, no alerta directa |
| URL | 189 | Caza programada, no alerta directa |
| Hash | 520 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 26 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (98 de 2002)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 98 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown malware | 837 |
| Unknown Loader | 200 |
| malware_download | 99 |
| ClearFake | 78 |
| Vidar | 54 |
| Mirai | 52 |
| Raven Stealer | 40 |
| Formbook | 39 |
| Agent Tesla | 39 |
| Unknown RAT | 29 |
| ValleyRAT | 28 |
| IClickFix | 25 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 750 |
| `wazuh/cti_dominio` | 445 |
| `wazuh/cti_url` | 189 |
| `wazuh/cti_hash` | 520 |
| `wazuh/cti_cve_kev` | 26 |
| `splunk/cti_ip.csv` | 750 |
| `splunk/cti_dominio.csv` | 445 |
| `splunk/cti_url.csv` | 189 |
| `splunk/cti_hash.csv` | 520 |
| `splunk/cti_cve_kev.csv` | 26 |
| `sentinel/CTI_Ip.csv` | 750 |
| `sentinel/CTI_Dominio.csv` | 445 |
| `sentinel/CTI_Url.csv` | 189 |
| `sentinel/CTI_Hash.csv` | 520 |
| `elastic/cti_ip.ndjson` | 750 |
| `elastic/cti_dominio.ndjson` | 445 |
| `elastic/cti_url.ndjson` | 189 |
| `elastic/cti_hash.ndjson` | 520 |

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
