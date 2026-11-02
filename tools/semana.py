# -*- coding: utf-8 -*-
"""Ayuda para editar plan.json semana a semana.

  python3 tools/semana.py ver   plan.json 2026-11-09          -> muestra la semana (lunes dado)
  python3 tools/semana.py copiar plan.json 2026-11-09 2026-11-16 -> copia la semana del lunes origen al lunes destino
  python3 tools/semana.py validar plan.json                    -> revisa estructura de todas las sesiones

Luego se editan a mano (o con Python) los campos tit/obj/dur y los "d" de cada item.
"""
import json, sys, datetime as dt

TIPOS = {'trote','intervalos','ritmo','fondo','pecho','piernas','abd','descanso'}
D = lambda s: dt.date.fromisoformat(s)

def cargar(f): return json.load(open(f, encoding='utf-8'))
def guardar(f, p): json.dump(dict(sorted(p.items())), open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

def validar(p):
    err = []
    for k, s in p.items():
        try: D(k)
        except Exception: err.append(f'{k}: fecha inválida')
        for c in ('t', 'ic', 'tit', 'dur', 'obj'):
            if c not in s: err.append(f'{k}: falta {c}')
        if s.get('t') not in TIPOS: err.append(f'{k}: tipo {s.get("t")} no válido')
        if s.get('t') != 'descanso' and not s.get('bloques'): err.append(f'{k}: sin bloques')
        for b in s.get('bloques', []):
            if 'f' not in b or 'items' not in b: err.append(f'{k}: bloque mal formado')
            for it in b.get('items', []):
                if 'n' not in it or 'd' not in it: err.append(f'{k}: item sin n/d')
    return err

if __name__ == '__main__':
    cmd, f = sys.argv[1], sys.argv[2]; p = cargar(f)
    if cmd == 'ver':
        l = D(sys.argv[3])
        for i in range(7):
            k = (l + dt.timedelta(i)).isoformat(); s = p.get(k)
            print(k, '—' if not s else f"[{s['t']}] {s['tit']} · {s['obj']}")
            for b in (s or {}).get('bloques', []):
                for it in b['items']: print('     ', b['f'], '|', it['n'], '|', it['d'])
    elif cmd == 'copiar':
        o, d = D(sys.argv[3]), D(sys.argv[4])
        for i in range(7):
            ko = (o + dt.timedelta(i)).isoformat(); kd = (d + dt.timedelta(i)).isoformat()
            if ko in p: p[kd] = json.loads(json.dumps(p[ko]))
        guardar(f, p); print('copiada', o, '->', d)
    elif cmd == 'validar':
        e = validar(p); print('OK' if not e else '\n'.join(e)); sys.exit(1 if e else 0)
