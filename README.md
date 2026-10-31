# Coach de Luis Miguel

App personal de entrenamiento: calendario de sesiones (trote, abdomen, pecho, piernas),
notas y datos del Garmin por día. Publicada como PWA instalable en GitHub Pages.

**App:** https://lsmiguel91-ui.github.io/coach/

## Instalar en Android

Abre la dirección en Chrome → menú ⋮ → **Instalar aplicación**.
Queda con ícono propio en la pantalla de inicio y abre a pantalla completa.

## Primer uso

La app pide una vez la dirección de tu Apps Script publicado. Se guarda solo
en ese dispositivo y no viaja con el código, porque este repositorio es público.
Tus notas y datos viven en Drive (`plan_entrenamiento_notas.json`), no aquí.

## Archivos

| Archivo | Para qué |
|---|---|
| `index.html` | La app completa, en un solo archivo (plan por fecha incluido) |
| `sw.js` | Service worker. El caché lleva la versión, así no se queda pegada en una anterior |
| `manifest.webmanifest` | Nombre, íconos y modo pantalla completa |

Al publicar una versión nueva hay que subir `index.html` y la constante `VERSION`
de `sw.js` en el mismo commit, para que el caché viejo se descarte.
