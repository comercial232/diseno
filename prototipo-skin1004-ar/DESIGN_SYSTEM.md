# SKIN1004 Argentina: sistema de diseño "Rótulo de origen"

Referencia implementada: `project/Main.dc.html` (home celular, 390 × 7960 px). Ante cualquier duda, copiá de ahí el markup exacto.
El `BRIEF.md` sigue mandando: si algo de este documento lo contradice, gana el brief.

---

## 1. Diagnóstico: qué se leía como diseño genérico

Revisé las seis pantallas. Lo que delataba plantilla o diseño generado:

1. **La misma sección diez veces.** Main y HomeDesktop apilaban `h2 28/48 px + bajada gris + grilla` en siete bloques seguidos, alternando fondo blanco y #F7F4EE. Nada cambiaba de ritmo, escala ni composición entre "Líneas", "Más vendidos", "Rutinas", "Reseñas" y "Guías".
2. **Tarjetas de e-commerce intercambiables.** Frasco sobre beige, punto de color de 8 px, nombre, nota y precio. Era idéntica en Main, HomeDesktop y Coleccion, y no decía nada de la marca: servía igual para cualquier tienda de cosmética.
3. **El color de línea desperdiciado.** El sistema de colores del packaging (lo más propio de la marca) aparecía como un punto de 8 px o como una grilla 3 × 2 de frascos que solo cambiaban de relleno. Parecía una paleta de muestras, no una forma de navegar.
4. **Franja de confianza con cuatro íconos** ("Representante oficial", "Rótulo ANMAT", "Vegana", "Envíos"). Es el patrón genérico de cualquier tienda online.
5. **El bloque del "número gigante".** "1004" a 80/120 px con 천사 en ámbar: el recurso de número grande con etiqueta chica, que es el más trillado.
6. **Placeholders de foto por todas partes.** Main tenía siete, con leyenda incluso en miniaturas de 64 × 80 ("Foto") y de 88 × 110 ("Foto: serum solar en mano"). Además, #6B6B66 sobre #EFEAE1 da 4,47:1 y no llega a AA.
7. **Decoración que no informa.** Las tarjetas de rutina tenían barras de colores de alturas arbitrarias que parecían un gráfico sin datos.
8. **Copy de plantilla** con estructura "X, una Y": "Cada línea, una necesidad", "Tres preguntas, una rutina", "Lo que dicen quienes la usan", "Guías para tu piel", "Sumate al club".
9. **Sin jerarquía de radios.** Había 2, 4, 6, 8 y 12 px según la pantalla (opciones del test en 12, muestras del carrito en 6, colección en 4), sin relación con el nivel de cada elemento.
10. **Cromo inconsistente.** El menú tenía dos o tres barras, el trazo de los íconos era de 1,5 o 1,6, la burbuja del carrito era negra o dorada, el logo iba en 16 o 17 px, los botones en peso 500 o 600 y la barra de anuncio en 12 o 13 px. Los pies de página no coincidían: Ficha no tenía navegación y Coleccion no tenía links legales.
11. **Colores fuera de paleta.** En el resultado del test había tintes por línea (#F4ECD9, #F6E4E5, #E0ECE3, #E1EAF3) que el brief no contempla.

---

## 2. Concepto: el rótulo de origen

> **Cada producto se presenta como su rótulo de origen: primero el ingrediente, después el nombre.**
> SKIN1004 nace del 원료주의, la idea de poner el ingrediente primero, y organiza su catálogo por colores de frasco.
> La tienda toma esas dos cosas al pie de la letra. En lugar de tarjetas, los productos se muestran como rótulos de laboratorio o de herbario, con campos (ingrediente, paso, piel, contenido).
> Cada línea tiene una **pestaña de color**, como las de una farmacopea, y esa pestaña **ocupa siempre la misma posición**. Así se forma una escalera de seis colores que remite a los estratos de la tienda de SoHo.

**Por qué es de SKIN1004 y no de otra marca:**
- Sale de tres rasgos verificados de la marca: la filosofía del ingrediente primero, el color de packaging por línea y la tienda de SoHo en capas.
- Los campos del rótulo se completan con datos reales del catálogo (línea, ingrediente, paso, contenido), así que no es decoración.
- El rótulo de la marca ("Por qué se llama 1004") y el rótulo del importador (Grupo Skinfree, BEK, ANMAT) usan el mismo componente. La confianza se muestra con datos, no con íconos.
- La capa en coreano es mínima y verificable: solo el nombre coreano del producto estrella (마다가스카르 센텔라 앰플) y 천사.

**Elementos memorables (solo dos; todo lo demás queda en silencio):**
1. **El índice de líneas en pestañas escalonadas.** Es un cajón blanco sobre hueso, con seis filas. Cada fila tiene su pestaña de color en un lugar fijo (slot 0 a 5), y juntas dibujan una diagonal de colores.
2. **El rótulo del producto estrella superpuesto a la foto** en el hero. Muestra la pestaña dorada asomando sobre la imagen, los campos del rótulo y el precio argentino completo.

La superposición (una capa encima de otra) se usa **solo** en esos dos momentos y en el rótulo de la marca. No se usa en ningún otro lugar.

---

## 3. Tokens

### 3.1 Color

| Token | Hex | Rol |
|---|---|---|
| `lienzo` | #FFFFFF | Fondo por defecto de todo. Es el color que predomina. |
| `hueso-1` | #F7F4EE | Fondo del índice de líneas (el "cajón"). Como mucho, una banda por pantalla. |
| `hueso-2` | #F2EDE4 | Placeholders de foto y pie de página. |
| `escenario` | #F5F2EC | Fondo del frasco dentro de un rótulo. |
| `tinta` | #141414 | Texto principal, botón principal, barra de anuncio. |
| `tinta-2` | #4A4A46 | Texto secundario, bajadas, nombre de línea en rótulos. |
| `tinta-3` | #6B6B66 | Claves de campo, notas, leyendas. **No usar sobre #EFEAE1.** |
| `filete-1` | #E8E4DC | Separadores de sección y filas internas de campos. |
| `filete-2` | #E0DBD1 | Borde de rótulos y del cajón. |
| `filete-3` | #CFCAC0 | Bordes de inputs, estante de la rutina, chips sin elegir. |
| `oro` | #A8812F | Solo en elementos que no son texto: foco, estrellas, barras de progreso. |
| `ambar` | #8A6A24 | Hover de links y números de paso de rutina. |
| `verde-transfer` | #2F6B45 | Precio con transferencia y "Gratis" en el envío. Nada más. |

**Colores de línea.** Van solo en la pestaña, el relleno del frasco y el punto de un chip. Nunca en fondos, textos ni tintes.

| Slot | Línea | Hex | Necesidad | Ingrediente de referencia |
|---|---|---|---|---|
| 0 | Madagascar Centella | #C9A24A | Piel sensible y rojeces | Centella asiática |
| 1 | Hyalu-Cica | #4A7FB5 | Hidratación | Ácido hialurónico y centella |
| 2 | Tone Brightening | #EFEDE6 (siempre con borde rgba(20,20,20,.14)) | Manchas y tono apagado | `[ingrediente clave]` |
| 3 | Poremizing | #D98E93 | Poros y brillo | Sal rosa del Himalaya |
| 4 | Tea-Trica | #4F8A5E | Granitos | Árbol de té y centella |
| 5 | Probio-Cica | #6B4A36 | Barrera de la piel | Cica fermentada |

**Contrastes verificados (WCAG 2.1, texto normal ≥ 4,5):**

| Texto / fondo | #FFFFFF | #F7F4EE | #F2EDE4 | #F5F2EC | #EFEAE1 |
|---|---|---|---|---|---|
| #141414 | 18,42 | 16,78 | 15,80 | 16,49 | 15,38 |
| #4A4A46 | 8,90 | 8,11 | 7,63 | 7,97 | 7,43 |
| #6B6B66 | 5,36 | 4,88 | 4,59 | 4,79 | **4,47 ✗** |
| #2F6B45 | 6,34 | 5,78 | 5,44 | 5,68 | 5,30 |
| #8A6A24 | 5,04 | 4,59 | **4,32 ✗** | 4,51 | **4,21 ✗** |
| #A8812F | 3,59 ✗ | 3,27 ✗ | 3,08 ✗ | 3,21 ✗ | 3,00 ✗ |

- #F7F4EE sobre #141414 (barra de anuncio): 16,78.
- Conclusiones: los placeholders van en **#F2EDE4**, no en #EFEAE1. El ámbar nunca va sobre hueso-2. El oro nunca se usa para texto; solo cumple el 3:1 que se pide a elementos que no son texto.
- Ningún color de línea lleva texto encima: el blanco sobre #4A7FB5 da 4,2 y sobre #4F8A5E da 4,1, así que no pasan.

### 3.2 Tipografía

| Familia | Uso | Pesos |
|---|---|---|
| Outfit | Títulos, nombres de producto, precio principal, números de paso, logo | 500 (logo, números, citas), 600 (títulos) |
| Inter | Texto, menús, campos, botones, precios secundarios | 400, 500, 600 |
| Noto Sans KR | Solo 천사 y el nombre coreano del producto, con `lang="ko"` | 500 |

**Escala** (en celular la relación es de alrededor de 1,25):

| Rol | Celular | Escritorio | Interlineado | Tracking |
|---|---|---|---|---|
| Display (h1) | Outfit 600 34 | Outfit 600 64 | 1,12 / 1,06 | −0,01em |
| h2 de sección | Outfit 600 26 | Outfit 600 44 | 1,2 / 1,12 | −0,005em |
| Título de rótulo principal | Outfit 600 24 | Outfit 600 32 | 1,2 | −0,005em |
| h2 dentro de un rótulo | Outfit 600 22 | Outfit 600 28 | 1,25 | −0,005em |
| Nombre de producto (rótulo compacto) | Outfit 600 17 | Outfit 600 20 | 1,3 | 0 |
| Nombre de línea en el índice | Outfit 600 18 | Outfit 600 22 | 1,3 | 0 |
| Texto grande | Inter 400 16 | Inter 400 18 | 1,65 | 0 |
| Texto | Inter 400 14–15 | Inter 400 16 | 1,6 | 0 |
| Valor de campo | Inter 400 14 (12 en compacto) | Inter 400 15 | 1,45 | 0 |
| Clave de campo, notas, legales | Inter 500/400 12 | Inter 500/400 13 | 1,5 | 0 |
| Botón | Inter 500 15 | Inter 500 16 | 1 | 0,005em |
| Logo | Outfit 500 16 | Outfit 500 20 | 44 px de línea | **0,34em** + `margin-right: -0.34em` para compensar el centrado |
| Hangul | Noto Sans KR 500 12 (rótulo) o del mismo cuerpo que el texto que lo rodea | igual | 1,5 | 0 |

- Todo va en minúscula de oración. Solo el logo va en mayúsculas.
- Los títulos llevan `text-wrap: balance`.
- Las cifras llevan `font-variant-numeric: tabular-nums`.
- No se usan cursivas: no están cargadas y las sintéticas no se permiten.

### 3.3 Espaciado

Escala en px: **4, 8, 12, 16, 20, 24, 32, 48, 56, 64, 96, 128**

- **Celular.** Margen lateral de 24. Las secciones llevan 64 arriba y abajo. Cuando dos secciones blancas se tocan, la siguiente arranca con un filete #E8E4DC dentro del margen y 56 de aire. Entre el título y el contenido van 20–32.
- **Escritorio.** Márgenes laterales de 144. Las secciones llevan 112–128. Entre el título y el contenido van 48.
- El ritmo tiene que variar a propósito. El hero es compacto arriba y generoso abajo; el índice va en un bloque de color y las secciones de texto van con filete. No se repite el mismo par título + bajada en todas las secciones.

### 3.4 Grilla

- **Celular, 390 px:** una columna de 342 px con márgenes de 24. Las fotos van a sangre (390 de ancho) y los rótulos quedan dentro del margen. Grillas internas: rótulo compacto de 96 + 16 + 1fr, estante de rutina de 4 × 1fr, campos de 2 × 1fr con 16 de separación.
- **Escritorio, 1440 px:** 12 columnas de 74 px con separación de 24 y márgenes de 144 (1152 útiles). Las fotos del hero y del origen se extienden hasta el borde, del lado de la foto (con `margin` negativo de 144).

### 3.5 Radios (jerarquía)

| Nivel | Radio | Dónde |
|---|---|---|
| Acción | 999 px | Botones, chips, inputs, burbuja del carrito |
| Contenedor | 12 px | Rótulos y el cajón del índice |
| Contenido interno | 4 px | Escenario del frasco dentro de un rótulo, QR, fotos que no van a sangre |
| Pestaña | 4px 4px 0 0 | Pestaña de línea |
| A sangre | 0 | Fotos a sangre, barras, bandas |

No hay otros valores: nada de 2, 6 ni 8 px.

### 3.6 Bordes y elevación

- Todos los bordes son de 1 px: #E8E4DC para filetes, #E0DBD1 para contenedores y #CFCAC0 para controles y el estante.
- **No hay sombras.** La elevación se expresa superponiendo capas (margin negativo) sobre una foto o sobre hueso, nunca con `box-shadow`.

---

## 4. Componentes

Todos los snippets son compatibles con `.dc.html`: estilos inline, etiquetas cerradas, atributos entre comillas y holes simples.

### 4.1 Barra de anuncio
Tiene un solo mensaje, sin rotación ni íconos. Mide 37 px de alto.
```html
<p style="margin: 0; background: #141414; color: #F7F4EE; font-size: 12px; font-weight: 500; letter-spacing: 0.01em; padding: 10px 24px; text-align: center; line-height: 1.4">Envío gratis desde $ 119.999</p>
```
En escritorio pueden ir las tres condiciones, separadas por 88 px de aire. No se separan con puntos medios.

### 4.2 Header (celular)
Es igual en Main, Coleccion y Ficha. Test y Carrito usan una variante con cerrar o volver. El menú tiene 2 barras, el trazo es de 1,5 y la burbuja del carrito es #141414.
```html
<header style="background: #FFFFFF; display: grid; grid-template-columns: 88px minmax(0, 1fr) 88px; align-items: center; padding: 10px 14px; border-bottom: 1px solid #E8E4DC">
  <div style="display: flex">
    <button type="button" aria-label="Abrir menú" style="width: 44px; height: 44px; border: 0; background: transparent; display: flex; align-items: center; justify-content: center; cursor: pointer; padding: 0"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#141414" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M4 8h16M4 16h16"></path></svg></button>
    <button type="button" aria-label="Buscar" style="…igual…"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="#141414" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="6.5"></circle><path d="M16 16l4 4"></path></svg></button>
  </div>
  <a href="Main.dc.html" aria-label="SKIN1004, inicio" style="justify-self: center; font-family: 'Outfit', 'Helvetica Neue', Arial, sans-serif; font-weight: 500; font-size: 16px; letter-spacing: 0.34em; margin-right: -0.34em; text-decoration: none; color: #141414; line-height: 44px">SKIN1004</a>
  <div style="display: flex; justify-content: flex-end"><!-- Mi cuenta + Carrito: ver Main.dc.html líneas 33-34 --></div>
</header>
```

### 4.3 Botones
Todos son cápsula, sin sombras, sin flechas y sin íconos decorativos. El alto mínimo es 48 (44 en chips y links).
```html
<!-- Principal: una acción principal por bloque -->
<a href="Ficha.dc.html" style="display: flex; align-items: center; justify-content: center; min-height: 48px; padding: 0 24px; border-radius: 999px; background: #141414; color: #FFFFFF; text-decoration: none; font-weight: 500; font-size: 15px; letter-spacing: 0.005em">Ver la Centella Ampoule</a>
<!-- Secundario -->
<a href="Carrito.dc.html" style="display: flex; align-items: center; justify-content: center; min-height: 48px; padding: 0 24px; border-radius: 999px; border: 1px solid #141414; box-sizing: border-box; color: #141414; text-decoration: none; font-weight: 500; font-size: 15px; letter-spacing: 0.005em">Agregar al carrito</a>
<!-- Terciario (link de texto) -->
<a href="Coleccion.dc.html" style="display: inline-flex; align-items: center; min-height: 44px; font-size: 14px; font-weight: 500; text-decoration: underline; text-underline-offset: 4px; text-decoration-thickness: 1px">Ver todos los productos</a>
```
En los `<button>` se agrega `font: inherit; border: 0; cursor: pointer`. Los botones de alternar usan `aria-pressed`.

### 4.4 Pestaña de línea (la pieza base del sistema)
Es un rectángulo de 48 × 10 px, con esquinas superiores de 4 px y el color de la línea. Se apoya sobre el borde superior de su contenedor, que tiene que llevar `position: relative`.
**La posición depende de la línea**, siempre en el mismo slot:
`left = 20 + slot × (W − 88) / 5`, donde W es el ancho interior del contenedor.
Para W = 340/342 (celular) los valores son `20px, 71px, 122px, 172px, 223px, 274px`. En Main están en la constante `TAB`.
```html
<span aria-hidden="true" style="position: absolute; top: -10px; left: {{p.tab}}; width: 48px; height: 10px; box-sizing: border-box; border-radius: 4px 4px 0 0; background: {{p.c}}; border: 1px solid rgba(20,20,20,0.14); border-bottom: 0"></span>
```
- Siempre lleva `aria-hidden`, porque el nombre de la línea tiene que estar escrito como texto al lado.
- Dejá 10–12 px libres arriba del contenedor para que la pestaña no se superponga con otra cosa.

### 4.5 Chip de línea (filtros y referencias chicas)
```html
<a href="Coleccion.dc.html" aria-current="{{l.current}}" style="display: inline-flex; align-items: center; gap: 8px; min-height: 44px; padding: 0 16px; box-sizing: border-box; border-radius: 999px; border: 1px solid {{l.ring}}; background: #FFFFFF; font-size: 14px; font-weight: 500; text-decoration: none; color: #141414; white-space: nowrap"><span aria-hidden="true" style="width: 8px; height: 8px; border-radius: 999px; background: {{l.c}}; border: 1px solid rgba(20,20,20,0.14); box-sizing: border-box"></span>{{l.name}}</a>
```
- Estado activo: `border #141414`. Estado inactivo: `#CFCAC0`.
- Si el chip elige una opción (como la rutina en Main) y no lleva a otra página, va relleno: `background: #141414; color: #FFFFFF` cuando está activo.

### 4.6 Rótulo de producto (reemplaza a la tarjeta)
Hay dos tamaños. Los dos tienen la pestaña, el nombre de la línea escrito, el nombre del producto, **los campos en este orden fijo (Ingrediente, Paso, Piel, Contenido)** y el bloque de precio.

**Rótulo principal** (hero, ficha, resultado del test): los campos van en una grilla de 2 × 2 con filetes.
```html
<article aria-labelledby="hero-product" style="position: relative; background: #FFFFFF; border: 1px solid #E0DBD1; border-radius: 12px; padding: 24px 20px; display: flex; flex-direction: column">
  <span aria-hidden="true" style="position: absolute; top: -10px; left: 20px; width: 48px; height: 10px; box-sizing: border-box; border-radius: 4px 4px 0 0; background: #C9A24A; border: 1px solid rgba(20,20,20,0.14); border-bottom: 0"></span>
  <span style="font-size: 12px; font-weight: 500; line-height: 1.5; color: #4A4A46">Madagascar Centella</span>
  <h2 id="hero-product" style="margin: 6px 0 0; font-family: 'Outfit', 'Helvetica Neue', Arial, sans-serif; font-weight: 600; font-size: 24px; line-height: 1.2; letter-spacing: -0.005em">Centella Ampoule</h2>
  <span lang="ko" style="margin-top: 4px; font-family: 'Noto Sans KR', sans-serif; font-weight: 500; font-size: 12px; line-height: 1.5; color: #6B6B66">마다가스카르 센텔라 앰플</span>
  <p style="margin: 12px 0 0; font-size: 14px; line-height: 1.6; color: #4A4A46">Ampolla liviana que calma la piel sensible o con rojeces.</p>
  <dl style="margin: 20px 0 0; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); column-gap: 16px; border-top: 1px solid #E8E4DC">
    <sc-for list="{{heroFields}}" as="f" hint-placeholder-count="4">
      <div style="padding: 12px 0; border-bottom: 1px solid #E8E4DC; display: flex; flex-direction: column; gap: 2px">
        <dt style="font-size: 12px; font-weight: 500; line-height: 1.5; color: #6B6B66">{{f.k}}</dt>
        <dd style="margin: 0; font-size: 14px; line-height: 1.45; color: #141414">{{f.v}}</dd>
      </div>
    </sc-for>
  </dl>
  <!-- bloque de precio (4.7) + principal + secundario -->
</article>
```
**Rótulo compacto** (listas, colección, carrito): frasco a la izquierda en un escenario de 96 px y campos en filas de clave y valor de 64 px + 1fr. El markup exacto está en la sección "Más vendidos" de Main.
- Cuando un dato no está confirmado va como placeholder: `[ml]`, `[precio]`, `[ingrediente clave]`. **Nunca se inventa.**
- El nombre coreano solo va en el rótulo principal del producto estrella. No se traducen al coreano los nombres de los demás productos.

### 4.7 Bloque de precio argentino
El orden es fijo: precio final, precio sin impuestos nacionales, precio con transferencia y condición de cuotas.
```html
<div style="display: flex; flex-direction: column; font-variant-numeric: tabular-nums">
  <span style="font-family: 'Outfit', 'Helvetica Neue', Arial, sans-serif; font-weight: 600; font-size: 26px; line-height: 1.15">$ 42.999</span>
  <span style="margin-top: 4px; font-size: 12px; line-height: 1.5; color: #6B6B66">Precio sin impuestos nacionales: $ 35.536</span>
  <span style="margin-top: 8px; font-size: 14px; line-height: 1.5; font-weight: 500; color: #2F6B45">$ 38.699 con transferencia</span>
  <span style="margin-top: 2px; font-size: 12px; line-height: 1.5; color: #6B6B66">6 cuotas sin interés en compras desde $ 150.000</span>
</div>
```
- **Compacto:** precio en Inter 600 16 y debajo "Precio sin impuestos nacionales: …" en 12 px.
- Si el precio es placeholder, las dos líneas se muestran igual (`[precio]`), para que el diseño quede con su largo real.
- El único precio real es el de la Centella Ampoule de 55 ml.
- Las cuotas solo se muestran como condición ("en compras desde $ 150.000"). Solo se calcula el valor de la cuota cuando el total llega al mínimo, como en Carrito.

### 4.8 Placeholder de foto con dirección de arte
Va en #F2EDE4 (no #EFEAE1, porque no da contraste AA). La leyenda va **arriba a la izquierda**, para que no la tape un rótulo superpuesto, con un ícono de cámara de 16 px. Lleva `role="img"` y un `aria-label` que describe la toma.
```html
<div role="img" aria-label="Foto editorial: …" style="width: 390px; height: 488px; background: #F2EDE4; padding: 20px 24px; box-sizing: border-box; display: flex; align-items: flex-start; gap: 8px">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#6B6B66" stroke-width="1.5" stroke-linejoin="round" aria-hidden="true" style="flex: 0 0 16px; margin-top: 1px"><path d="M4 8h3l2-2.5h6L17 8h3v11H4z"></path><circle cx="12" cy="13" r="3.5"></circle></svg>
  <p style="margin: 0; max-width: 262px; font-size: 12px; line-height: 1.5; color: #6B6B66">Foto editorial: … (toma, luz, fondo, formato)</p>
</div>
```
Se permiten **como mucho 2 o 3 por pantalla**. Nunca se usan en miniaturas de menos de 120 px: en ese caso va el frasco en SVG o nada.

### 4.9 Índice de líneas (elemento memorable 1)
Es un cajón blanco (radio 12, borde #E0DBD1) sobre #F7F4EE, con seis filas. Cada fila lleva su pestaña en su slot, y la primera apoya la suya sobre el borde del cajón. A la izquierda va el nombre y la necesidad; a la derecha, el ingrediente de referencia (12 px, #6B6B66, ancho máximo de 100 px).
```html
<ul style="list-style: none; margin: 32px 0 0; padding: 0; background: #FFFFFF; border: 1px solid #E0DBD1; border-radius: 12px">
  <sc-for list="{{lines}}" as="l" hint-placeholder-count="6">
    <li style="position: relative; border-top: {{l.rule}}">
      <span aria-hidden="true" style="position: absolute; top: -10px; left: {{l.tab}}; width: 48px; height: 10px; box-sizing: border-box; border-radius: 4px 4px 0 0; background: {{l.c}}; border: 1px solid rgba(20,20,20,0.14); border-bottom: 0"></span>
      <a href="Coleccion.dc.html" style="display: grid; grid-template-columns: minmax(0, 1fr) auto; align-items: center; column-gap: 16px; padding: 20px 20px 18px; text-decoration: none; color: #141414">
        <span style="display: flex; flex-direction: column"><span style="font-family: 'Outfit', 'Helvetica Neue', Arial, sans-serif; font-weight: 600; font-size: 18px; line-height: 1.3">{{l.name}}</span><span style="margin-top: 2px; font-size: 13px; line-height: 1.5; color: #4A4A46">{{l.need}}</span></span>
        <span style="max-width: 100px; font-size: 12px; line-height: 1.45; color: #6B6B66; text-align: right">{{l.ingr}}</span>
      </a>
    </li>
  </sc-for>
</ul>
```
`rule` vale `'0'` en la primera fila y `'1px solid #E0DBD1'` en las demás.

### 4.10 Paso de rutina (estante)
Es la única lista numerada del sistema, porque la rutina coreana sí es una secuencia. Los frascos se apoyan sobre una línea de estante de 1 px #CFCAC0. Debajo va el número (Outfit 500 15 #8A6A24), el nombre corto (Inter 600 13) y el momento de uso (12 px, #6B6B66).
```html
<ol aria-label="{{routine.name}}, paso por paso" style="list-style: none; margin: 32px 0 0; padding: 0; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr))">
  <sc-for list="{{routine.steps}}" as="st" hint-placeholder-count="4">
    <li style="display: flex; flex-direction: column">
      <span style="height: 124px; display: flex; align-items: flex-end; justify-content: center; border-bottom: 1px solid #CFCAC0"><!-- sc-if por forma: ampoule, bottle, jar, tube, stick --></span>
      <span style="margin-top: 12px; padding: 0 4px; font-family: 'Outfit', 'Helvetica Neue', Arial, sans-serif; font-weight: 500; font-size: 15px; line-height: 1.3; color: #8A6A24">{{st.n}}</span>
      <span style="margin-top: 4px; padding: 0 4px; font-size: 13px; font-weight: 600; line-height: 1.35">{{st.name}}</span>
      <span style="margin-top: 4px; padding: 0 4px; font-size: 12px; line-height: 1.45; color: #6B6B66">{{st.when}}</span>
    </li>
  </sc-for>
</ol>
```
- El orden es el de aplicación: limpieza, tónico, ampolla, crema y, al final, protector solo de día. La máscara semanal va después de limpiar.
- En Ficha, el paso del producto que se está viendo se marca con el nombre en #141414 y el texto "Estás viendo este producto". **No se usa fondo de color.**

### 4.11 Reseña
No lleva foto placeholder ni estrellas llenas mientras no haya puntaje real. El puntaje va como texto.
```html
<figure style="margin: 0; padding: 24px 0; border-top: 1px solid #E8E4DC; display: flex; flex-direction: column">
  <span style="font-size: 12px; line-height: 1.5; color: #6B6B66">Puntaje: [puntaje] de 5</span>
  <blockquote style="margin: 10px 0 0; font-family: 'Outfit', 'Helvetica Neue', Arial, sans-serif; font-weight: 500; font-size: 20px; line-height: 1.4; color: #141414">[Texto de la reseña verificada]</blockquote>
  <figcaption style="margin-top: 12px; font-size: 13px; line-height: 1.5; color: #4A4A46">[Nombre], piel sensible. Compró Centella Ampoule.</figcaption>
</figure>
```
Cuando haya puntajes reales, las estrellas van en #A8812F con `role="img"` y `aria-label="4,8 de 5"`.

### 4.12 Pie legal (obligatorio y completo en **todas** las pantallas con pie)
Lleva fondo #F2EDE4 y este orden:
1. Logo y "The Untouched Nature".
2. Navegación "Comprar" y "Ayuda", con links de 44 px de alto.
3. Links legales: Términos y Política de privacidad.
4. **Botón de arrepentimiento** (secundario, a lo ancho).
5. QR de Data Fiscal (placeholder de 72 × 72, radio 4) junto a "Defensa de las y los consumidores. Para reclamos, ingresá acá."
6. Medios de pago y condiciones.
7. Razón social: Grupo Skinfree, Gurruchaga 592, CABA; importa Laboratorio BEK SRL, legajo ANMAT `[número]`; precios con IVA y precio sin impuestos nacionales.
8. Craver Corporation.

Copiá el `<footer>` completo de Main. En Test y Carrito, que no tienen pie, el botón de arrepentimiento aparece como link en el cierre (Carrito ya lo tiene).

---

## 5. Dirección de arte fotográfica

**Criterio general.** Luz natural lateral y dura, piel real con textura visible, fondos de cal o papel en tonos hueso. Tierra roja de Madagascar como único acento cálido. No hay modelos sonriendo a cámara, ni stock de spa, ni gotas de agua digitales, ni hojas volando.

| Ubicación | Toma |
|---|---|
| Main, hero (4:5 a sangre) | Retrato de perfil, piel sin maquillaje, luz de ventana lateral. Una gota de la Centella Ampoule sobre el pómulo. Pared de cal color hueso. La mitad inferior tiene que funcionar tapada por el rótulo. |
| Main, origen (390 × 320) | Planta de centella con raíces y tierra roja apoyada sobre papel de herbario. Plano cenital, luz rasante de mañana. |
| HomeDesktop, hero (6 columnas, 680 de alto) | La misma sesión que el hero de celular en formato horizontal, con el rostro en el tercio derecho. |
| HomeDesktop, origen | Plano general de un campo de centella a ras del suelo, sin personas, con la tierra roja visible. |
| Coleccion, cabecera | Por línea: el frasco de la línea sobre su material (centella: hojas frescas; Poremizing: sal rosa en piedra; Tea-Trica: hojas de árbol de té; Hyalu-Cica: vidrio con agua). Fondo hueso, sombra dura. |
| Ficha, galería | 1) El frasco en SVG sobre #F5F2EC. 2) Textura: gota sobre vidrio, contraluz. 3) Rótulo en español con BEK y el legajo legibles. 4) Aplicación: manos con luz natural. |
| Test, intro | Detalle de piel (mejilla, poros visibles) con luz de ventana, sin rostro completo. |
| Carrito | Sin fotos. |

---

## 6. Reglas de copy

- **Voz.** Rioplatense con voseo (hacé, elegí, sumate, dejanos, conocé). Nunca "che". Oraciones cortas. Nombrá las cosas por lo que hacen para quien compra.
- **Claims.** Solo "calma", "ayuda a", "acompaña", "cuida". Nunca "cura", "trata", "elimina", "antiacné" ni "clínicamente probado" sin respaldo.
- **Cifras.** No inventes precios, puntajes, reseñas, estadísticas, plazos ni cantidades: usá `[placeholder]`.
- **Títulos.** Tienen que decir algo concreto del contenido. Prohibidas las fórmulas "X, una Y" y los "Descubrí…", "Tu piel merece…", "Lo que dicen…", "Viví la experiencia…", "Sumate al club", "Cada línea, una necesidad", "Guías para tu piel".
  - Bien: "Todo empieza por la centella de Madagascar", "Tu rutina, en el orden en que se aplica", "Por qué se llama 1004", "Para leer antes de elegir".
- **CTA.** Dicen exactamente qué pasa: "Ver la Centella Ampoule", "Agregar la rutina al carrito", "Hacé el test de piel". El mismo verbo se mantiene en todo el flujo: "Agregar al carrito" lleva a "Agregado al carrito".
- **Coreano.** Solo 천사, 센텔라, 앰플 y 마다가스카르, siempre con `lang="ko"`, en Noto Sans KR y como mucho dos veces por pantalla. Nunca como decoración suelta ni en títulos.
- **Nombres de producto.** Van en inglés, como en el packaging. La descripción va en español.
- **Formato.** Nada de mayúsculas en etiquetas, eyebrows, "A · B · C", " — " con espacios, flechas en links ni emojis.

---

## 7. Movimiento

| Qué | Cómo | Dónde |
|---|---|---|
| Hover y foco en links y botones | Color u opacidad en 0,2 s ease (ya está en `<helmet>`) | Todas |
| Cambio de rutina (chips) | Cambio inmediato del estante, sin animación | Main, Ficha |
| Pestaña en hover o foco (producción) | `transform: translateY(-3px)` en 150 ms ease-out | Índice y rótulos, solo en el tema de Shopify |
| **Único momento orquestado** | Al mostrar el resultado del test, la pestaña de la línea recomendada sube de 10 a 24 px en 240 ms `cubic-bezier(.2,.7,.2,1)`, una sola vez | Test (en producción; en el prototipo el estado final es estático) |
| Nada más | No hay entradas por sección, parallax, carruseles automáticos, contadores ni sombras animadas | Todas |

Con `prefers-reduced-motion: reduce` se anulan todas las transiciones. El contenido nunca depende de una animación.

---

## 8. Checklist anti-IA (verificala antes de entregar tu pantalla)

- [ ] ¿Algún título sigue la fórmula "X, una Y" o suena a slogan que serviría para otra marca? Reescribilo.
- [ ] ¿Dos secciones seguidas tienen la misma estructura (título + bajada + grilla)? Cambiá una.
- [ ] ¿Hay fondos alternados blanco/hueso en cada sección? Solo puede haber una banda hueso por pantalla, además del pie.
- [ ] ¿Algún producto aparece como tarjeta genérica? Tiene que ser un rótulo con pestaña en su slot y campos en el orden fijo.
- [ ] ¿La pestaña de cada línea está en su slot (0 a 5) y en los mismos px que en Main?
- [ ] ¿Hay colores de línea en fondos, textos o tintes? Quitalos.
- [ ] ¿Hay más de 3 placeholders de foto, o alguno de menos de 120 px? ¿Alguno va sobre #EFEAE1?
- [ ] ¿Hay radios fuera de 999, 12, 4 o 0? ¿Sombras? ¿Gradientes?
- [ ] ¿Hay números 1, 2, 3 en algo que no sea una secuencia real (rutina, pasos del test, pasos del checkout)?
- [ ] ¿Hay íconos decorativos (franjas de beneficios con ícono, hojitas en recuadros)?
- [ ] ¿Hay mayúsculas fuera del logo, eyebrows, "·", " — ", "→" o emojis?
- [ ] ¿Hay algún número grande con etiqueta chica usado como recurso visual?
- [ ] ¿Cada precio real tiene "Precio sin impuestos nacionales" al lado? ¿Hay datos inventados?
- [ ] ¿Header y pie son idénticos a los de Main (menú de 2 barras, trazo 1,5, burbuja negra, logo 16 px 0,34em)?
- [ ] ¿Todo es táctil a 44 px o más, con `aria-label` en los botones de ícono, `<label>` en los inputs y contraste ≥ 4,5?
- [ ] ¿La audacia está en un solo lugar? Si agregaste un segundo "momento", sacá uno.

---

## 9. Dirección por pantalla

### Main (celular), implementada
- **Orden:** anuncio, header, hero (h1 + bajada + link al test, foto a sangre, rótulo de la Ampoule superpuesto 88 px), índice de líneas (cajón sobre hueso), más vendidos (3 rótulos compactos ordenados por slot, así las pestañas bajan en escalera), rutina con 4 chips (estante de 4 pasos, CTA de set y test), origen (foto a sangre + rótulo de la marca "Por qué se llama 1004" con 천사 y los datos de Skinfree, BEK y ANMAT), reseñas (2, como citas), guías (lista de texto, sin miniaturas), club, pie legal.
- **Qué se eliminó:** la franja de 4 íconos, la grilla 3 × 2 de frascos, las tarjetas de rutina con barras, el bloque "1004" gigante y cinco placeholders de foto.
- **Momento memorable:** la pestaña dorada que asoma sobre el retrato y, más abajo, la escalera de seis pestañas del índice.
- **Alto: 7960 px.**

### HomeDesktop (1440)
- **Hero:** h1 en las columnas 1–5 (64 px), bajada y link al test. La foto va en las columnas 6–12, a sangre, con 680 de alto. El rótulo principal de la Ampoule cruza de la columna 5 a la 9, superpuesto 96 px sobre el borde inferior izquierdo de la foto, con la pestaña en el slot 0 calculado con la fórmula de 4.4.
- **Índice:** el cajón en las columnas 1–8 con filas de 80 px. En las columnas 10–12 va un texto corto ("La pestaña tiene el color del frasco.") y el link a todos los productos. Las pestañas se calculan con W igual al ancho del cajón.
- **Más vendidos:** 3 rótulos compactos en vertical (escenario arriba, 4 columnas cada uno), con las pestañas en su slot.
- **Rutina:** chips y estante en las columnas 1–8, con frascos a 160 px de alto. En las columnas 10–12 va el bloque del test, con un filete a la izquierda de toda la columna. No es un borde de acento.
- **Origen:** la foto en las columnas 1–7 a sangre por la izquierda. El rótulo de la marca va en las columnas 7–12, superpuesto una columna.
- **Reseñas:** en 2 columnas. **Guías:** lista de 3 columnas, solo texto.
- **Pie:** el mismo contenido que en Main, en 12 columnas.
- **Qué se quita:** el patrón "título en las columnas 1–6 y bajada en las 8–12" repetido en cada sección, y las tres grillas de 3 tarjetas con foto.
- **Momento memorable:** la escalera de pestañas a lo ancho del cajón.

### Coleccion
- **Cabecera:** migas; debajo, la **fila de las seis pestañas** como selector de línea. La pestaña activa sube a 24 px y lleva el nombre de la línea escrito al lado; las otras quedan de 10 px, en su slot. Reemplaza al scroller de chips con puntos.
- **Luego:** h1 con la línea, rótulo corto de la línea (ingrediente, necesidad, cantidad de productos) y una foto del frasco sobre su material (4.8, una sola).
- **Grilla:** una columna de rótulos compactos (como en Main, sin repetir la pestaña, porque todos son de la misma línea). Si se prefieren 2 columnas: escenario arriba, nombre, campos de Paso y Contenido, y precio.
- **Filtros:** chips de categoría, filtrando por paso de rutina (Limpieza, Tónico, Ampolla, Crema, Protector, Kits).
- **Rutina de la línea:** el estante de 4.10.
- **Qué se elimina:** la foto con leyenda duplicada (leyenda más figcaption), el badge flotante "Más vendido" (pasa a ser un campo) y el pie sin links legales (usar el pie completo).
- **Momento memorable:** la pestaña activa que sobresale entre las seis.

### Ficha
- **Galería:** igual (4 vistas), pero las miniaturas de foto son rectángulos #F2EDE4 con el texto de la vista ("Textura", "Rótulo"), sin cámara ni el contador "1 de 4".
- **Bloque de compra:** es el **rótulo principal** completo (pestaña, línea, nombre, nombre en coreano, campos 2 × 2, precio 4.7, tamaños, cantidad, agregar, WhatsApp).
- **Acordeones:** se ordenan como un rótulo: Para qué sirve, Cómo usarla, Ingredientes (INCI `[lista]`), Tipo de piel y textura, **Rótulo en español**. Este último se presenta como una réplica del rótulo físico: un `dl` dentro de un recuadro de radio 4 con importador, legajo `[número]`, origen y contenido.
- **Completá la rutina:** el estante (4.10) con la Ampoule marcada.
- **Reseñas:** 4.11 con filtros por tipo de piel.
- **Qué se quita:** las cajas de fondo blanco con borde en cada paso de rutina y los números dorados sueltos.
- **Momento memorable:** la réplica del rótulo en español con los datos ANMAT. Es el diferencial de ser la tienda oficial.

### Test
- **Intro:** foto de detalle de piel (4.8), h1 y un solo botón principal.
- **Preguntas:** una por pantalla. El progreso es "Pregunta 2 de 3" con una barra oro de 2 px. Las opciones son **filas con filete** de 64 px como mínimo, con un radio visible de 20 px a la izquierda del texto. Se eliminan las tarjetas de radio 12.
- **Resultado:** **rótulo principal de la rutina**, con la pestaña de la línea recomendada en su slot, subida a 24 px (el único momento con movimiento del sistema). Adentro: "Según tus respuestas: …" como campo, el estante de pasos, precio del set, agregar al carrito y guardar por mail.
- **Qué se quita:** los fondos tintados por línea y el recuadro "Un consejo para tu piel" con hojita. El consejo pasa a ser un campo "Consejo" del rótulo.
- **Momento memorable:** la pestaña que sube al revelar tu línea.

### Carrito
- **Arriba:** el umbral de envío gratis con barra oro de 4 px y el umbral del regalo (`[monto]`).
- **Ítems:** rótulos compactos, cada uno con su pestaña.
- **Tu rutina en el carrito:** un estante mini de 4 pasos que muestra cuáles ya están en el carrito (frasco relleno) y cuáles faltan (contorno #CFCAC0 con el nombre del paso). El faltante tiene un CTA secundario. Reemplaza al bloque genérico "Completá tu rutina".
- **Muestras:** filas con checkbox visible, sin tarjetas de radio 6.
- **Resumen:** Subtotal, Envío, Total, Precio sin impuestos nacionales. El recuadro de transferencia y cuotas pasa a ser filas con filete, en verde solo el precio con transferencia.
- **Link de arrepentimiento** al final (ya está).
- **Momento memorable:** el estante que muestra qué paso de tu rutina falta. Es una venta cruzada honesta, basada en la secuencia real.

---

## 10. Placeholders abiertos (no inventar)
- Legajo ANMAT `[número]`.
- Precios de todo menos la Centella Ampoule de 55 ml: `[precio]`, `[precio del set]`.
- `[ml]` del Centella Toning Toner.
- `[ingrediente clave]` de Tone Brightening.
- `[puntaje]`, `[cantidad]` y textos de reseñas.
- `[beneficio de bienvenida]` del club.
- `[monto]` del regalo en el carrito.
- Tiempos de lectura de las guías (4, 5 y 6 min vienen del prototipo anterior; hay que confirmarlos).
- Los hex de las líneas son aproximados: hay que reemplazarlos por los del brand book de Craver cuando llegue.
