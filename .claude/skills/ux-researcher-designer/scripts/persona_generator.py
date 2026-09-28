#!/usr/bin/env python3
"""Generate research-backed personas from user data and interview notes.

Usage:
    python scripts/persona_generator.py [data.json] [--format text|json]

Without a data file it runs on built-in sample data.
"""

import argparse
import json
import sys
from collections import Counter

FREQUENCY_SCORE = {"daily": 4, "weekly": 3, "monthly": 2, "rarely": 1}

ARCHETYPES = {
    "power_user": {
        "name": "Usuario experto",
        "summary": "Usa el producto seguido y se mueve con soltura en lo digital.",
        "implications": [
            "Atajos, acciones masivas y repetir pedidos anteriores",
            "Información densa sin pasos de onboarding que estorben",
            "Personalización y configuraciones avanzadas",
        ],
    },
    "pragmatic": {
        "name": "Usuario pragmático",
        "summary": "Usa el producto de forma regular para resolver tareas concretas.",
        "implications": [
            "Flujos principales cortos y predecibles",
            "Estados claros de éxito y error",
            "Ayuda contextual solo cuando hace falta",
        ],
    },
    "occasional": {
        "name": "Usuario ocasional",
        "summary": "Entra de vez en cuando y necesita reorientarse cada vez.",
        "implications": [
            "Navegación evidente y lenguaje sin jerga",
            "Recordar datos y preferencias de la visita anterior",
            "Recordatorios o avisos para volver en el momento justo",
        ],
    },
    "reluctant": {
        "name": "Usuario reticente",
        "summary": "Tiene poca confianza en lo digital y usa el producto por obligación.",
        "implications": [
            "Un solo paso por pantalla, botones grandes y textos simples",
            "Canal humano visible (teléfono, WhatsApp) como respaldo",
            "Confirmaciones explícitas antes de acciones irreversibles",
        ],
    },
}

SAMPLE_DATA = {
    "users": [
        {"id": "u1", "age": 34, "role": "Farmacéutica", "tech_savviness": 5,
         "usage_frequency": "daily", "device": "desktop",
         "goals": ["reponer stock rápido", "controlar precios"],
         "pain_points": ["demasiados pasos para pedir"],
         "motivations": ["ahorrar tiempo"],
         "quotes": ["Quiero pedir en dos clicks."]},
        {"id": "u2", "age": 29, "role": "Compradora", "tech_savviness": 4,
         "usage_frequency": "daily", "device": "desktop",
         "goals": ["reponer stock rápido"],
         "pain_points": ["no ver el estado del pedido"],
         "motivations": ["ahorrar tiempo", "evitar faltantes"],
         "quotes": ["Necesito saber cuándo llega."]},
        {"id": "u3", "age": 45, "role": "Dueño de farmacia", "tech_savviness": 3,
         "usage_frequency": "weekly", "device": "mobile",
         "goals": ["controlar precios"],
         "pain_points": ["no ver el estado del pedido"],
         "motivations": ["mejorar márgenes"],
         "quotes": ["Miro todo desde el celular."]},
        {"id": "u4", "age": 58, "role": "Dueño de perfumería", "tech_savviness": 2,
         "usage_frequency": "monthly", "device": "mobile",
         "goals": ["hacer el pedido sin errores"],
         "pain_points": ["la web es confusa", "no ver el estado del pedido"],
         "motivations": ["tranquilidad"],
         "quotes": ["Prefiero llamar al vendedor."]},
        {"id": "u5", "age": 63, "role": "Encargada", "tech_savviness": 1,
         "usage_frequency": "rarely", "device": "mobile",
         "goals": ["hacer el pedido sin errores"],
         "pain_points": ["la web es confusa"],
         "motivations": ["tranquilidad"],
         "quotes": ["Me da miedo equivocarme."]},
    ]
}


def classify(user):
    """Assign a user to an archetype from digital skill and usage frequency."""
    skill = user.get("tech_savviness", 3)
    freq = FREQUENCY_SCORE.get(str(user.get("usage_frequency", "")).lower(), 2)
    score = skill + freq  # 2..9
    if score >= 8:
        return "power_user"
    if score >= 6:
        return "pragmatic"
    if score >= 4:
        return "occasional"
    return "reluctant"


def top(counter, n=3):
    return [item for item, _ in counter.most_common(n)]


def confidence(size, total):
    """Confidence from absolute segment size and its share of the sample."""
    if size >= 12:
        level = "alta"
    elif size >= 5:
        level = "media"
    else:
        level = "baja"
    note = f"{size} de {total} participantes ({size / total:.0%})"
    if level == "baja":
        note += "; validar con más entrevistas antes de decidir"
    return level, note


def build_persona(key, users, total):
    archetype = ARCHETYPES[key]
    ages = [u["age"] for u in users if isinstance(u.get("age"), (int, float))]
    goals, pains, motivations, devices, roles = (Counter() for _ in range(5))
    quotes = []
    for u in users:
        goals.update(u.get("goals", []))
        pains.update(u.get("pain_points", []))
        motivations.update(u.get("motivations", []))
        if u.get("device"):
            devices[u["device"]] += 1
        if u.get("role"):
            roles[u["role"]] += 1
        quotes.extend(u.get("quotes", []))

    main_goal = top(goals, 1)[0] if goals else "resolver su tarea"
    main_pain = top(pains, 1)[0] if pains else "fricción en el flujo"
    device = top(devices, 1)[0] if devices else "cualquier dispositivo"
    level, note = confidence(len(users), total)

    return {
        "archetype": key,
        "name": archetype["name"],
        "summary": archetype["summary"],
        "demographics": {
            "age_range": ("sin datos" if not ages
                          else str(min(ages)) if min(ages) == max(ages)
                          else f"{min(ages)}-{max(ages)}"),
            "roles": top(roles),
            "main_device": device,
        },
        "behavior": {
            "avg_tech_savviness": round(
                sum(u.get("tech_savviness", 3) for u in users) / len(users), 1),
            "usage_frequency": top(Counter(
                u.get("usage_frequency", "sin datos") for u in users), 2),
        },
        "psychographics": {
            "goals": top(goals),
            "pain_points": top(pains),
            "motivations": top(motivations),
        },
        "quotes": quotes[:3],
        "scenario": (f"Desde {device}, quiere {main_goal}, "
                     f"pero se frena por esto: {main_pain}."),
        "design_implications": archetype["implications"],
        "confidence": {"level": level, "basis": note},
        "participants": [u.get("id") for u in users],
    }


def generate(data):
    users = data.get("users", [])
    if not users:
        raise ValueError("El JSON necesita una lista 'users' con al menos un participante.")
    groups = {}
    for u in users:
        groups.setdefault(classify(u), []).append(u)
    order = list(ARCHETYPES)
    return [build_persona(k, groups[k], len(users))
            for k in sorted(groups, key=order.index)]


def render_text(personas):
    lines = []
    for p in personas:
        d, b, ps = p["demographics"], p["behavior"], p["psychographics"]
        lines += [
            "=" * 60,
            f"{p['name']}  (confianza {p['confidence']['level']}: {p['confidence']['basis']})",
            p["summary"],
            "",
            f"Edad: {d['age_range']} | Roles: {', '.join(d['roles']) or '-'} | Dispositivo: {d['main_device']}",
            f"Habilidad digital promedio: {b['avg_tech_savviness']}/5 | Frecuencia: {', '.join(b['usage_frequency'])}",
            f"Objetivos: {', '.join(ps['goals']) or '-'}",
            f"Dolores: {', '.join(ps['pain_points']) or '-'}",
            f"Motivaciones: {', '.join(ps['motivations']) or '-'}",
        ]
        if p["quotes"]:
            lines.append("Citas: " + " / ".join(f'"{q}"' for q in p["quotes"]))
        lines += ["", f"Escenario: {p['scenario']}", "Implicancias de diseño:"]
        lines += [f"  - {i}" for i in p["design_implications"]]
        lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("data", nargs="?", help="archivo JSON con los participantes")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args()

    if args.data:
        with open(args.data, encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = SAMPLE_DATA

    try:
        personas = generate(data)
    except ValueError as e:
        sys.exit(str(e))

    if args.format == "json":
        print(json.dumps(personas, ensure_ascii=False, indent=2))
    else:
        print(render_text(personas))


if __name__ == "__main__":
    main()
