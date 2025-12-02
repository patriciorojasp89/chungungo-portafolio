USE chungungo_kanban;

-- =========================================================
-- 1. INSERT: cargar datos de ejemplo
-- =========================================================

-- 1.1. Usuarios
INSERT INTO users (username, email) VALUES
('patricio', 'patricio@example.com'),
('maria', 'maria@example.com');

-- 1.2. Tableros
INSERT INTO boards (name, description, owner_id) VALUES
('Trabajo',  'Tablero de tareas laborales', 1),
('Personal', 'Tareas personales y del hogar', 1),
('Estudio',  'Pendientes del bootcamp', 2);

-- 1.3. Columnas
INSERT INTO columns (name, position, board_id) VALUES
('Por hacer',   1, 1),
('En progreso', 2, 1),
('Completado',  3, 1),

('Por hacer',   1, 2),
('En progreso', 2, 2),
('Completado',  3, 2),

('Por hacer',   1, 3),
('En progreso', 2, 3),
('Completado',  3, 3);

-- 1.4. Etiquetas (tags)
INSERT INTO tags (name, color, owner_id) VALUES
('Urgente',     '#ff0000', 1),
('Importante',  '#ff9900', 1),
('Estudio',     '#0066ff', 2),
('Hogar',       '#00aa00', 1);

-- 1.5. Tareas
INSERT INTO tasks (title, description, priority, due_date, position, column_id) VALUES
('Preparar informe mensual',        'Informe para la jefatura',           'H', '2025-12-05', 1, 1),
('Responder correos pendientes',    'Correos a clientes importantes',     'M', '2025-12-03', 2, 1),
('Reunión con equipo',              'Planificación semanal',              'M', '2025-12-02', 1, 2),

('Pagar cuentas',                    'Luz, agua e internet',              'H', '2025-12-04', 1, 4),
('Hacer compras del mes',            'Supermercado',                      'M', '2025-12-06', 2, 4),
('Lavar el auto',                    NULL,                                 'L', NULL,         1, 5),

('Estudiar SQL',                     'Repasar joins y group by',          'H', '2025-12-01', 1, 7),
('Revisar documentación Django',     'Modelos y migraciones',             'M', '2025-12-07', 2, 7),
('Completar ejercicios bootcamp',    'Backend y frontend',                 'H', '2025-12-10', 1, 8);

-- 1.6. Relación TASK_TAGS (etiquetas asignadas a tareas)
INSERT INTO task_tags (task_id, tag_id) VALUES
(1, 1), -- Informe mensual → Urgente
(1, 2), -- Informe mensual → Importante
(2, 2), -- Correos → Importante
(4, 1), -- Pagar cuentas → Urgente
(4, 4), -- Pagar cuentas → Hogar
(7, 3), -- Estudiar SQL → Estudio
(9, 3); -- Completar bootcamp → Estudio


-- =========================================================
-- 2. UPDATE: modificaciones
-- =========================================================

-- 2.1. Cambiar descripción del tablero 1
UPDATE boards
SET description = 'Tablero principal de tareas laborales'
WHERE id = 1;

-- 2.2. Subir prioridad de una tarea (ej: tarea 2 se vuelve urgente)
UPDATE tasks
SET priority = 'H'
WHERE id = 2;

-- 2.3. Asignar fecha a tareas sin due_date
UPDATE tasks
SET due_date = '2025-12-15'
WHERE due_date IS NULL;


-- =========================================================
-- 3. DELETE: borrados con cascada
-- =========================================================

-- 3.1. Eliminar una tarea que ya no se realizará
--     También borra sus etiquetas en task_tags gracias a CASCADE.
DELETE FROM tasks
WHERE id = 6; -- "Lavar el auto"

-- 3.2. Eliminar una etiqueta que ya no se usa
DELETE FROM tags
WHERE id = 4; -- "Hogar"

-- 3.3. Eliminar un tablero completo (y sus columnas y tareas)
DELETE FROM boards
WHERE id = 2; -- Tablero "Personal"


