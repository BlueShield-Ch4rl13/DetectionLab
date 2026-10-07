# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-10-07 05:32 UTC  
**Listas generadas:** 2026-10-07T12:24:49Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 0 | Caza programada, no alerta directa |
| Dominio | 0 | Caza programada, no alerta directa |
| URL | 100 | Caza programada, no alerta directa |
| Hash | 100 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (92 de 292)

| Motivo | Descartados |
|---|---:|
| tipo no usado | 62 |
| nivel bajo | 30 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| malware_download | 100 |
| ClingSTUN Linux Backdoor Abuses Public STUN Infrastructure | 49 |
| Anatomy of BraZetsu: How Cybercriminals Supply the Underground Ecosystem | 32 |
| Lunex Uses BYOVD to Disable Security Monitoring and Deploy Persistent Stealer | 9 |
| A STUNning Disguise: Cling Malware Masquerades as Google | 6 |
| StyleSmuggler: Magento and Adobe Commerce 0-day RCE under active attack | 4 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 0 |
| `wazuh/cti_dominio` | 0 |
| `wazuh/cti_url` | 100 |
| `wazuh/cti_hash` | 100 |
| `wazuh/cti_cve_kev` | 13 |
| `splunk/cti_ip.csv` | 0 |
| `splunk/cti_dominio.csv` | 0 |
| `splunk/cti_url.csv` | 100 |
| `splunk/cti_hash.csv` | 100 |
| `splunk/cti_cve_kev.csv` | 13 |
| `sentinel/CTI_Ip.csv` | 0 |
| `sentinel/CTI_Dominio.csv` | 0 |
| `sentinel/CTI_Url.csv` | 100 |
| `sentinel/CTI_Hash.csv` | 100 |
| `elastic/cti_ip.ndjson` | 0 |
| `elastic/cti_dominio.ndjson` | 0 |
| `elastic/cti_url.ndjson` | 100 |
| `elastic/cti_hash.ndjson` | 100 |

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
