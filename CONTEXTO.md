# Contexto del proyecto — Coach de Luis Miguel

Estado al **8 de noviembre de 2026**. Este archivo cuenta **qué hay y cómo se llegó aquí**.
Las reglas de trabajo (progresión semanal, lectura de métricas, estructura de datos, formato
de `plan.json`) viven en **CLAUDE.md** y mandan sobre cualquier cosa escrita aquí.
Si cambia una regla, se cambia en CLAUDE.md, no en este archivo.

---

## 1. Qué es y dónde vive

App PWA para preparar la prueba física oficial de su institución y registrar cada sesión. La copia viva es
este repositorio; no hay ninguna otra.

| | |
|---|---|
| Repositorio | `lsmiguel91-ui/coach`, rama `main` |
| App publicada | https://lsmiguel91-ui.github.io/coach/ (GitHub Pages, main /root) |
| Datos del atleta | Google Drive, `plan_entrenamiento_notas.json`, (id en el archivo privado) |
| Reportes PDF | Google Drive, carpeta "Reportes coach semanales", (id en el archivo privado) |
| Respaldos | OneDrive `_versiones/COACH/` — **solo respaldos fechados, no se edita nada ahí** |

Archivos del repo: `index.html` (la app completa), `plan.json` (el plan, se descarga al abrir),
`sw.js` (service worker), `CLAUDE.md` (reglas), `CONTEXTO.md` (este archivo),
`tools/reporte_coach.py` (PDF semanal), `tools/semana.py` (ver, copiar y validar semanas).

La URL del Apps Script que sincroniza con Drive **no está en el repo a propósito**: el
repositorio es público y ese endpoint no tiene autenticación. Se pega una vez por dispositivo
dentro de la app y queda en `localStorage`.

## 2. Tarea programada

"Coach semanal: reporte + propuesta" ((id en el archivo privado), creada el 15-nov),
**domingos 18:55 hora local** (`55 23 * * 0` UTC), en la nube, modelo Opus 5.5, conectores Drive y
Gmail. Lee Drive, evalúa la semana, genera el PDF y lo sube a "Reportes coach semanales", y deja
la semana siguiente **como propuesta en la rama `propuesta/AAAA-MM-DD`**, nunca en main. Si la
semana siguiente ya está en `plan.json` de main, no propone nada y solo hace el reporte.
**Cuando él responde "aprobado"**: traer `plan.json` de esa rama a main (solo las fechas de la
semana propuesta), validar, commit y push. Gestión: claude.ai/code → Rutinas
La rutina anterior ((id en el archivo privado), que cargaba sin confirmar) ya no existe.

## 3. Estado actual

**Funcionando al 100%:**

- App publicada y sincronizando con Drive.
- Plan separado en `plan.json`; el service worker no lo cachea. Versión: **v8** (se ve junto al
  estado de sincronización; `APP_VERSION` en index.html y `VERSION` en sw.js van siempre iguales).
- **Sincronización segura entre dispositivos** (v7 y v8, 15-nov): antes de subir, la app lee
  Drive y combina **campo por campo** con la hora de edición de cada uno (`t`); en datos viejos
  sin `t`, un vacío nunca pisa un valor lleno. Al escribir se guarda solo el campo tocado. No se
  puede editar hasta la primera lectura de Drive (máx. 20 s). Lo que no sube queda pendiente
  (`coach_pend`) y se reintenta solo; aviso rojo si el equipo no está conectado o tiene cambios
  sin subir; el estado distingue "sin conexión" de "Drive respondió error" y muestra la última
  sincronización buena.
- **Auditoría del 15-nov (C1–C8, v8):** además de lo anterior, Progreso grafica solo los tests
  (y el intento único de plancha), sin huecos de semanas; el PDF muestra rodilla con decimal, no
  dibuja carreras sin pulso como 0, ajusta el eje de sueño y acepta semanas incompletas; la app
  vuelve sola al día de hoy, se recarga sola con una versión nueva si no estás escribiendo y
  un plan.json con errores ya no la tumba.
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
   solo de madrugada (horario exacto en el archivo privado).
2. **Estructura semanal fija:** lunes trote · martes intervalos · miércoles pecho + abdomen
   con tests · jueves ritmo · viernes piernas que protegen la rodilla + abdominales de
   velocidad · sábado fondo + pecho corto · domingo descanso.
3. El plan se aplica **solo** cada domingo; él confirma o ajusta después.
4. Los entregables de las tareas programadas van a **Google Drive, nunca a carpetas de la PC**:
   la computadora puede estar apagada cuando la tarea corre.
5. **Netlify ya no se usa.** GitHub es la copia viva.
6. Alertas en Cinta: FC alta 150 solo en trote y fondo; cadencia baja 160 siempre activa;
   cadencia alta desactivada.
7. **Los tests del miércoles van al inicio, en fresco** (aprobado el 8-nov, aplicado desde el
   11-nov): activación corta, abdominales militares, 3 min de descanso, AMRAP de push-ups, y
   después el pecho. Antes iban al final y el número salía castigado por el cansancio.
   **Ojo con la comparación:** los tests desde el 11-nov no son comparables con los anteriores.
   El salto de esa semana no es mejora real; la línea base limpia empieza ahí. Está escrito como
   regla 6b y 6c en CLAUDE.md.

## 5. Problemas resueltos (no reinventar)

- La tarea programada vieja terminaba en 5 s porque seguía atada a una carpeta de OneDrive.
  Se creó una nueva sin carpeta; la vieja ((id en el archivo privado)) quedó desactivada.
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

- **Datos del celular que no llegaban a Drive (15-nov):** el lunes 9-nov quedó en Drive sin
  nota, cadencia ni "completada", y la PC (Edge) no tenía configurada la URL del Apps Script.
  Causas: cada guardado reemplazaba el archivo completo, los fallos de subida eran silenciosos
  y lo local más nuevo no se volvía a subir. Corregido en v7.

## 6. Semana 2–8 nov — conclusiones

Las cifras de esa semana (FC, sueño, readiness, potencia, tests) están en el archivo privado de
Drive. Aquí solo lo que entra en la progresión:

- **Lunes 2, trote:** FC prom sobre el tope de los días suaves → **no sube velocidad**.
  Enfriamiento corto.
- **Martes 3, intervalos:** 5 series completas con RPE ≤8 → **puede avanzar**. (Creyó haber
  hecho 6: un intervalo de Garmin de 5.7 s es un LAP pulsado dos veces.)
- **Miércoles 4, pecho y abdomen:** ejercicios registrados pero **sin ninguna métrica**.
  Abdominales con pausas (no es un test limpio); push-ups por debajo del mínimo de aprobar.
- **Jueves 5, ritmo:** RPE sobre el tope de 8 → **se mantiene**.
- **Viernes 6, piernas:** RPE muy bajo y superó todo lo planificado → **esa sesión está corta,
  hay que subirla**.
- **Sábado 7, fondo + pecho corto:** FC justo sobre el tope; molestia inicial de rodilla yendo
  muy lento y con mala cadencia, que se fue después.
- **Rodilla en la semana:** la mejor racha registrada.

## 7. Pendientes

1. **Gripe del 10 al 15-nov:** no entrenó; solo quedó el lunes 9. Semana 16–22 nov cargada como
   **retorno** (~80 %): trote 20 min a 9.5, intervalos 4×400 a 12.5 (solo si el lunes FC ≤150),
   pecho sin tests, ritmo 2×1 km a 12.0, piernas con 14 kg, fondo 25 min. Si sale a RPE ≤7,
   la semana 23–29 vuelve al plan normal (5×600 a 12.8, 3×1 km a 12.5, 16 kg) con **tests el
   miércoles 25**. La semana 9–15 no cuenta para la regla 1 ni para la progresión.
1b. **Hoy 15-nov, 18:55:** primera corrida de la rutina nueva. Como la semana 16–22 ya está
   cargada, solo debe generar el PDF de la semana de gripe. Revisar que el PDF quede en Drive.
2. **Calibración de la cinta:** ya calibra antes de guardar y el total es confiable, pero el
   ritmo por intervalo que muestra Garmin sigue subestimando. Las series se miden por tiempo ×
   velocidad de banda.
3. **25 de noviembre:** decidir si se cancela Strava. Hay un recordatorio programado
   ((id en el archivo privado)). Strava no era elegible para su cuenta por despliegue
   gradual; revisar si ya lo es.
4. **Miércoles 11-nov:** primera sesión con los tests al inicio. Revisar si el pecho posterior
   aguantó el volumen o hubo que quitar una serie, y dejar los números de ese día como nueva
   línea base de push-ups y abdominales.
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
