# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-26 11:59 UTC  
**Listas generadas:** 2026-11-26T16:07:42Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 740 | Caza programada, no alerta directa |
| Dominio | 1030 | Caza programada, no alerta directa |
| URL | 367 | Caza programada, no alerta directa |
| Hash | 506 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (0 de 2643)

| Motivo | Descartados |
|---|---:|

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown malware | 983 |
| ClearFake | 371 |
| IClickFix | 368 |
| Unknown Loader | 206 |
| ZStealer | 204 |
| malware_download | 94 |
| Vidar | 77 |
| Mirai | 69 |
| Mozi | 41 |
| Stealc | 22 |
| Raven Stealer | 21 |
| Cobalt Strike | 20 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 740 |
| `wazuh/cti_dominio` | 1030 |
| `wazuh/cti_url` | 367 |
| `wazuh/cti_hash` | 506 |
| `wazuh/cti_cve_kev` | 26 |
| `splunk/cti_ip.csv` | 740 |
| `splunk/cti_dominio.csv` | 1030 |
| `splunk/cti_url.csv` | 367 |
| `splunk/cti_hash.csv` | 506 |
| `splunk/cti_cve_kev.csv` | 26 |
| `sentinel/CTI_Ip.csv` | 740 |
| `sentinel/CTI_Dominio.csv` | 1030 |
| `sentinel/CTI_Url.csv` | 367 |
| `sentinel/CTI_Hash.csv` | 506 |
| `elastic/cti_ip.ndjson` | 740 |
| `elastic/cti_dominio.ndjson` | 1030 |
| `elastic/cti_url.ndjson` | 367 |
| `elastic/cti_hash.ndjson` | 506 |

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
