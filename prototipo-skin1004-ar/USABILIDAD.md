# Pasada de usabilidad: destrabar el camino a la compra

Pedido del cliente: corregir el prototipo para que sea más usable e intuitivo, listo para que lo revise el brand manager. **No** se programa Liquid ni se tocan metacampos todavía: es diseño de prototipo.

Se suma a DESIGN_SYSTEM.md, VENTA.md y BRIEF.md (siguen vigentes). Sin notas de anotación dentro de las pantallas ("Referencia: …"): las explicaciones para el manager van en notas del lienzo, que escribe el coordinador.

## Los seis puntos a resolver
1. **"Agregar" no da feedback claro** (celular home y colección; también escritorio y ficha): sumar un **aviso de agregado** con "Ver carrito".
2. **El botón de menú del celular no abre nada**: diseñar el **menú desplegable** con Líneas, Rutinas y kits y Test de piel.
3. **Escritorio solo tiene home**: diseñar **ColeccionDesktop, FichaDesktop, TestDesktop y CarritoDesktop** (1440 px) y enlazar todo el escritorio entre sí.
4. **Carrito**: **barra de compra fija** al pie con total y "Iniciar compra".
5. **WhatsApp saca a la persona del sitio**: **hoja de consulta** que muestra el mensaje prearmado con el producto y el link de vuelta al carrito antes de abrir WhatsApp.
6. **Test**: mostrar el **precio del set desde el inicio** del test.

## Componentes compartidos (misma especificación en todas las pantallas)

### A. Aviso de agregado (toast)
- Aparece al tocar cualquier "Agregar" / "Agregar al carrito" que no navega. Se va solo a los 4 s (setTimeout en el handler, limpiá el timer anterior) o con su botón de cerrar.
- Ubicación: fijo arriba, debajo del header. Patrón para que funcione estático y al hacer scroll: un contenedor `position: sticky; top: 0; height: 0; z-index: 40` como primer hijo después del header, con el aviso adentro en `position: absolute; top: 8px; left: 12px; right: 12px` (escritorio: `right: 144px; width: 400px; left: auto`).
- Contenido: mini frasco o punto del color de la línea, "Agregaste Centella Ampoule" (nombre real del producto), línea chica con el total del carrito cuando es real ("Tu carrito: $ 42.999") o "Te faltan $ X para el envío gratis" si corresponde, botón principal "Ver carrito" (cápsula negra, `<a href="Carrito.dc.html">`, en escritorio CarritoDesktop.dc.html) y botón de cerrar (ícono X, `aria-label="Cerrar aviso"`).
- Fondo #FFFFFF, borde 1px #141414, radio 12, sin sombra. `role="status"` + `aria-live="polite"`.
- El botón que se tocó pasa a "Agregado" como hoy; el número del ícono del carrito sube.

### B. Menú desplegable (solo celular)
- El botón de menú (hamburguesa) abre un panel con estado `menuOpen`; el ícono pasa a X con `aria-expanded`.
- Mismo patrón sticky de altura 0 arriba del todo; el panel ocupa 390 px de ancho y el alto de su contenido, fondo #FFFFFF, filete inferior #E8E4DC, más una capa de fondo semitransparente (#141414 al 40%) que cierra al tocarla.
- Contenido en este orden:
  1. Buscador (input con label "Buscar productos").
  2. "Líneas": las seis filas con la pestaña del color de cada línea y la necesidad ("Madagascar Centella, rojeces y piel sensible"), cada una link a Coleccion.dc.html.
  3. "Rutinas y kits" (Coleccion.dc.html), "Lo más elegido" (Coleccion.dc.html), "Test de piel" (Test.dc.html) como filas grandes de 52 px.
  4. Condiciones en texto chico: envío gratis desde $ 119.999, 10% off con transferencia, 6 cuotas sin interés desde $ 150.000.
  5. "Consultanos por WhatsApp" (abre la hoja C) y "Mi cuenta".
- Filas de 48–52 px, separadas por filete, sin íconos decorativos.

### C. Hoja de consulta por WhatsApp
- Todo botón o link "Consultar por WhatsApp" / "Consultanos por WhatsApp" abre esta hoja (estado `waOpen`) en lugar de salir del sitio.
- Celular: hoja que sube desde abajo (mismo patrón sticky, pero `bottom: 0` con contenedor al final del root; si es más simple, arriba bajo el header como el toast), radio 12 arriba. Escritorio: panel de 440 px anclado arriba a la derecha bajo el header.
- Contenido:
  - Título "Consultanos por WhatsApp".
  - Burbuja con el mensaje prearmado, editable en un `<textarea>` con label "Tu mensaje": "Hola, quiero consultar por Centella Ampoule 55 ml ($ 42.999). Lo estoy viendo en la tienda oficial: [link al producto]. Mi carrito: [link al carrito]". El producto cambia según dónde se abrió (en home, el de la oferta; en ficha, el producto y tamaño elegidos).
  - Línea chica: "Te respondemos de [horario de atención]. Después volvés a tu carrito con el link del mensaje."
  - Botón principal "Abrir WhatsApp" (`<a href="https://wa.me/" target="_blank" rel="noopener">`, el número es `[número]`), secundario "Seguir en la tienda" (cierra).
- Nada de promesas de tiempo de respuesta inventadas.

### D. Barra de compra fija (carrito; ficha ya tiene una)
- Última pieza del contenido antes del pie: `position: sticky; bottom: 0; z-index: 30`, fondo #FFFFFF, filete superior #E8E4DC, padding 12px 20px.
- Carrito: "Total $ X" (Outfit 20) + "$ Y con transferencia" en verde #2F6B45 + botón "Iniciar compra" (cápsula negra 48 px). Debe mostrar los mismos valores que el resumen.
- Ficha: quitar el texto "Referencia: al bajar, esta barra queda fija al pie" y dejar la barra con el mismo patrón sticky.

### E. Escritorio
- Header igual al de HomeDesktop (links de texto, logo centrado, íconos). Navegación: Productos y Rutinas y kits → ColeccionDesktop.dc.html; Test de piel → TestDesktop.dc.html; carrito → CarritoDesktop.dc.html; productos → FichaDesktop.dc.html; logo → HomeDesktop.dc.html.
- Pie legal igual al de HomeDesktop.
- Grilla de 12 columnas, márgenes de 144 px, como HomeDesktop.

## Reglas
- Todo lo del sistema visual sigue igual (Outfit + Inter, blanco/hueso/negro, cápsulas, sin sombras, sin gradientes, sin mayúsculas salvo el logo, sin puntos medios ni flechas en botones).
- Datos: solo los reales del brief; lo demás con placeholders (`[precio]`, `[número]`, `[horario de atención]`, `[link al carrito]`…).
- Formato .dc.html: línea support.js exacta, raíz de tamaño fijo = `$preview`, holes simples, hints en sc-for/sc-if, etiquetas cerradas. Verificá con `python3 /tmp/claude-0/-home-user-diseno/55f21219-0d03-5812-b30d-aa6d30d31d14/scratchpad/check_dc.py <archivo>` (el TypeError final por `lines`/`best` se ignora).
- Accesibilidad: objetivos ≥44 px, foco visible, `aria-expanded`/`aria-pressed`/`aria-live` donde corresponde, `aria-label` en botones de ícono, contraste AA.
