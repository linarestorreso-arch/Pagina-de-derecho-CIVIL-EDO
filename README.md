# IUS EDOMEX — Proyecto de revisión

Plataforma local de estudio de Derecho Civil y Procesal Civil del Estado de México.

## Cómo abrir

1. Descomprime la carpeta completa.
2. Abre `index.html` en Chrome, Edge o Firefox. No requiere instalación ni conexión para consultar el contenido incluido.
3. Para servirlo localmente (opcional): abre una terminal en esta carpeta y ejecuta `python -m http.server 8000`; visita `http://localhost:8000`.

## Estructura

- `index.html`: estructura y navegación.
- `styles.css`: diseño visual adaptable y tema oscuro.
- `app.js`: lógica, curso, búsqueda, casos, fichas de jurisprudencia, progreso y respaldo.
- `data/codigos.js`: base legislativa que venía incrustada en el HTML original.
- `docs/`: espacio para fuentes oficiales y bitácora de actualización.

## Mejoras incorporadas

- Separación de estructura, estilos, lógica y datos.
- Interfaz renovada con navegación adaptable, panel de inicio y métricas.
- Conservación de curso, códigos, artículos enlazados, ruta procesal, práctica, tarjetas, notas, favoritos y progreso.
- Laboratorio de casos: hechos, problema jurídico, pretensiones, normas, pruebas, contraargumentos, conclusión y fuentes.
- Fichero de jurisprudencia: rubro, registro, órgano, época, tipo, hechos, problema, criterio, aplicación y fuente oficial.
- Exportación de respaldo JSON y validación básica al importar.
- Avisos de control de vigencia y accesos a portales oficiales.
- Tema claro/oscuro, responsive e impresión.

## Persistencia y privacidad

El avance se guarda en `localStorage` del navegador y equipo donde se abre. No hay servidor, cuenta ni sincronización en la nube. Usa **Exportar respaldo** para conservarlo o moverlo a otro equipo. El navegador puede borrar estos datos; no son un respaldo infalible.

## Advertencias jurídicas

La base normativa se conservó desde el archivo original. Esta entrega no certifica que los textos estén actualizados, completos, vigentes o que sus referencias sean correctas. Antes de citar una disposición o criterio en un asunto real, verifica el texto oficial, reformas, transitorios, declaratorias de entrada en vigor, ámbito temporal y criterios posteriores. La plataforma es educativa, no asesoría jurídica.

## Revisión técnica pendiente recomendada

- Validación jurídica artículo por artículo contra Gaceta del Gobierno / DOF.
- Pruebas automatizadas de referencias cruzadas, preguntas y resultados.
- Auditoría de seguridad adicional antes de publicar en internet.
- Si se requiere sincronización multi-dispositivo, diseñar autenticación y backend con reglas de acceso; no subir notas o expedientes personales a un repositorio público.

## Compatibilidad

JavaScript moderno, HTML5 y CSS. Sin dependencias externas.
