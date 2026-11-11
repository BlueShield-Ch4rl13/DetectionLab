# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-11 04:21 UTC  
**Listas generadas:** 2026-11-11T13:20:06Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 137 | Caza programada, no alerta directa |
| Dominio | 341 | Caza programada, no alerta directa |
| URL | 175 | Caza programada, no alerta directa |
| Hash | 561 | **Alerta directa**: un hash coincide o no |
| CVE en KEV | 19 | Priorizacion de parcheo y caza de explotacion |

## Por que las IP y los dominios no alertan

Un indicador de reputacion coincide muchas veces por motivos aburridos:
sinkholes de investigadores, CDN compartidas, dominios reciclados, rangos
de proveedores de nube. Desplegarlos como alerta directa llena la cola de
eventos que se cierran sin accion, y eso entrena al turno a cerrar sin
mirar. Se despliegan como **consultas de caza programadas con umbral**, en
`deploy/<siem>/consultas/`.

El hash es distinto: no comparte infraestructura con nada legitimo, asi que
va como alerta y ademas sin caducidad.

## Que se descarto del feed (89 de 1303)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 89 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Unknown Loader | 117 |
| ClearFake | 114 |
| Mirai | 113 |
| malware_download | 100 |
| Unknown malware | 60 |
| Vidar | 50 |
| SalatStealer | 47 |
| IClickFix | 47 |
| Inside an AhsayCBS Intrusion: Hidden Webshells  a CryptoMiner  and a C2 Implant | 42 |
| XWorm | 33 |
| php.shin_webshell | 33 |
| PureRAT | 28 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 137 |
| `wazuh/cti_dominio` | 341 |
| `wazuh/cti_url` | 175 |
| `wazuh/cti_hash` | 561 |
| `wazuh/cti_cve_kev` | 19 |
| `splunk/cti_ip.csv` | 137 |
| `splunk/cti_dominio.csv` | 341 |
| `splunk/cti_url.csv` | 175 |
| `splunk/cti_hash.csv` | 561 |
| `splunk/cti_cve_kev.csv` | 19 |
| `sentinel/CTI_Ip.csv` | 137 |
| `sentinel/CTI_Dominio.csv` | 341 |
| `sentinel/CTI_Url.csv` | 175 |
| `sentinel/CTI_Hash.csv` | 561 |
| `elastic/cti_ip.ndjson` | 137 |
| `elastic/cti_dominio.ndjson` | 341 |
| `elastic/cti_url.ndjson` | 175 |
| `elastic/cti_hash.ndjson` | 561 |

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
