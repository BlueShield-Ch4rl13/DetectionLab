# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-05 10:24 UTC  
**Listas generadas:** 2026-11-05T13:47:38Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 170 | Caza programada, no alerta directa |
| Dominio | 351 | Caza programada, no alerta directa |
| URL | 248 | Caza programada, no alerta directa |
| Hash | 889 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 14 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (198 de 1856)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 198 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown Loader | 356 |
| AMOS | 302 |
| Unknown malware | 176 |
| malware_download | 100 |
| SalatStealer | 79 |
| Astaroth | 66 |
| Vidar | 57 |
| VShell | 38 |
| Mirai | 36 |
| ACR Stealer | 31 |
| ClearFake | 31 |
| php.shin_webshell | 30 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 170 |
| `wazuh/cti_dominio` | 351 |
| `wazuh/cti_url` | 248 |
| `wazuh/cti_hash` | 889 |
| `wazuh/cti_cve_kev` | 14 |
| `splunk/cti_ip.csv` | 170 |
| `splunk/cti_dominio.csv` | 351 |
| `splunk/cti_url.csv` | 248 |
| `splunk/cti_hash.csv` | 889 |
| `splunk/cti_cve_kev.csv` | 14 |
| `sentinel/CTI_Ip.csv` | 170 |
| `sentinel/CTI_Dominio.csv` | 351 |
| `sentinel/CTI_Url.csv` | 248 |
| `sentinel/CTI_Hash.csv` | 889 |
| `elastic/cti_ip.ndjson` | 170 |
| `elastic/cti_dominio.ndjson` | 351 |
| `elastic/cti_url.ndjson` | 248 |
| `elastic/cti_hash.ndjson` | 889 |

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
