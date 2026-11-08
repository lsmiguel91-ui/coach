# Contexto del proyecto — Coach de Luis Miguel

Estado al **8 de noviembre de 2026**. Este archivo cuenta **qué hay y cómo se llegó aquí**.
Las reglas de trabajo (progresión semanal, lectura de métricas, estructura de datos, formato
de `plan.json`) viven en **CLAUDE.md** y mandan sobre cualquier cosa escrita aquí.
Si cambia una regla, se cambia en CLAUDE.md, no en este archivo.

---

## 1. Qué es y dónde vive

App PWA para preparar la prueba física de la FAE y registrar cada sesión. La copia viva es
este repositorio; no hay ninguna otra.

| | |
|---|---|
| Repositorio | `lsmiguel91-ui/coach`, rama `main` |
| App publicada | https://lsmiguel91-ui.github.io/coach/ (GitHub Pages, main /root) |
| Datos del atleta | Google Drive, `plan_entrenamiento_notas.json`, fileId `1cvSm0c0z094HYEPbuBk4rQ0N1Bo8jN_R` |
| Reportes PDF | Google Drive, carpeta "Reportes coach semanales", id `1nK2QPvdBPXlNcg1jRkgQjOwtAdQULYtU` |
| Respaldos | OneDrive `_versiones/COACH/` — **solo respaldos fechados, no se edita nada ahí** |

Archivos del repo: `index.html` (la app completa), `plan.json` (el plan, se descarga al abrir),
`sw.js` (service worker), `CLAUDE.md` (reglas), `CONTEXTO.md` (este archivo),
`tools/reporte_coach.py` (PDF semanal), `tools/semana.py` (ver, copiar y validar semanas).

La URL del Apps Script que sincroniza con Drive **no está en el repo a propósito**: el
repositorio es público y ese endpoint no tiene autenticación. Se pega una vez por dispositivo
dentro de la app y queda en `localStorage`.

## 2. Tarea programada

"Coach semanal: reporte + plan" (`trig_01Q2KFkoXvXyPGAahGG4FZPa`), **domingos 18:55**, corre
solo en la nube, sin carpeta local asociada. Lee los datos de Drive, genera el PDF con la
página del plan de la próxima semana, se lo envía y lo sube a Drive, y carga la semana
siguiente en `plan.json` sin esperar confirmación. Él ajusta después si quiere.

## 3. Estado actual

**Funcionando al 100%:**

- App publicada y sincronizando con Drive.
- Plan separado en `plan.json`; el service worker no lo cachea. Versión del SW: **v6**.
- Recuadro "⌚ Reloj" en cada sesión, con la actividad del reloj y qué alertas usar.
- **Campos de métricas por tipo de día** (desde 4-nov): en pecho y abdomen no aparecen
  cadencia, distancia ni rodilla; en piernas vuelve rodilla; en intervalos y ritmo se agregó
  potencia media de series.
- **Registro por ejercicio** (desde 4-nov): cada ejercicio de fuerza muestra una casilla por
  serie prellenada con lo planificado, casilla de kg donde aplica, y botón "tal cual". Los
  tests van sin prellenar, con la meta como pista. Se guarda en `dias[fecha].e`.
- **Gráficos de Progreso** alimentados con lo registrado, combinados con el histórico fijo
  hasta la semana del 12-18 oct.
- **Las semanas se nombran por fechas** ("2–8 nov"), nunca por número correlativo.

**Reloj Forerunner 265 configurado:** pantalla de Cinta 1 con Tiempo/Distancia/FC/Cadencia y
pantalla 2 con FC media/Cadencia media/Distancia/Tiempo; en Fuerza, Cronómetro de serie/
Repeticiones/FC/Tiempo con series automáticas desactivadas. **Pausa automática desactivada**
desde el 3-nov. Cardio no se usa.

## 4. Decisiones tomadas (no revertir)

1. **El examen 2026 no se rinde.** Entrena con intensidad moderada-alta, sin fecha límite,
   solo de madrugada (antes de 06:10 lunes y viernes, 07:10 martes a jueves).
2. **Estructura semanal fija:** lunes trote · martes intervalos · miércoles pecho + abdomen
   con tests · jueves ritmo · viernes piernas que protegen la rodilla + abdominales de
   velocidad · sábado fondo + pecho corto · domingo descanso.
3. El plan se aplica **solo** cada domingo; él confirma o ajusta después.
4. Los entregables de las tareas programadas van a **Google Drive, nunca a carpetas de la PC**:
   la computadora puede estar apagada cuando la tarea corre.
5. **Netlify ya no se usa.** GitHub es la copia viva.
6. Alertas en Cinta: FC alta 150 solo en trote y fondo; cadencia baja 160 siempre activa;
   cadencia alta desactivada.

## 5. Problemas resueltos (no reinventar)

- La tarea programada vieja terminaba en 5 s porque seguía atada a una carpeta de OneDrive.
  Se creó una nueva sin carpeta; la vieja (`trig_01WmWz3Weart9Cwopb4qheCA`) quedó desactivada.
- Push a GitHub rechazado → él agregó el repo `coach` a la app de Claude en GitHub
  (Settings → Installations).
- GitHub Pages se activa a mano en Settings → Pages (main, /root); el proxy no lo permite por API.
- Los emojis en el PDF no los dibuja la fuente: se eliminaron de los textos.
- LAP en Cinta solo marca vueltas, no pausa. La pantalla de descanso existe solo en Fuerza.
- Readiness se toma de "Predisposición para entrenar", no de la puntuación de sueño.
- FC máx no va en la pantalla de datos del reloj: se lee en el resumen al terminar.
- **El reloj no puede escribirse desde aquí.** El conector de Drive lee contenido y edita
  metadatos, pero no sobrescribe el contenido de un archivo existente: las correcciones al
  JSON de datos las hace él en la app, que además es la fuente y sobrescribiría cualquier
  edición hecha por debajo.
- Garmin no tiene "hollow body hold" en su catálogo y no permite crear nombres propios. Lo
  más cercano es "Hollow rock", en la categoría Abdominales. Da igual: el dato que cuenta ya
  queda en la app.

## 6. Semana 2–8 nov — lo que quedó registrado

Semana completa, seis sesiones, todas marcadas. Lecturas que deben entrar en la progresión:

- **Lunes 2, trote:** FC prom 157, por encima del tope de 150 de los días suaves → **no sube
  velocidad**. Enfriamiento de solo 2 min. Sueño 5.8 h.
- **Martes 3, intervalos:** 5 series a 12.5 km/h y 1.5 %, cadencia de series 173, potencia
  media 311 W, RPE 7 → **puede avanzar**. (Creyó haber hecho 6: el intervalo 1 de Garmin dura
  5.7 s, es un LAP pulsado dos veces.)
- **Miércoles 4, pecho y abdomen:** doce ejercicios registrados, pero **sin ninguna métrica**
  (ni sueño, ni readiness, ni RPE, ni FC). Tests: abdominales militares 52 **con tres pausas**,
  así que no es un 52 limpio; AMRAP push-ups 36, de las cuales 30 corridas, por debajo de las
  43 de aprobar. Plancha 2:30 a RPE 7, su mejor marca.
- **Jueves 5, ritmo:** RPE **8.5**, por encima del tope de 8 → **se mantiene en 12.5**.
  Potencia 335 W, la más alta de la semana. Readiness 53.
- **Viernes 6, piernas:** RPE **3**, readiness 85, sueño 9.5 h, y superó todo lo planificado
  (peso muerto 15 kg × 12 contra 14 kg × 10; bloques de abdominales 25-25-25-25-23 contra una
  meta de 18-20) → **esa sesión está corta, hay que subirla**.
- **Sábado 7, fondo + pecho corto:** FC prom 151, cadencia 160, 6.29 km, RPE 6, rodilla 0.5.
  Nota: dolor inicial de rodilla yendo muy lento y con mala cadencia, que se fue después.
- **Rodilla en la semana:** 0.5, 0.5, 0, 0, 0.5 — la mejor racha registrada.

## 7. Pendientes

1. **Hoy domingo 8, 18:55:** primer reporte automático completo y carga de la semana siguiente.
   Verificar que llegue el aviso y que el PDF quede en Drive.
2. **Decisión abierta sobre los tests.** El AMRAP de push-ups y los abdominales militares están
   al final de la sesión del miércoles, después de todo el trabajo de pecho. Ese número no mide
   su capacidad real ni es comparable con la prueba de la FAE, donde llegaría fresco. Está
   propuesto moverlos al inicio del miércoles o a un día aparte; **falta que él lo apruebe**.
3. **Calibración de la cinta:** ya calibra antes de guardar y el total es confiable, pero el
   ritmo por intervalo que muestra Garmin sigue subestimando. Las series se miden por tiempo ×
   velocidad de banda.
4. **25 de noviembre:** decidir si se cancela Strava. Hay un recordatorio programado
   (`trig_01WRJ1M2PyDcSAXN3QC6KzEm`). Strava no era elegible para su cuenta por despliegue
   gradual; revisar si ya lo es.
5. Recordatorios vivos para él: completar los 5 min de enfriamiento, dormir 6.5 h o más, y no
   agregar series extra a lo planificado.

## 8. Cómo trabajar con él

Respuestas cortas y precisas, sin preámbulo. Preguntar antes de diseñar o ejecutar cambios.
En cambios técnicos, decir qué cambió y por qué, sin mostrar código ni salidas de terminal; si
algo falla, el problema en una línea. Señalarle los problemas que se detecten aunque no sean lo
que se estaba conversando. Si falta un acceso, decirlo claro desde el inicio. No es experto en
métricas: explicar simple.

**Al tocar `index.html` hay que subir `VERSION` en `sw.js`** (v6, v7…) o el teléfono se queda
con la versión vieja en caché.
