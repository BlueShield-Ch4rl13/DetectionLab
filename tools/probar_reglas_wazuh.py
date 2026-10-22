#!/usr/bin/env python3
"""
Prueba las reglas generadas de Wazuh contra eventos de muestra, sin Wazuh.

Reproduce lo justo del motor de Wazuh para las fuentes que no son Windows:
el decodificador de deploy/wazuh/decodificadores/ (Sysmon for Linux) o el
decodificador json (auditoria de Kubernetes), y despues los <field> y el
<regex> de cada regla de 0970-detection_lab_sigma.xml.

No sustituye a wazuh-logtest (PCRE2 y el motor real tienen matices que aqui
no estan), pero si atrapa lo que la revision encontro: reglas que no podian
saltar nunca porque buscaban win.eventdata.* en eventos de Linux, y reglas
que saltaban de mas ("sh -i" dentro de "ssh -i").

Cada muestra de purple/muestras_wazuh.json dice que reglas deben saltar
("esperadas") y cuales no ("prohibidas").

    python tools/probar_reglas_wazuh.py
"""
from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
REGLAS = RAIZ / "deploy" / "wazuh" / "reglas" / "0970-detection_lab_sigma.xml"
DECODER = RAIZ / "deploy" / "wazuh" / "decodificadores" / "0975-sysmon_linux.xml"
MUESTRAS = RAIZ / "purple" / "muestras_wazuh.json"


def pcre(patron: str) -> re.Pattern:
    # \x3c es valido en Python igual que en PCRE2
    return re.compile(patron)


def cargar_decoder() -> tuple[re.Pattern, list[tuple[re.Pattern, str]]]:
    raiz = ET.fromstring("<raiz>" + DECODER.read_text(encoding="utf-8") + "</raiz>")
    prematch, campos = None, []
    for d in raiz.findall("decoder"):
        if d.find("parent") is None:
            prematch = pcre(d.find("prematch").text)
        else:
            campos.append((pcre(d.find("regex").text), d.find("order").text))
    return prematch, campos


def decodificar_sysmon(log: str, prematch, campos) -> dict | None:
    if not prematch.search(log):
        return None
    salida = {}
    for regex, nombre in campos:
        m = regex.search(log)
        if m:
            salida[nombre] = m.group(1)
    return salida


def aplanar(d, prefijo="") -> dict:
    """Como el decodificador json de Wazuh: objetos con puntos; las listas no se aplanan."""
    salida = {}
    for k, v in d.items():
        clave = f"{prefijo}{k}"
        if isinstance(v, dict):
            salida.update(aplanar(v, clave + "."))
        elif not isinstance(v, list):
            salida[clave] = str(v).lower() if isinstance(v, bool) else str(v)
    return salida


def cargar_reglas() -> list[dict]:
    texto = REGLAS.read_text(encoding="utf-8")
    raiz = ET.fromstring(texto[texto.index("<group"):])
    reglas = []
    for r in raiz.findall("rule"):
        decoded = r.find("decoded_as")
        reglas.append({
            "id": r.get("id"),
            "decoded_as": decoded.text if decoded is not None else None,
            "campos": [(f.get("name"), pcre(f.text), f.get("negate") == "yes") for f in r.findall("field")],
            "regex": pcre(r.find("regex").text) if r.find("regex") is not None else None,
            "origen": re.search(r"origen=(\S+)", r.find("info").text).group(1).removesuffix(".yml"),
        })
    return reglas


def salta(regla: dict, decoder: str, campos: dict, log: str) -> bool:
    if regla["decoded_as"] != decoder:
        return False
    for nombre, patron, negado in regla["campos"]:
        valor = campos.get(nombre)
        if valor is None:
            return False            # Wazuh: un <field> sobre un campo ausente no casa, ni negado
        if bool(patron.search(valor)) == negado:
            return False
    return not regla["regex"] or bool(regla["regex"].search(log))


def main() -> int:
    prematch, campos_dec = cargar_decoder()
    reglas = cargar_reglas()
    muestras = json.loads(MUESTRAS.read_text(encoding="utf-8"))
    fallos = 0
    for m in muestras:
        if m["fuente"] == "sysmon-linux":
            log = m["log"]
            campos = decodificar_sysmon(log, prematch, campos_dec)
            decoder = "sysmon-linux"
            if campos is None:
                print(f"✗ {m['nombre']}: el decodificador no reconoce el evento")
                fallos += 1
                continue
        else:
            log = json.dumps(m["evento"])
            campos = aplanar(m["evento"])
            decoder = "json"
        saltan = {r["origen"] for r in reglas if salta(r, decoder, campos, log)}
        faltan = set(m.get("esperadas", [])) - saltan
        sobran = set(m.get("prohibidas", [])) & saltan
        if faltan or sobran:
            fallos += 1
            print(f"✗ {m['nombre']}: no saltan {sorted(faltan)}; saltan de mas {sorted(sobran)}")
        else:
            print(f"✓ {m['nombre']}")
    print(f"\n{len(muestras) - fallos}/{len(muestras)} muestras correctas")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
