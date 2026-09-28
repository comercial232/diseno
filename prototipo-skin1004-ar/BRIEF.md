# Brief: prototipo de la tienda oficial SKIN1004 Argentina (Shopify)

Estás refinando UNA pantalla de un prototipo navegable. Cada pantalla es un archivo `.dc.html` en
`/tmp/claude-0/-home-user-diseno/55f21219-0d03-5812-b30d-aa6d30d31d14/scratchpad/proto/project/`.
Solo editás tu archivo. No publiques nada, no toques `canvas.json` ni los otros archivos.

## Contexto de negocio (datos verificados, no inventar otros)
- Marca: SKIN1004 (Craver Corporation, Seúl). "1004" se lee cheon-sa (천사) = "ángel". Eslogan: "The Untouched Nature".
  Ingrediente eje: centella asiática de Madagascar. Vegana, certificada por PETA, hipoalergénica.
- Operador: Grupo Skinfree, representante oficial en Argentina, Gurruchaga 592, CABA. Importador: Laboratorio BEK SRL (legajo ANMAT: usar placeholder [número]).
- Líneas y color de packaging: Madagascar Centella (dorado #C9A24A, piel sensible/rojeces), Hyalu-Cica (azul #4A7FB5, hidratación),
  Tone Brightening (blanco #EFEDE6, manchas/tono), Poremizing (rosa #D98E93, poros/brillo), Tea-Trica (verde #4F8A5E, granitos),
  Probio-Cica (marrón #6B4A36, barrera).
- Productos reales que podés usar: Centella Ampoule (55 ml y 100 ml), Centella Toning Toner, Centella Soothing Cream,
  Centella Light Cleansing Oil, Centella Ampoule Foam, Centella Travel Kit (5 pasos), Hyalu-Cica Water-Fit Sun Serum FPS 50+ (50 ml),
  Hyalu-Cica First Ampoule, Hyalu-Cica Moisture Cream (75 ml), Poremizing Fresh Ampoule (100 ml), Poremizing Clay Stick Mask,
  Tea-Trica Purifying Toner, Tea-Trica Relief Ampoule (100 ml), Probio-Cica Essence Toner, Tone Brightening Capsule Ampoule.
- Precios: el ÚNICO precio real es Centella Ampoule 55 ml = $ 42.999 (con transferencia 10% off = $ 38.699; sin impuestos nacionales = $ 35.536).
  Todo otro precio va como placeholder `[precio]`. Nunca inventes precios, puntajes, cantidades de reseñas ni estadísticas: usá `[placeholder]`.
- Condiciones comerciales: envío gratis desde $ 119.999; 10% off con transferencia; 6 cuotas sin interés desde $ 150.000.
- Obligatorios legales argentinos (en el pie o donde corresponda): Botón de arrepentimiento (visible), "Defensa de las y los consumidores. Para reclamos, ingresá acá.",
  QR de Data Fiscal (placeholder), "Precio sin impuestos nacionales" junto a cada precio real.
- Textos: español rioplatense con voseo, sin "che". Claims cosméticos prudentes ("calma", "ayuda a"), nunca "cura" o "trata".

## Dirección visual (pedida por el cliente, se respeta al pie de la letra)
- **Títulos**: sans-serif geométrica/humanista, bold o semibold, trazos limpios, letter-spacing sutil, terminaciones rectas → **Outfit** 600/700.
- **Texto y menús**: neo-grotesca muy legible en tamaños chicos → **Inter** 400/500/600, interlineado holgado (1.6–1.7 en párrafos).
- **Logotipo**: "SKIN1004" en mayúsculas, **tracking muy amplio** (≈0.34em), Outfit 500. Es lo único en mayúsculas.
- Hangul (천사): 'Noto Sans KR'.
- Google Fonts ya cargadas en `<helmet>`: Outfit 500/600/700, Inter 400/500/600, Noto Sans KR 500.
- **Estilo "clean beauty"**: predominio absoluto de blanco y espacio; márgenes amplios; grillas equilibradas; el contenido antes que el adorno.
- **Paleta**: lienzo #FFFFFF; hueso/beige muy tenue #F7F4EE y #F2EDE4; fondo de producto #F5F2EC; texto #141414; texto secundario #4A4A46 y #6B6B66;
  bordes #E8E4DC / #E0DBD1 / #CFCAC0. Acentos terrosos solo en detalles: dorado #A8812F (estrellas, progreso), ámbar oscuro #8A6A24 (hover), verde #2F6B45 (precio con transferencia).
  Los colores de línea aparecen solo en los frascos y en chips chicos.
- **Botones**: cápsula (border-radius 999px). Principal: relleno sólido #141414 con texto blanco. Secundario: borde fino 1px #141414. Nada de sombras.
- **Microinteracciones**: transiciones suaves (ya hay reglas en `<helmet>`: opacidad al hover en cápsulas, 0.2s ease, respeta prefers-reduced-motion). Sin efectos de entrada por sección, sin sombras pesadas.
- **Fotografía**: editorial de alto impacto (lifestyle y producto), fondos limpios, modelos con luz natural. Como no hay fotos todavía, usá **placeholders de foto** bien diseñados:
  un bloque de color hueso (#EFEAE1 / #F2EDE4) con proporción de foto real y una leyenda chica en #6B6B66 que describa la toma, por ejemplo
  "Foto editorial: modelo con luz natural aplicando la Centella Ampoule". Para producto se mantienen las ilustraciones SVG de frascos sobre #F5F2EC.
- Evitá: mayúsculas en etiquetas (salvo el logo), eyebrows sobre cada título, separadores con punto medio, flechas en botones, fuentes monoespaciadas, emojis, bordes de acento a la izquierda, gradientes.
- Accesibilidad: `<button>`, `<a href>`, `<input>`+`<label>` reales; objetivos táctiles ≥44px; contraste de texto ≥4.5:1; `aria-label` en botones de ícono.

## Reglas del formato .dc.html (si se rompen, falla en silencio)
- Mantené EXACTA la línea `<script src="./support.js"></script>` en `<head>`.
- Todo el contenido vive dentro de `<x-dc>`; `<helmet><style>` solo para bases de página y colores de `a`/`a:hover`/foco. Los estilos van inline (`style="…"`).
- El elemento raíz tiene tamaño FIJO (width/height en px) igual al `$preview` del `data-props`. Si cambiás la altura, cambiá ambos y **reportá la altura final**. Preferí que sobre un poco de alto a que se corte; el fondo del raíz es #FFFFFF.
- Cerrá todo elemento no vacío y poné comillas en todos los atributos.
- `{{hole}}` es solo una búsqueda con puntos (`{{p.name}}`), nunca una expresión. Calculá todo en `renderVals()`.
- Eventos: `onClick="{{fn}}"` con funciones devueltas por `renderVals()`. Estado: `this.state` / `this.setState`.
- Repeticiones: `<sc-for list="{{items}}" as="it" hint-placeholder-count="N">`; condicionales: `<sc-if value="{{cond}}" hint-placeholder-val="{{true}}">`.
- Links entre pantallas: `<a href="Main.dc.html">` (pantallas: Main = home celular, Coleccion, Ficha, Test, Carrito, HomeDesktop). Estilá el `<a>` como botón; no metas `<button>` dentro de `<a>`.
- Lógica: JS clásico, `class Component extends DCLogic { renderVals() {…} }`, sin imports. Nada de innerHTML ni componentes propios en window.
- Íconos: SVG inline de trazo (stroke) 1.5px, nunca emoji.
- Sin red salvo el `<link>` de Google Fonts ya presente.
- No podés renderizar el archivo; revisalo leyendo el código con cuidado (etiquetas cerradas, holes válidos, que cada `sc-for`/`sc-if` tenga sus `hint-*`).

## Qué devolver
Un resumen corto: qué cambiaste, decisiones de diseño, alto final del raíz, y cualquier dato que dejaste como placeholder.
