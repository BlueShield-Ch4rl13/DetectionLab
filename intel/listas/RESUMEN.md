# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-20 11:02 UTC  
**Listas generadas:** 2026-11-20T14:41:48Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 427 | Caza programada, no alerta directa |
| Dominio | 166 | Caza programada, no alerta directa |
| URL | 259 | Caza programada, no alerta directa |
| Hash | 477 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 18 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (57 de 1386)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 57 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown malware | 423 |
| Mirai | 165 |
| malware_download | 100 |
| ZStealer | 96 |
| Vidar | 48 |
| ClearFake | 45 |
| VShell | 32 |
| Sliver | 32 |
| Cobalt Strike | 24 |
| AsyncRAT | 21 |
| The Gentlemen: A closer look at a not-so-gentle ransomware-as-a-service operation | 21 |
| Gentlemen | 19 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 427 |
| `wazuh/cti_dominio` | 166 |
| `wazuh/cti_url` | 259 |
| `wazuh/cti_hash` | 477 |
| `wazuh/cti_cve_kev` | 18 |
| `splunk/cti_ip.csv` | 427 |
| `splunk/cti_dominio.csv` | 166 |
| `splunk/cti_url.csv` | 259 |
| `splunk/cti_hash.csv` | 477 |
| `splunk/cti_cve_kev.csv` | 18 |
| `sentinel/CTI_Ip.csv` | 427 |
| `sentinel/CTI_Dominio.csv` | 166 |
| `sentinel/CTI_Url.csv` | 259 |
| `sentinel/CTI_Hash.csv` | 477 |
| `elastic/cti_ip.ndjson` | 427 |
| `elastic/cti_dominio.ndjson` | 166 |
| `elastic/cti_url.ndjson` | 259 |
| `elastic/cti_hash.ndjson` | 477 |

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
