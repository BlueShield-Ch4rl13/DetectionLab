# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-25 04:11 UTC  
**Listas generadas:** 2026-11-25T16:35:32Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 718 | Caza programada, no alerta directa |
| Dominio | 207 | Caza programada, no alerta directa |
| URL | 164 | Caza programada, no alerta directa |
| Hash | 674 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 16 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (155 de 1918)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 155 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown malware | 872 |
| ZStealer | 261 |
| malware_download | 100 |
| ClearFake | 63 |
| Vidar | 47 |
| Unknown Loader | 45 |
| IClickFix | 32 |
| Unknown Stealer | 30 |
| Mirai | 27 |
| Python  Re-Skinned  Keeping the Steal: Braodo's Latest Python Loader and Obfuscation | 25 |
| SNOWLIGHT | 22 |
| Remcos | 18 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 718 |
| `wazuh/cti_dominio` | 207 |
| `wazuh/cti_url` | 164 |
| `wazuh/cti_hash` | 674 |
| `wazuh/cti_cve_kev` | 16 |
| `splunk/cti_ip.csv` | 718 |
| `splunk/cti_dominio.csv` | 207 |
| `splunk/cti_url.csv` | 164 |
| `splunk/cti_hash.csv` | 674 |
| `splunk/cti_cve_kev.csv` | 16 |
| `sentinel/CTI_Ip.csv` | 718 |
| `sentinel/CTI_Dominio.csv` | 207 |
| `sentinel/CTI_Url.csv` | 164 |
| `sentinel/CTI_Hash.csv` | 674 |
| `elastic/cti_ip.ndjson` | 718 |
| `elastic/cti_dominio.ndjson` | 207 |
| `elastic/cti_url.ndjson` | 164 |
| `elastic/cti_hash.ndjson` | 674 |

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
