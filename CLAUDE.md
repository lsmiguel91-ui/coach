# Coach de Luis Miguel — reglas para la sesión semanal

> Este archivo tiene las **reglas** y manda sobre cualquier otra cosa escrita en el repo.
> El **estado del proyecto** (qué hay hecho, qué se decidió, qué está pendiente) está en
> `CONTEXTO.md`: léelo al empezar un chat nuevo, pero no copies reglas ahí.

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
5. Cadencia objetivo 165-170: si está por debajo, recordarlo en la sesión ("pasos cortos y rápidos"). Alertas del reloj (Cinta): cadencia baja 160 siempre activa, cadencia alta desactivada; FC alta 150 solo en trote/fondo. Cuando su cadencia media en días suaves sea ≥165 dos semanas seguidas, indícale subir la alerta baja a 165.
6. Abd. militares: series fijas hasta que todas salgan limpias sin fatiga final; luego +5 reps por serie. Push-ups: mantener volumen moderado (no agotar antes del test).
6b. **Los dos tests del miércoles van siempre al inicio de la sesión, en fresco** (desde el 11-nov-2026): activación corta, test de abdominales militares, 3 min de descanso, AMRAP de push-ups, y recién después todo el trabajo de pecho. Nunca al final: un test hecho con el pecho ya cansado no mide su capacidad ni se parece a la prueba real de la FAE. Si por el test se le cae la última serie de press o de fondos, se quita esa serie y se anota; no cuenta como retroceso.
6c. **Los tests del 11-nov-2026 en adelante no son comparables con los anteriores**, que se tomaban al final de la sesión. El salto de esa semana no es mejora real: la línea base limpia arranca ahí. No aplicar la regla 1 (máximo ~10 % semanal) sobre ese salto ni celebrarlo como progreso.
7. Rodilla derecha (historial de dolor medial bajo la articulación): dolor ≥3/10 → la semana siguiente baja impacto (trote → bici o caminata inclinada, sin intervalos) y avísale. 1-2/10 → mantener, no subir carga de carrera.
8. Sueño <6.5 h varios días o Readiness bajo → no subir carga esa semana.
9. Sesión no registrada ≠ no hecha: si no hay datos, mantener esa sesión igual (no subir ni bajar) y mencionarlo.
10. Cada 4.ª semana, descarga: -20% volumen de carrera, mismas velocidades.
11. Protocolos que siempre van: test de la grada + foam roller antes de correr; enfriamiento anti-mareo 5 min @6 km/h al final de cada carrera.
12. Mencionar en "obj" la velocidad, inclinación y RPE esperado; en los items, "d" = cantidades y "c" = cómo hacerlo, en palabras simples. YouTube: campo "yt" con texto de búsqueda (nunca links directos).

## Cómo se leen y registran las métricas (cinta + Garmin)
Reglas fijas desde el 3-nov-2026. En cinta el reloj estima la distancia con el acelerómetro de muñeca: subestima la carrera rápida y sobreestima la caminata. Por eso **el ritmo que muestra Garmin en cinta no sirve** para evaluar progreso.

1. **Distancia**: siempre la que marca la cinta, ingresada en el reloj con "Calibrar y guardar" antes de guardar la actividad. Una vez guardada ya no se puede corregir.
2. **Velocidad de las series**: se deduce de la velocidad de la banda y el tiempo del intervalo, nunca del "ritmo medio" de Garmin. Ese es el número que se compara contra la meta de 3219 m.
3. **Pausa automática desactivada** en el perfil de Cinta. Con pausa activa el reloj se corta al bajar la banda entre series, se reanuda solo y ensucia los laps.
4. **Laps basura**: al contar series, ignorar los intervalos de menos de ~20 s; son un LAP pulsado dos veces. (El 3-nov aparecían 6 intervalos de "Carrera", pero uno duraba 5.7 s: fueron 5 series, no 6.)
5. **FC máxima**: siempre de Estadísticas → Frecuencia cardiaca máxima, de toda la actividad. Es un techo, no se recorta al límite de un lap.
6. **FC promedio y cadencia**, según el tipo de día:
   - Días continuos (trote, ritmo, fondo): de toda la actividad.
   - Días con descansos (intervalos): **de las series**, no del total. Se leen en Intervalos → filtro "Carrera" → girar el teléfono a horizontal → fila Total. El promedio del total está diluido por las caminatas y no significa nada.
   - Al evaluar, **no comparar la FC prom de un día de intervalos contra el umbral de 150** de la regla 2: ese umbral aplica solo a días continuos.
7. **Potencia media de las series** (misma fila Total, en W y W/kg): es el mejor indicador de fatiga dentro de la sesión, porque no la afecta ni la calibración de la cinta ni el retardo de la FC. Si cae de forma sostenida entre la primera y la última serie, el volumen o la velocidad están altos aunque el RPE diga lo contrario.
8. **Enfriamiento**: la regla 11 pide 5 min y en nov-2026 venía haciendo 2-3 min. Revisar las notas y recordárselo mientras no se cumpla; con la rodilla en 0-1/10 es justo el tramo que no conviene recortar.
9. **Alerta de cadencia en el calentamiento**: a 8 km/h la alerta de cadencia baja (160) suena seguido. Es esperado y es útil: a esa velocidad 160 ppm equivale a una zancada de 0.83 m, perfectamente alcanzable. No desactivarla; usarla para entrar al trabajo con pasos cortos y rápidos.

## Qué registra la app en cada día (estructura de datos)
`datos.dias["YYYY-MM-DD"] = {nota, m:{}, e:{}, ok, f}` y eso es lo que llega a Drive.

- **`m`** = métricas del día. Los campos que se muestran dependen del tipo de sesión, no son los mismos todos los días:
  `trote`/`fondo` → fcp, fcm, cad, dist, rdy, sue, rod, rpe · `intervalos`/`ritmo` → los mismos **+ pot** (potencia media de las series) · `pecho`/`abd` → fcp, fcm, rdy, sue, rpe · `piernas` → esos + rod · `descanso` → rdy, sue, rod.
  Si un día viejo trae campos que su tipo ya no muestra, se conservan: no se borran.
- **`e`** = lo registrado ejercicio por ejercicio: `{"<id>": {n:"nombre", u:"reps"|"s", v:["12","12","10"], kg:"10"}}`. El id es el nombre del ejercicio en minúsculas y sin tildes, más su posición en el día.
- **`nota`** = texto libre, ahora opcional: los números van en `e`, la nota es para lo que no es número.

### Cómo decide la app qué pedir en cada ejercicio
Lo deduce del campo `d` del propio ejercicio, así que **no hay que cambiar nada en plan.json** para que funcione:
`3 × 12` → 3 casillas de repeticiones · `3 × 45 s` → 3 casillas de segundos · `4 × 8 · 10 kg` → 4 casillas + casilla de kg · `5 × 30 s · meta 18` → 5 casillas de repeticiones (manda la meta) · `meta 2:20` → una casilla de tiempo · AMRAP, `1'30"` o "sin pausa" → test de una sola casilla, sin prellenar, con la meta como pista.
No se pide nada en calentamiento, enfriamiento, foam roller, test de la grada, drills, ni en nada que lleve km/h o series en metros: eso ya lo cubre el reloj.
Para forzarlo desde plan.json: `"cap":{"u":"reps","ns":4,"v":"8","kg":"10"}` en el ejercicio, o `"cap":false` para que no pida nada.

### Qué hacer con esto en la sesión semanal
- Los gráficos de Progreso de la app ya combinan el histórico fijo (hasta la semana 17) con lo registrado en `e` de la semana 20 en adelante: push-ups AMRAP, abdominales militares, plancha y hollow.
- **Las semanas se nombran por fechas, no por número.** En la app, en el reporte y en el PDF se escribe el rango ("2–8 nov", "30 nov–6 dic"), nunca "Semana 20". En el JSON del reporte, `rango` es lo que se imprime como subtítulo y `fuerza_hist.etiquetas` son las etiquetas del eje x (por ejemplo "2/11"); `semana` ya no se usa en el PDF.
- Para el PDF, llenar `fuerza_detalle` en el JSON del reporte: `[{"dia":"Mié 4","filas":[["Press mancuernas banco plano","8·8·8·7 · 10 kg"],...]}]`. Si no se llena, el PDF sale igual que antes.
- Al evaluar la regla 6, usar `e` y no la nota: ahí está cuántas repeticiones hizo de verdad en cada serie.

## Formato de una sesión en plan.json
"YYYY-MM-DD": {"t","ic" (emoji),"tit","dur","obj","hora","bloques":[{"f":"Nombre bloque","items":[{"n","d","c","yt"?,"k"?:1 si es el ejercicio clave}]}],"tips"?:[...]}
Herramienta: `python3 tools/semana.py ver|copiar|validar plan.json ...`. Siempre `validar` antes de subir.

## Publicar
git add plan.json && git commit && git push origin main. No toques index.html ni sw.js en la sesión semanal.
Si alguna vez sí se cambia index.html, hay que subir `VERSION` en sw.js (v5, v6…) o el teléfono se queda con la versión vieja en caché.
Commits con la línea: Co-Authored-By: Claude <noreply@anthropic.com>
