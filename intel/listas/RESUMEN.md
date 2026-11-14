# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-14 04:42 UTC  
**Listas generadas:** 2026-11-14T12:47:25Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 128 | Caza programada, no alerta directa |
| Dominio | 818 | Caza programada, no alerta directa |
| URL | 234 | Caza programada, no alerta directa |
| Hash | 539 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (24 de 1743)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 24 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown Loader | 769 |
| Unknown malware | 212 |
| malware_download | 100 |
| Mirai | 60 |
| ClingSTUN Turns Vulnerable Edge Devices Into Attacker Infrastructure | 57 |
| RN Stealer | 43 |
| Vidar | 37 |
| ZStealer | 24 |
| WARDENStealer | 22 |
| RevStealer | 22 |
| php.shin_webshell | 21 |
| ClearFake | 20 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 128 |
| `wazuh/cti_dominio` | 818 |
| `wazuh/cti_url` | 234 |
| `wazuh/cti_hash` | 539 |
| `wazuh/cti_cve_kev` | 15 |
| `splunk/cti_ip.csv` | 128 |
| `splunk/cti_dominio.csv` | 818 |
| `splunk/cti_url.csv` | 234 |
| `splunk/cti_hash.csv` | 539 |
| `splunk/cti_cve_kev.csv` | 15 |
| `sentinel/CTI_Ip.csv` | 128 |
| `sentinel/CTI_Dominio.csv` | 818 |
| `sentinel/CTI_Url.csv` | 234 |
| `sentinel/CTI_Hash.csv` | 539 |
| `elastic/cti_ip.ndjson` | 128 |
| `elastic/cti_dominio.ndjson` | 818 |
| `elastic/cti_url.ndjson` | 234 |
| `elastic/cti_hash.ndjson` | 539 |

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
