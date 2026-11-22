# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-22 10:50 UTC  
**Listas generadas:** 2026-11-22T13:51:50Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 0 | Caza programada, no alerta directa |
| Dominio | 0 | Caza programada, no alerta directa |
| URL | 100 | Caza programada, no alerta directa |
| Hash | 125 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (70 de 295)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 70 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| malware_download | 100 |
| Inside SiriusQT: A Seriously Skilled RAT | 80 |
| SEO Poisoning Campaign Delivers New Armorsteal Malware | 21 |
| MythicRatatoskr: An Yggdrasil-enabled backdoor deployed in a UAC-0099-Sandworm collaboration | 18 |
| StealC Is Back  and This Time It's a RAT | 5 |
| M365 Token Spray and Replay Campaign Compromises Business Email Accounts | 1 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 0 |
| `wazuh/cti_dominio` | 0 |
| `wazuh/cti_url` | 100 |
| `wazuh/cti_hash` | 125 |
| `wazuh/cti_cve_kev` | 21 |
| `splunk/cti_ip.csv` | 0 |
| `splunk/cti_dominio.csv` | 0 |
| `splunk/cti_url.csv` | 100 |
| `splunk/cti_hash.csv` | 125 |
| `splunk/cti_cve_kev.csv` | 21 |
| `sentinel/CTI_Ip.csv` | 0 |
| `sentinel/CTI_Dominio.csv` | 0 |
| `sentinel/CTI_Url.csv` | 100 |
| `sentinel/CTI_Hash.csv` | 125 |
| `elastic/cti_ip.ndjson` | 0 |
| `elastic/cti_dominio.ndjson` | 0 |
| `elastic/cti_url.ndjson` | 100 |
| `elastic/cti_hash.ndjson` | 125 |

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
