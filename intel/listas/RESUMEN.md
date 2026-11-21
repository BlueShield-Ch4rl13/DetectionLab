# Listas de inteligencia

<!-- Generado por tools/sync_cti.py desde ScriptNewsCTI - no editar a mano -->

**Origen:** [ScriptNewsCTI](https://github.com/BlueShield-Ch4rl13/ScriptNewsCTI)  
**Feed generado:** 2026-11-21 10:46 UTC  
**Listas generadas:** 2026-11-21T13:57:58Z  
**Filtro aplicado:** nivel minimo `media`, maximo `30` dias de antiguedad

## Que hay en cada lista

| Indicador | Entradas | Uso previsto |
|---|---:|---|
| IP | 222 | Caza programada, no alerta directa |
| Dominio | 510 | Caza programada, no alerta directa |
| URL | 187 | Caza programada, no alerta directa |
| Hash | 778 | **Alerta directa**: un hash coincide o no |
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

## Que se descarto del feed (59 de 1756)

| Motivo | Descartados |
|---|---:|
| nivel bajo | 59 |

## Familias mas presentes

| Amenaza | Indicadores |
|---|---:|
| Skimer | 334 |
| Unknown malware | 254 |
| ZStealer | 156 |
| Merdoor | 120 |
| Mirai | 114 |
| malware_download | 100 |
| Unknown Stealer | 72 |
| Raven Stealer | 69 |
| ClearFake | 42 |
| INC and The Gentlemen Ransomware: Exposed AI Infrastructure | 27 |
| Stray Cat  Open Doors: How k0t Wanders Through the Network Edge | 21 |
| Vidar | 21 |

## Ficheros generados

| Fichero | Entradas |
|---|---:|
| `wazuh/cti_ip` | 222 |
| `wazuh/cti_dominio` | 510 |
| `wazuh/cti_url` | 187 |
| `wazuh/cti_hash` | 778 |
| `wazuh/cti_cve_kev` | 21 |
| `splunk/cti_ip.csv` | 222 |
| `splunk/cti_dominio.csv` | 510 |
| `splunk/cti_url.csv` | 187 |
| `splunk/cti_hash.csv` | 778 |
| `splunk/cti_cve_kev.csv` | 21 |
| `sentinel/CTI_Ip.csv` | 222 |
| `sentinel/CTI_Dominio.csv` | 510 |
| `sentinel/CTI_Url.csv` | 187 |
| `sentinel/CTI_Hash.csv` | 778 |
| `elastic/cti_ip.ndjson` | 222 |
| `elastic/cti_dominio.ndjson` | 510 |
| `elastic/cti_url.ndjson` | 187 |
| `elastic/cti_hash.ndjson` | 778 |

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
