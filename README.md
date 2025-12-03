# Chungungo Kanban – Portafolio

Este proyecto corresponde a una versión simplificada del tablero **Chungungo Kanban**, creada específicamente para el **portafolio del curso**.  
Aquí se muestran los avances módulo a módulo utilizando HTML5, CSS3, Bootstrap, JavaScript, jQuery, Python y Django.

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
- **Python avanzado**
  - Crear un tablero desde la consola.
  - Registrar tareas con título, descripción, prioridad, horas estimadas y fecha límite.
  - Detectar automáticamente si una tarea es “grande” (≥ 8 horas).
  - Clasificar la fecha según su estado: vencida, para hoy, próximos días o futura.
  - Mostrar un resumen final con estadísticas y detalle de todas las tareas ingresadas.
- **Django**
  - Proyecto definido como modulo6
  - App principal chungungo
  - Uso del patrón MTV (Model–Template–View)
  - Modelos
  - Step: representa cada avance del portafolio (título, descripción, orden, completado).
  - Templates
  - step_list.html: muestra los pasos registrados desde la base de datos.
  - step_form.html: formulario para crear nuevos pasos.
  - login.html: autenticación para usuarios.
  - Formularios
  - StepForm basado en ModelForm para registrar nuevos pasos.
  - Autenticación y autorización
  - Login y logout con django.contrib.auth.
  - Restricción de acceso a la creación de pasos (LoginRequiredMixin).
  - Gestión de usuarios, grupos y permisos desde /admin.
  - Admin personalizado
  - Encabezados básicos para identificar el proyecto.
  - Gestión completa del modelo Step.
  - Proyecto mínimo backend dentro del portafolio
  - App principal **portafolio**
  - Uso del patrón MTV (Model–Template–View)
  - CRUD funcional del modelo Proyecto
  - Integración con base de datos SQLite mediante ORM
  - Migraciones para creación y modificación de tablas
  - Consultas ORM y SQL crudo
  - Admin con modelos registrados
-**SQL**
  - Creación del modelo relacional basado en las entidades reales del proyecto: User, Board, Column, Task,  Tag  la relación TaskTag.
  - Generación del Diagrama Entidad–Relación (ER) del tablero Kanban.
  - Script DDL para crear todas las tablas en MySQL usando claves primarias, foráneas y relaciones 1:N y N:M.
  - Script DML con ejemplos de inserción, actualización y eliminación.
  - Consultas SELECT con JOIN, WHERE, GROUP BY y filtros por fecha para obtener tareas por tablero, prioridad, etiquetas y estadísticas.
- **GitHub**:
  - Repositorio remoto para controlar versiones y registrar los avances del portafolio.

---

## Estructura del proyecto

```text
chungungo-portafolio/
│
├─ index.html                           # Página principal       Módulo 2
├─ css/
│   └─ styles.css                       # Estilos adicionales    Módulo 2
├─ js/
│   └─ script.js                        # Lógica con JS + jQuery Módulo 2
│
├─ python/
│   ├─ conversor_tiempo_tareas.py       # Script del Módulo 3 (Python)
│   ├─ tablero.py                       # Script del Módulo 4 (Python avanzado)
│   └─ python/django/modulo6/           # Script del Módulo 6 (Django)
│       │
│       ├─ manage.py
│       │
│       ├─ modulo6/                     # Proyecto Django (Módulo 6 )
│       │   ├─ settings.py
│       │   ├─ urls.py
│       │   └─ wsgi.py
│       │
│       ├─ chungungo/                   # App principal (Módulo 6)
│       │   ├─ models.py                # Modelo Step
│       │   ├─ forms.py                 # Formulario StepForm
│       │   ├─ views.py                 # ListView + CreateView
│       │   ├─ urls.py                  # Rutas de la app
│       │   └─ admin.py                 # Administración del modelo Step
│       │
│       ├─ templates/
│       │   ├─ chungungo/
│       │   │   ├─ step_list.html       # Lista de pasos
│       │   │   └─ step_form.html       # Formulario
│       │   └─ registrations/
│       │       └─ login.html           # Autenticación
│       │
│       └─ admin_usuarios_permisos.md   # Gestión de grupos, permisos y usuarios
│
│
├─ backend/                             # Backend Django Módulo 7
│   ├─ settings.py
│   ├─ urls.py
│   └─ wsgi.py
│
├─ portafolio/                          # App Django minimalista
│   ├─ models.py                        # Modelos + relaciones
│   ├─ forms.py                         # Formulario ProyectoForm
│   ├─ views.py                         # CRUD Proyecto
│   ├─ urls.py                          # Rutas CRUD
│   ├─ admin.py                         # Modelos registrados
│   ├─ queries_example.py               # ORM + SQL crudo
│   └─ templates/portafolio/
│       ├─ lista_proyectos.html
│       ├─ crear_proyecto.html
│       ├─ editar_proyecto.html
│       └─ confirmar_eliminar_proyecto.html
│
│
├─ sql/                                  # Script del Módulo 5 (Bases de datos)
│    ├─ modelo_relacional.md
│    ├─ ddl_creacion_tablas.sql
│    ├─ dml_ejemplos.sql
│    ├─ consultas_select.sql
│    └─ diagrama_er.png
│
└─ README.md
