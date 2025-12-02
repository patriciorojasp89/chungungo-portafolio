# Modelo Relacional – Chungungo Kanban  
Módulo 5 – SQL (Portafolio)

Este documento describe el modelo relacional diseñado para el proyecto **Chungungo Kanban**, basado directamente en los modelos del backend (`Board`, `Column`, `Tag`, `Task` y `User`). Este modelo permite administrar usuarios, tableros, columnas, tareas y etiquetas dentro de un sistema tipo Kanban.

---

## 1. Características y rol de la base de datos relacional

La aplicación utiliza una **base de datos relacional MySQL** para almacenar y organizar información. Su rol principal es:

- Almacenar datos estructurados sobre usuarios, tableros, columnas, tareas y etiquetas.
- Mantener consistencia mediante claves primarias (PK) y foráneas (FK).
- Permitir relaciones entre tablas para resolver necesidades del sistema.
- Facilitar consultas como:
  - Tareas por tablero
  - Tareas por prioridad
  - Tareas por etiqueta
  - Tableros de un usuario

---

## 2. Componentes fundamentales: tablas, campos, PK y FK

### 2.1. Tablas del sistema

El proyecto utiliza las siguientes tablas:

- **users** — información de usuarios del sistema.
- **boards** — tableros creados por cada usuario.
- **columns** — columnas dentro de un tablero.
- **tasks** — tareas que pertenecen a una columna.
- **tags** — etiquetas definidas por un usuario.
- **task_tags** — tabla intermedia para la relación tarea–etiqueta.

---

### 2.2. Registros y campos

- Un **registro** es una fila dentro de cualquier tabla (por ejemplo, una tarea).
- Un **campo** es una columna (por ejemplo, `title`, `priority`, `due_date`).

Ejemplos:

| Tabla     | Qué representa cada registro      |
|-----------|-----------------------------------|
| `users`   | Un usuario del sistema            |
| `boards`  | Un tablero Kanban                 |
| `columns` | Una etapa del tablero             |
| `tasks`   | Una tarea dentro de una columna   |
| `tags`    | Una etiqueta creada por un usuario|

---

### 2.3. Claves primarias (PK)

Cada tabla posee una clave primaria que identifica un registro de forma única:

- `users.id`
- `boards.id`
- `columns.id`
- `tasks.id`
- `tags.id`
- `task_tags.task_id` + `task_tags.tag_id` (PK compuesta)

---

### 2.4. Claves foráneas (FK)

Las FK conectan las tablas y mantienen la integridad del sistema:

| Tabla     | FK            | Referencia a  |
|-----------|---------------|---------------|
| boards    | `owner_id`    | users.id      |
| columns   | `board_id`    | boards.id     |
| tasks     | `column_id`   | columns.id    |
| tags      | `owner_id`    | users.id      |
| task_tags | `task_id`     | tasks.id      |
| task_tags | `tag_id`      | tags.id       |

---

## 3. Relaciones entre las tablas

El sistema utiliza relaciones **1:N** y **N:M**.

### ✔️ Relaciones 1 a N (uno a muchos)

- **USER 1 ─── N BOARD**  
  Un usuario puede tener varios tableros.

- **BOARD 1 ─── N COLUMN**  
  Un tablero tiene varias columnas.

- **COLUMN 1 ─── N TASK**  
  Una columna contiene múltiples tareas.

- **USER 1 ─── N TAG**  
  Cada usuario define sus propias etiquetas.

### ✔️ Relación N a M (muchos a muchos)

- **TASK N ─── M TAG**  
  Implementada con la tabla **task_tags**.

Ejemplo:  
Una tarea puede ser → “Urgente”, “Trabajo”  
Una etiqueta puede aplicarse → a varias tareas.

---

## 4. Gestión y almacenamiento de datos

Los datos se almacenan en tablas separadas y conectadas:

- Los **usuarios** administran tableros y etiquetas.
- Cada **tablero** contiene varias columnas.
- Cada **columna** contiene varias tareas.
- Las **tareas** pueden tener varias etiquetas.
- Las relaciones están aseguradas mediante claves foráneas y cascadas (`ON DELETE CASCADE`).

Esto permite consultas como:

- Tareas de un tablero  
- Tareas etiquetadas como “Urgente”  
- Número de tareas por prioridad  
- Tareas pendientes, vencidas, o sin fecha  

---

## 5. Resumen del modelo relacional

El modelo relacional de Chungungo Kanban:

- Representa entidades reales del sistema (tableros, columnas, tareas, etiquetas).
- Mantiene integridad referencial con PK y FK.
- Define relaciones 1:N y N:M.
- Permite manipular datos con DDL, DML y consultas SQL.
- Está completamente alineado con los modelos Django del proyecto original.

