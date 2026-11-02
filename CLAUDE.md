# Coach de Luis Miguel — reglas para la sesión semanal

App PWA (index.html) publicada en https://lsmiguel91-ui.github.io/coach/ desde la rama `main`.
El plan de entrenamiento vive en **plan.json** (la app lo descarga al abrir; index.html trae una copia vieja solo como respaldo).
Los datos que él registra (notas, Garmin, completado) están en Google Drive, fileId `1cvSm0c0z094HYEPbuBk4rQ0N1Bo8jN_R`.

## Quién es
Luis Miguel, 35 años, 70 kg, 1.68 m, Quito (2850 m). Oficial FAE. Entrena solo de madrugada (antes de 06:10 lun/vie y 07:10 mar-jue), en trotadora NordicTrack (km/h, hasta 10% inclinación), con mancuernas hasta 16 kg, banda, foam roller, ABCoaster. Reloj Garmin Forerunner 265. No es experto en métricas: explicar simple.

## Metas (Tabla 5 FAE, 34-36 años)
- 3219 m: aprobar 14:11 (13.6 km/h) · meta 13:46 (≈14 km/h).
- Push-ups 1'30": aprobar 43 · meta 48.
- Abdominales militares 1'30" (escápula completa): aprobar 52 · meta 58.
El examen 2026 no lo rinde; entrena con intensidad moderada-alta sin presión de fecha.

## Estructura semanal fija (no cambiar días ni tipo salvo que él lo pida)
Lun trote moderado · Mar intervalos · Mié pecho + abdomen con tests (abd. militares 1'30" + AMRAP push-ups) · Jue ritmo · Vie piernas que protegen la rodilla + abd. por velocidad · Sáb fondo + pecho corto · Dom descanso.
Tipos válidos en plan.json: trote, intervalos, ritmo, fondo, pecho, piernas, abd, descanso.

## Reglas de progresión (aplicar cada domingo con los datos de la semana)
1. Volumen o velocidad: nunca subir más de ~10% por semana. Un solo cambio por sesión.
2. Días suaves (trote, fondo): FC prom ≤150. Si salió >150 → bajar 0.5 km/h o mantener; si ≤145 dos semanas seguidas → subir 0.2-0.3 km/h o +5 min.
3. Intervalos: avanzar (+0.2-0.3 km/h, o +1 serie, o -15 s descanso) solo si completó todas las series con esfuerzo (RPE) ≤8. Si falló una serie → mantener.
4. Ritmo: avanzar (+0.2 km/h o +250 m por bloque) si completó con RPE ≤8.
5. Cadencia objetivo 165-170: si está por debajo, recordarlo en la sesión ("pasos cortos y rápidos").
6. Abd. militares: series fijas hasta que todas salgan limpias sin fatiga final; luego +5 reps por serie. Push-ups: mantener volumen moderado (no agotar antes del test).
7. Rodilla derecha (historial de dolor medial bajo la articulación): dolor ≥3/10 → la semana siguiente baja impacto (trote → bici o caminata inclinada, sin intervalos) y avísale. 1-2/10 → mantener, no subir carga de carrera.
8. Sueño <6.5 h varios días o Readiness bajo → no subir carga esa semana.
9. Sesión no registrada ≠ no hecha: si no hay datos, mantener esa sesión igual (no subir ni bajar) y mencionarlo.
10. Cada 4.ª semana, descarga: -20% volumen de carrera, mismas velocidades.
11. Protocolos que siempre van: test de la grada + foam roller antes de correr; enfriamiento anti-mareo 5 min @6 km/h al final de cada carrera.
12. Mencionar en "obj" la velocidad, inclinación y RPE esperado; en los items, "d" = cantidades y "c" = cómo hacerlo, en palabras simples. YouTube: campo "yt" con texto de búsqueda (nunca links directos).

## Formato de una sesión en plan.json
"YYYY-MM-DD": {"t","ic" (emoji),"tit","dur","obj","hora","bloques":[{"f":"Nombre bloque","items":[{"n","d","c","yt"?,"k"?:1 si es el ejercicio clave}]}],"tips"?:[...]}
Herramienta: `python3 tools/semana.py ver|copiar|validar plan.json ...`. Siempre `validar` antes de subir.

## Publicar
git add plan.json && git commit && git push origin main. No toques index.html ni sw.js en la sesión semanal.
Commits con la línea: Co-Authored-By: Claude <noreply@anthropic.com>
