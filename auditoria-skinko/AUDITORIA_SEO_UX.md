# Auditoría de SEO y experiencia de usuario: Skinko (www.skinko.com.ar)

Fecha: 7 de octubre de 2026. Fuente: Admin API de Shopify (catálogo completo, colecciones, menús, páginas, código del tema publicado "Wonder") y ShopifyQL (sesiones y ventas de los últimos 90 y 180 días).

Límites del análisis: desde este entorno no pude abrir la tienda pública (la red lo bloquea), así que no medí velocidad real ni el HTML renderizado. Los problemas del tema salen de leer el código Liquid. Semrush no tenía unidades de API disponibles, así que no hay datos de palabras clave ni de posiciones.

Archivos que acompañan este informe:
- `problemas-por-producto.csv`: los 865 productos activos con sus problemas, ordenados de más a menos problemas.
- `problemas-por-coleccion.csv`: las 165 colecciones con cantidad de productos, largo de la descripción y estado de los campos SEO.

---

## 1. Resumen ejecutivo

| # | Hallazgo | Impacto | Esfuerzo |
|---|---|---|---|
| 1 | El tema imprime un `<div>` y scripts **antes de `<html>`**. Eso cierra el `<head>` antes de tiempo, y el `<title>`, la meta description, el canonical y las etiquetas Open Graph quedan dentro del `<body>`. Google ignora el `rel=canonical` fuera del `<head>`. | Crítico (SEO de todo el sitio) | Bajo (mover 3 líneas) |
| 2 | Hay un script que **bloquea la selección de texto** en todo el sitio, así que no se pueden copiar nombres de productos, cupones ni datos. | Alto (UX, accesibilidad) | Bajo |
| 3 | En celular la conversión es de **0,94 %**, contra **2,55 %** en escritorio, y el celular trae el **92 %** del tráfico. El rebote en celular es del 60 % (34 % en escritorio). | Alto (ventas) | Medio |
| 4 | Solo el 21,5 % de las sesiones que llegan al checkout terminan comprando (septiembre). | Alto (ventas) | Medio |
| 5 | **2.985 de 2.987 imágenes** de producto no tienen texto alternativo. | Alto (SEO de imágenes, accesibilidad) | Medio (se puede hacer masivo) |
| 6 | **803 de 865 productos (93 %)** no tienen meta description. 610 tienen un título SEO de más de 60 caracteres, que Google corta. | Alto (CTR orgánico) | Medio (masivo) |
| 7 | Las descripciones de producto tienen una mediana de **37 palabras**. 719 productos tienen menos de 80. | Alto (posicionamiento sin marca) | Alto |
| 8 | El blog "Noticias" tiene **0 artículos**. 82 colecciones no tienen descripción y solo 1 supera las 50 palabras. | Alto (tráfico sin marca) | Alto |
| 9 | El producto que más facturó en el trimestre (Celimax Vita-A Retinal Shot Booster) **no tiene stock**, y su página es la segunda con más entradas del sitio. | Alto (ventas) | Bajo |
| 10 | Hay menús que llevan a colecciones vacías o casi vacías ("Correctores" tiene 0 productos y "Base" 1), y los menús de celular y escritorio no coinciden. | Medio (UX) | Bajo |

Orden de magnitud: si la conversión en celular subiera de 0,94 % a 1,2 %, serían unos 3.200 pedidos más por trimestre con el tráfico actual. Con el ticket promedio de los últimos meses (≈ $ 148.000), eso da alrededor de $ 480 millones por trimestre. Es una estimación para ordenar prioridades, no una proyección.

---

## 2. Datos de tráfico y conversión

### Embudo mensual (sesiones)

| Mes | Sesiones | Con carrito | Llegaron al checkout | Compraron | Conversión |
|---|---|---|---|---|---|
| Abr 2026 | 344.941 | 16.970 | 9.398 | 2.116 | 0,61 % |
| May 2026 | 540.562 | 92.853 | 25.571 | 5.609 | 1,04 % |
| Jun 2026 | 349.921 | 25.729 | 14.980 | 3.213 | 0,92 % |
| Jul 2026 | 413.658 | 36.666 | 24.573 | 4.943 | 1,19 % |
| Ago 2026 | 520.263 | 41.047 | 25.631 | 5.129 | 0,99 % |
| Sep 2026 | 450.606 | 38.730 | 23.718 | 5.106 | 1,13 % |

En septiembre, el 8,6 % de las sesiones agregó algo al carrito, el 61 % de esos carritos llegó al checkout y solo el 21,5 % de los checkouts se completó. El último paso es la fuga más grande. Las causas habituales son un costo de envío que aparece recién en el checkout, el precio con transferencia o las cuotas que no se ven antes, y la creación de cuenta obligatoria.

### Dispositivo (90 días)

| Dispositivo | Sesiones | Conversión | Rebote |
|---|---|---|---|
| Celular | 1.255.357 (92 %) | 0,94 % | 60 % |
| Escritorio | 107.690 | 2,55 % | 34 % |
| Tablet | 3.567 | 1,37 % | 51 % |

### Origen (90 días)

| Origen | Sesiones | Conversión | Rebote |
|---|---|---|---|
| Redes sociales | 602.901 | 0,95 % | 58 % |
| Directo | 476.157 | 1,10 % | 69 % |
| Buscadores | 274.141 | 1,26 % | 40 % |
| Email | 1.569 | 1,34 % | 55 % |
| Pago | 89 | — | — |

- Instagram trae 489.858 sesiones con una conversión de 1,13 %. TikTok trae 50.898 con 0,006 % (unas 3 compras), y Facebook 56.878 con 0,31 %.
- Solo 89 sesiones aparecen como "pago". Casi seguro las campañas de Meta no llevan parámetros UTM y caen dentro de "social". Sin eso no se puede saber qué anuncio vende.
- El 44 % de las visitas desde Google entra por la home (120.610 de 274.141). Ese patrón es típico de búsquedas de marca. Las fichas y las colecciones casi no reciben tráfico orgánico propio, y ahí está el margen de crecimiento.

### Páginas de entrada con problemas

| Página de entrada | Sesiones | Conversión | Rebote | Lectura |
|---|---|---|---|---|
| `/collections/mary-may/products/mary-may-spicule-retinol-pdrn-cream` | 51.527 | 0,01 % | 88 % | El 78 % viene de Instagram en celular. La misma ficha, abierta desde `/products/...`, convierte 0,72 %. Hoy tiene 3 unidades de stock. |
| `/products/the-vita-a-retinal-shot-tightening-booster-15ml` | 51.454 | 0,71 % | 71 % | Es el producto que más facturó en el trimestre y hoy tiene **stock 0**. |
| `/collections/celimax-1/products/the-vita-a-retinol-shot-tightening-serum-30ml` | 5.101 | 0,04 % | 86 % | Mismo patrón: URL anidada dentro de una colección, rebote altísimo. |
| `/products/dr-melaxin-cemenrete-cyano-pink-spicule-cream` (desde buscadores) | 1.100 | 0 % | 85 % | Entra por Google pero nadie compra. Conviene revisar el precio, el contenido y la intención de búsqueda. |
| `/collections/daily-comma`, `/collections/foodology` | ~5.600 / ~4.400 | 0,18 % | 66–77 % | Colecciones con tráfico y casi sin ventas. |

Acción: revisá el destino de la campaña o el link de Instagram que apunta a la URL anidada de Mary&May. Conviene que todos los anuncios apunten a `/products/handle` con UTM y que no se pauten productos con stock bajo.

---

## 3. Problemas técnicos del tema (Wonder)

### 3.1 Contenido antes de `<html>` (crítico)

Las primeras líneas de `layout/theme.liquid` son estas:

```
<!doctype html>
<script> /* tweaked by 1dcursors.tumblr.com */ ... document.onselectstart = ... return false </script>
{% render 'log-users' %}
{% render 'puzzle-popup' %}   ← imprime <div id="puzzle-popup-container"> y un <style>
<html ...>
  <head>
    <title>…</title>
    <meta name="description" …>
    <link rel="canonical" …>
```

Según las reglas de lectura de HTML, el `<div>` del puzzle abre el `<body>`. A partir de ahí, el `<html>` y el `<head>` que vienen después se ignoran, y el `<title>`, la meta description, el canonical, las etiquetas OG y Twitter y el `content_for_header` de Shopify quedan dentro del `<body>`.

- Google solo tiene en cuenta el `rel=canonical` cuando está en el `<head>`. Con los filtros, la paginación y las URLs anidadas tipo `/collections/x/products/y`, eso abre la puerta a contenido duplicado.
- Las meta descriptions y las etiquetas de redes sociales también pueden ignorarse.

**Cómo comprobarlo:** en Search Console, usá "Inspeccionar URL", después "Ver página rastreada" y "HTML", y fijate si `<link rel="canonical">` aparece dentro de `<body>`.

**Corrección:**
1. Borrá el `<script>` de 1dcursors (el bloqueo de selección y los restos del cursor con brillitos).
2. Mové `{% render 'log-users' %}` y `{% render 'puzzle-popup' %}` dentro del `<body>`, al final, junto a `skin-quiz` y `wishlist-modal`.

### 3.2 Selección de texto bloqueada en todo el sitio

`document.onselectstart = () => false` y `onmousedown = disableselect` impiden copiar texto. No protegen nada (cualquier persona copia desde el código fuente), molestan a quien quiere copiar un cupón, un nombre de producto o un dato de envío, y perjudican la accesibilidad. Hay que borrarlo.

### 3.3 Rendimiento en celular

- **Favicon:** un script borra y vuelve a crear los 3 favicons con `?v=` + la hora al cargar la página y otra vez al segundo. Así se descargan de nuevo en cada visita y se pierde la caché del navegador. Hay que borrar ese script; los `<link>` estáticos alcanzan.
- **Fuentes:** se cargan Adobe Typekit (`tqb1hbl`) y además hasta 9 `@font-face` de Shopify, con hasta 6 precargas. Conviene dejar 2 familias (títulos y texto) y una sola fuente de origen.
- **Código que se carga en todas las páginas:** `skin-quiz` (27 KB de Liquid), `puzzle-popup` (14 KB), wishlist, `log-users` y un `QQ-CustomCursor` en las fichas y colecciones. Lo ideal es cargar el quiz y el puzzle solo en sus páginas, o cuando el usuario los abre.
- Hay más de 15 scripts con `defer` en el `<head>`, además de GTM. Conviene revisar en GTM qué etiquetas siguen haciendo falta.
- Medí Core Web Vitals en PageSpeed Insights o en el informe de "Métricas web principales" de Search Console, filtrando por celular. Con un rebote del 60 % en celular, el LCP es el primer sospechoso.

### 3.4 Datos estructurados y metadatos

- El JSON-LD `Product` existe, pero le faltan `aggregateRating` y `review` (si Judge.me no los inyecta, hay que activarlo), `hasMerchantReturnPolicy`, `shippingDetails` y `priceValidUntil`. Además usa `http://schema.org`.
- No hay `BreadcrumbList` (aunque el sitio muestra migas de pan), ni `Organization`, ni `WebSite` con `SearchAction`.
- En `meta-tags.liquid`, `og:image` se arma con el prefijo `http:`. Debe ser `https:`.
- El `<title>` es solo `{{ page_title }}`. No agrega "Página 2" en la paginación ni el nombre de la tienda, así que las colecciones paginadas repiten título.
- `snippets/product-head.liquid` usa `itemprop` sin `itemscope`, así que no sirve. Además tiene un `if` vacío.

### 3.5 Texto alternativo de imágenes

Cuando una imagen no tiene `alt`, el tema usa el título del producto para todas las fotos de la galería. Es mejor que nada, pero 4 fotos con el mismo alt no aportan. Además, la imagen de "Agotado" usa `alt="Agotado"` en cada tarjeta.

---

## 4. Catálogo de productos (865 activos)

| Métrica | Valor |
|---|---|
| Sin meta description propia | 803 (93 %) |
| Sin título SEO propio | 406 (47 %) |
| Título SEO de más de 60 caracteres | 610 (mediana: 86) |
| Descripción de menos de 80 palabras | 719 (mediana: 37) |
| Descripción de 200 palabras o más | 29 |
| Imágenes sin alt | 2.985 de 2.987 |
| Productos con menos de 3 imágenes | 128 |
| Productos con video | 1 |
| Sin tipo de producto (`productType`) | 703 |
| Con un `<h1>` dentro de la descripción (queda duplicado con el H1 del tema) | 5 |
| Con "modo de uso" en la descripción | 43 |
| Con lista de ingredientes en la descripción | 47 |
| URL (handle) de más de 70 caracteres | 79 |
| Sin stock | 35 |

### 4.1 Marca (vendor) escrita de dos formas

Hay 11 marcas cargadas con dos grafías distintas, y eso divide los filtros y las búsquedas por marca:
ABIB/Abib, VT Cosmetics/Vt Cosmetics, MIXSOON/Mixsoon, BIODANCE/Biodance, EQQUALBERRY/Eqqualberry, TOCOBO/Tocobo, FWEE/Fwee, UNLEASHIA/Unleashia, ANUA/Anua, MEDICUBE/Medicube, MARY&MAY/MARYMAY.

### 4.2 Títulos

Los títulos mezclan formatos: "MARCA | Producto", "Marca Producto – Beneficio", todo en mayúsculas o con espacios dobles. Propuesta de formato único:

- **Título visible:** `Marca Nombre del producto Tamaño`, por ejemplo `Dr. Althea 345 Relief Cream 50 ml`.
- **Título SEO (50 a 60 caracteres):** `Nombre del producto: beneficio | Marca`, por ejemplo `345 Relief Cream: crema calmante con ceramidas | Dr. Althea`.
- **Meta description (140 a 155 caracteres):** beneficio, tipo de piel y condición comercial. Por ejemplo: `Crema liviana que calma y equilibra la piel sensible con pantenol y ceramidas. Original de Corea. Envío a todo el país y cuotas sin interés.`

### 4.3 Descripciones

Las fichas más vendidas tienen entre 25 y 35 palabras (345 Relief Cream: 30; PDRN Pink Collagen Capsule Cream: 34; Madeca Cream: 32; Mary&May: 25). Esta plantilla tiene la extensión que Google y quien compra esperan (250 a 400 palabras):

1. Para qué sirve, en 2 líneas, con la palabra clave principal.
2. Para qué tipo de piel es.
3. Ingredientes clave y qué hace cada uno.
4. Modo de uso: paso de la rutina, mañana o noche, cantidad.
5. Textura y terminación.
6. Preguntas frecuentes (3 o 4). Sirven para búsquedas largas y para las respuestas de IA.

Conviene cargar esto en **metafields** (ingredientes, modo de uso, tipo de piel, problemática) y no en HTML suelto. Así el tema lo muestra en pestañas, se pueden armar filtros por tipo de piel y los datos quedan estructurados.

### 4.4 Claims

Hay 4 productos que usan "trata" en la descripción: `dr-melaxin-eyephalt-eyebag-cream`, `medi-peel-bio-sun-stick-pro`, `pyunkang-yul-black-tea-time-reverse-eye-cream` y `some-by-mi-pdrn-spirulina-poreless-primer`. Para cosméticos es más prudente decir "ayuda a mejorar" o "suaviza la apariencia de".

---

## 5. Colecciones (165)

| Métrica | Valor |
|---|---|
| Sin descripción | 82 |
| Con 50 palabras o más | 1 |
| Sin título SEO | 108 |
| Sin meta description | 128 |
| Vacías (0 productos) | 11 |
| Con menos de 4 productos | 14 |
| Handle con sufijo numérico (`celimax-1`, `beauty-of-joseon-1`, `aplb-1`, `ofertas-bomba-1`, `baby-care-1`…) | 10 |

**Colecciones duplicadas**, que compiten entre sí en Google y confunden la navegación:
- `celimax` y `celimax-1` (42 productos cada una), `abib` y `abib-1`, `manyo` y `ma-nyo`, `fwee` y `fwee-1`.
- `ofertas-bomba` (20) y `ofertas-bomba-1` (4, la que figura en el menú), `pigmentacion` (77) y `pigmentacion-1` (1), `sets` / `set` / `sets-2`.
- `piel-grasa` (titulada "Piel Oleosa", 68 productos) y `piel-oleosa` (7).

Lo recomendable es quedarse con una de cada par, redirigir la otra con una redirección 301 y borrar las colecciones de prueba (`coleccion-robertito`) y las vacías que no estén en uso.

**Títulos con símbolos decorativos:** "⭒⋆ skincare para tu rutina diaria ⋆✩", "-`𖹭´- Make up para tu era glow ✧˖°" y "｡⋆ Todos los productos ⋆✴︎". Ese título se usa como H1 y como `<title>` en Google. Conviene usar títulos descriptivos ("Skincare coreano", "Maquillaje coreano") y dejar los símbolos para el diseño del banner.

Las colecciones por problema y por tipo de piel (`acne`, `rosacea`, `pigmentacion`, `piel-sensible`, `piel-grasa`, `protectores-solares`, `serums-ampoules`…) **no tienen ningún texto**. Son las páginas que mejor pueden posicionar búsquedas sin marca, como "protector solar coreano", "crema para rosácea" o "skincare coreano para piel grasa". Para cada una conviene escribir:
- Una intro de 2 o 3 líneas arriba de la grilla.
- Un bloque de 300 a 500 palabras abajo: qué buscar, ingredientes recomendados, cómo armar la rutina, y FAQ.
- Un título SEO y una meta description propios.

Los handles con `-1` se pueden renombrar a `/collections/celimax`, `/collections/beauty-of-joseon`, etc. Shopify crea la redirección 301 si tildás la opción al cambiar el handle.

---

## 6. Navegación

**Menú principal (celular y escritorio):**
- "Correctores" lleva a una colección **vacía**. "Base" (escritorio) lleva a `bases-cushions`, que tiene **1 producto**, y "Pre-bases" y "Ojos/Sombras" tienen 3 cada una. Quien entra a Makeup se encuentra con páginas casi vacías. Hay dos caminos: completar esas colecciones (como colecciones automáticas por categoría o tipo) o sacarlas del menú.
- El menú de celular y el de escritorio no tienen las mismas marcas. En celular aparecen Meditherapy, Medipeel, Torriden, Baren, Bringgreen, Fully, A by Unleashia, Men's Care y Baby care, y en escritorio no. Además, en escritorio "Base" va a `bases-cushions` y en celular a `base`.
- "Todas las marcas" lleva a tres destinos distintos: `/collections/all`, `/collections/todos-los-productos` y `/pages/marcas`. Conviene dejar uno solo: la página de marcas.
- "BB Lab" lleva a una página de resultados de búsqueda en vez de a `/collections/bblab`, que existe.
- Varios links son absolutos (`https://www.skinko.com.ar/collections/...`); deberían ser relativos.
- Los títulos de grupo usan `/` o `#` como link, lo que manda rastreos y toques a la home.
- Errores de tipeo: "Cabelllo graso", "Tipo de cabelllo", "Affiliados" (página).

**Footer:**
- "Información de envíos" y "Cambios y devoluciones" llevan a la página de FAQ general. Conviene que cada una tenga su propia página o un ancla dentro de las FAQ.
- "Seguí tu pedido" lleva al buscador genérico de OCA. Es mejor usar la página de estado del pedido de Shopify o una app de seguimiento.
- "SKINKO es una marca de Laboratorio BEK S.R.L." lleva a `/pages/skinko-club`.

**Páginas:**
- Hay páginas duplicadas: `contact` y `contacto`, `skinko-club` y `skinko-club-1`.
- La página "Quiénes somos" tiene el handle `page`. Conviene renombrarla a `quienes-somos`, con redirección.
- "Suscripción cancelada" está publicada con CSS dentro del cuerpo. Igual que Puzzles, Encuestas y Wishlist, conviene ponerle `noindex`.
- Hay solo 3 redirecciones para un catálogo de 865 productos con rotación. Revisá el informe de páginas 404 en Search Console y redirigí los productos discontinuados a su colección o a un producto equivalente.

---

## 7. Mejoras de UX para la compra en celular

En orden de impacto estimado:

1. **Fichas sin stock:** mostrar "Avisame cuando vuelva" y debajo 3 o 4 alternativas (misma marca o mismo beneficio), en vez de solo la imagen "Agotado". Lo más urgente es el Celimax Retinal Booster.
2. **Precio con transferencia y cuotas a la vista en la tarjeta y en la ficha**, no recién en el checkout. Lo mismo para el umbral de envío gratis, con la barra del carrito que ya existe en el tema (`cart-free-shipping-bar`).
3. **Botón de compra fijo en celular** (el tema tiene `enable_sticky_buy_button`; hay que confirmar que esté activo) con precio y cantidad.
4. **Galería:** al menos 4 fotos por producto (frasco, textura, uso y tamaño en mano) y video corto en los más vendidos. Hoy hay 1 solo producto con video, y el tráfico viene de Instagram y TikTok, donde el video es lo que convence.
5. **Reseñas** (Judge.me ya aparece como origen de tráfico): mostrar estrellas en la tarjeta y en la ficha, arriba del precio, y exponerlas en el JSON-LD.
6. **Filtros por tipo de piel y problemática** basados en metafields, para no depender de colecciones armadas a mano.
7. **Popups:** revisar que el quiz, el puzzle y la suscripción no se abran en la primera visita desde Instagram, donde el rebote ya es alto. Google penaliza los interstitials invasivos en celular.
8. **Checkout:** revisar que el pago como invitado esté habilitado, mostrar los costos de envío antes (calculadora en el carrito) y revisar el orden de los medios de pago.
9. **Campañas:** poner UTM en toda la pauta de Meta y TikTok, apuntar siempre a `/products/handle` y pausar los anuncios de productos con menos de 10 unidades.

---

## 8. Contenido para posicionar búsquedas sin marca

- Reactivar el blog con 2 notas por mes, pensadas para búsquedas concretas, por ejemplo: "Rutina coreana para piel grasa paso a paso", "Retinol vs. retinal: diferencias y cómo empezar", "Qué es el PDRN y para qué sirve", "Protector solar coreano: cuál elegir según tu piel", "Centella asiática: beneficios y productos". Cada nota debería enlazar a 3 o 5 productos y a su colección.
- Convertir el "ABC de K-Beauty" (glosario) en páginas por ingrediente, como `/pages/niacinamida` o `/blogs/ingredientes/niacinamida`, enlazadas desde las fichas.
- Enlaces internos: desde cada ficha, links a la colección de su problemática y a la nota del ingrediente principal.

---

## 9. Plan de acción

**Semana 1 (rápido y con mucho impacto)**
- [ ] Mover `log-users` y `puzzle-popup` dentro del `<body>` y borrar el script de 1dcursors (sección 3.1 y 3.2).
- [ ] Borrar el script que recarga el favicon.
- [ ] Corregir `og:image` a `https:`.
- [ ] Reponer el Celimax Retinal Booster, o activar el aviso de reposición y mostrar alternativas en su ficha.
- [ ] Sacar "Correctores" del menú o completar la colección; unificar los menús de celular y escritorio.
- [ ] Poner UTM en las campañas de Meta y TikTok; cambiar el destino del anuncio de Mary&May.

**Semanas 2 a 4**
- [ ] Unificar las 11 marcas con dos grafías.
- [ ] Unir las colecciones duplicadas con redirecciones 301 y quitar los símbolos de los títulos de colección.
- [ ] Cargar alt en todas las imágenes, de forma masiva, con el formato `Marca Producto, vista X`.
- [ ] Título SEO y meta description para los 100 productos que más venden, y después para el resto (masivo, con revisión).
- [ ] Completar `productType` en los 703 productos que no lo tienen.
- [ ] Texto en las 20 colecciones por problemática y tipo de piel.
- [ ] Ampliar el JSON-LD: reseñas, políticas de devolución y envío, BreadcrumbList, Organization y WebSite.

**Mes 2 y 3**
- [ ] Reescribir las descripciones de los 100 productos más vendidos con la plantilla del punto 4.3, cargada en metafields.
- [ ] Blog: 2 notas por mes.
- [ ] Optimizar las fuentes y la carga del quiz y el puzzle; medir Core Web Vitals en celular.
- [ ] Redirecciones de productos discontinuados según Search Console.

**Indicadores a seguir:** conversión en celular, porcentaje de checkouts completados, sesiones orgánicas que no entran por la home, clics e impresiones de búsquedas sin marca en Search Console, y Core Web Vitals en celular.
