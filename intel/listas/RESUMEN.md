# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-11 05:20 UTC  
**Listas generadas:** 2026-10-11T11:53:52Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 120 | Caza programada, no alerta directa |
| Dominio | 164 | Caza programada, no alerta directa |
| URL | 214 | Caza programada, no alerta directa |
| Hash | 178 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (339 de 1054)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 318 |
| nivel bajo | 21 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Mantax Otax: Indonesian Mobile Ransomware with Spyware Integration | 139 |
| malware_download | 100 |
| Unknown malware | 54 |
| Vidar | 50 |
| php.shin_webshell | 47 |
| IClickFix | 43 |
| ClearFake | 38 |
| Casbaneiro: A Banking Trojan with Distributed Data-Receiving Servers | 23 |
| VShell | 16 |
| Melofee: a look back at a Linux implant and its new variants | 15 |
| Jackskid | 14 |
| Mirai | 11 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 120 |
| `wazuh/cti_dominio` | 164 |
| `wazuh/cti_url` | 214 |
| `wazuh/cti_hash` | 178 |
| `wazuh/cti_cve_kev` | 13 |
| `splunk/cti_ip.csv` | 120 |
| `splunk/cti_dominio.csv` | 164 |
| `splunk/cti_url.csv` | 214 |
| `splunk/cti_hash.csv` | 178 |
| `splunk/cti_cve_kev.csv` | 13 |
| `sentinel/CTI_Ip.csv` | 120 |
| `sentinel/CTI_Dominio.csv` | 164 |
| `sentinel/CTI_Url.csv` | 214 |
| `sentinel/CTI_Hash.csv` | 178 |
| `elastic/cti_ip.ndjson` | 120 |
| `elastic/cti_dominio.ndjson` | 164 |
| `elastic/cti_url.ndjson` | 214 |
| `elastic/cti_hash.ndjson` | 178 |

## Como se instala cada una

Ver `deploy/<siem>/INSTALAR.md`. En resumen:

```bash
# Wazuh: copiar, declarar en ossec.conf y compilar
sudo cp intel/listas/wazuh/*.cdb /var/ossec/etc/lists/
sudo /var/ossec/bin/ossec-makelists

# Splunk: como lookups de la app
cp intel/listas/splunk/*.csv $SPLUNK_HOME/etc/apps/TA-detection-lab/lookups/

# Sentinel: Watchlists > New > importar el CSV, alias sin el prefijo CTI_
# Elastic: bulk al indice de indicadores
curl -XPOST 'localhost:9200/logs-ti_newscti-default/_bulk' \
     -H 'Content-Type: application/x-ndjson' \
     --data-binary @intel/listas/elastic/cti_ip.ndjson
```
