# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-09 05:44 UTC  
**Listas generadas:** 2026-10-09T12:22:07Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 127 | Caza programada, no alerta directa |
| Dominio | 533 | Caza programada, no alerta directa |
| URL | 258 | Caza programada, no alerta directa |
| Hash | 90 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (457 de 1494)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 353 |
| nivel bajo | 104 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown Loader | 319 |
| malware_download | 100 |
| ClearFake | 89 |
| Unknown Stealer | 81 |
| php.shin_webshell | 80 |
| Unknown malware | 38 |
| IClickFix | 31 |
| ClearFake WebDAV infection chain delivers Amatera stealer  ZigCryptoStealer  and NetSupport Manager | 30 |
| Vidar | 29 |
| 16 Malicious Firefox Extensions Steal Cryptocurrency Wallet Credentials | 21 |
| Inside a Packed Android RAT Loader | 20 |
| Remcos | 13 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 127 |
| `wazuh/cti_dominio` | 533 |
| `wazuh/cti_url` | 258 |
| `wazuh/cti_hash` | 90 |
| `wazuh/cti_cve_kev` | 16 |
| `splunk/cti_ip.csv` | 127 |
| `splunk/cti_dominio.csv` | 533 |
| `splunk/cti_url.csv` | 258 |
| `splunk/cti_hash.csv` | 90 |
| `splunk/cti_cve_kev.csv` | 16 |
| `sentinel/CTI_Ip.csv` | 127 |
| `sentinel/CTI_Dominio.csv` | 533 |
| `sentinel/CTI_Url.csv` | 258 |
| `sentinel/CTI_Hash.csv` | 90 |
| `elastic/cti_ip.ndjson` | 127 |
| `elastic/cti_dominio.ndjson` | 533 |
| `elastic/cti_url.ndjson` | 258 |
| `elastic/cti_hash.ndjson` | 90 |

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
