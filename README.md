# Chungungo Kanban – Portafolio

Este proyecto corresponde a una versión simplificada del tablero **Chungungo Kanban**, creada específicamente para el **portafolio del curso**.  
Aquí se muestran los avances módulo a módulo utilizando HTML5, CSS3, Bootstrap, JavaScript, jQuery y python.

## Objetivo

Construir un sitio web básico y responsivo que represente un tablero Kanban con tres columnas:

- **Por hacer**
- **En progreso**
- **Completado**

A medida que avance el curso, se irán incorporando más funcionalidades sobre esta base.

---

## Tecnologías utilizadas

- **HTML5**: estructura semántica de la página (header, nav, main, sections, footer).
- **CSS3**: ajustes mínimos de estilo para complementar Bootstrap.
- **Bootstrap 5** (CDN):  
  - Navbar responsivo.  
  - Sistema de grillas (`container`, `row`, `col-12`, `col-md-4`).  
  - Cards para las columnas del tablero.
- **JavaScript** :
  - Manejo de eventos con `addEventListener`.
  - Creación y agregado dinámico de elementos al DOM.
- **jQuery**:
  - Manejo de eventos con `$(...).on(...)`.
  - Modificación dinámica de clases con `toggleClass` sobre componentes Bootstrap.
- **Python**:
  - Variables, tipos de datos, operadores.
  - Condicionales if / elif / else.
  - Bucles for y while.
  - Estructuras de datos (listas, diccionarios, tuplas).
  - Funciones para modularizar el código.
  - Programa de consola integrado al portafolio.
- **GitHub**:
  - Repositorio remoto para controlar versiones y registrar los avances del portafolio.

---

## Estructura del proyecto

```text
chungungo-portafolio/
│
├─ index.html                      # Página principal
├─ css/
│   └─ styles.css                  # Estilos adicionales
├─ js/
│   └─ script.js                   # Lógica con JS + jQuery
├─ python/
│   └─ gestor_tareas.py            # Script del Módulo 3 (Python)
└─ README.md                       # Documentación del proyecto

