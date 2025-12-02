USE chungungo_kanban;

-- =========================================================
-- 1. SELECT + WHERE (consultas básicas)
-- =========================================================

-- 1.1. Obtener todos los tableros de un usuario específico
--     Ejemplo: usuario con id = 1
SELECT
    b.id,
    b.name,
    b.description
FROM boards b
WHERE b.owner_id = 1;

-- 1.2. Obtener todas las tareas de una columna específica
--     Ejemplo: columna con id = 1
SELECT
    t.id,
    t.title,
    t.priority,
    t.due_date,
    t.position
FROM tasks t
WHERE t.column_id = 1
ORDER BY t.position;

-- 1.3. Tareas con prioridad alta
SELECT
    t.id,
    t.title,
    t.priority,
    t.due_date
FROM tasks t
WHERE t.priority = 'H'
ORDER BY t.due_date;


-- =========================================================
-- 2. JOIN simples y múltiples
-- =========================================================

-- 2.1. Tareas de un tablero por su nombre
--     Ejemplo: tablero "Trabajo"
SELECT
    b.name        AS board_name,
    c.name        AS column_name,
    t.id          AS task_id,
    t.title       AS task_title,
    t.priority,
    t.due_date
FROM boards b
JOIN columns c   ON c.board_id = b.id
JOIN tasks t     ON t.column_id = c.id
WHERE b.name = 'Trabajo'
ORDER BY c.position, t.position;

-- 2.2. Tareas de un usuario, con tablero y columna
SELECT
    u.username,
    b.name      AS board_name,
    c.name      AS column_name,
    t.title     AS task_title,
    t.priority,
    t.due_date
FROM users u
JOIN boards b   ON b.owner_id = u.id
JOIN columns c  ON c.board_id = b.id
JOIN tasks t    ON t.column_id = c.id
WHERE u.username = 'patricio'
ORDER BY b.name, c.position, t.position;

-- 2.3. Tareas con sus etiquetas (JOIN + GROUP_CONCAT)
SELECT
    t.id                AS task_id,
    t.title             AS task_title,
    GROUP_CONCAT(tag.name ORDER BY tag.name SEPARATOR ', ') AS etiquetas
FROM tasks t
LEFT JOIN task_tags tt ON tt.task_id = t.id
LEFT JOIN tags tag      ON tag.id = tt.tag_id
GROUP BY t.id, t.title
ORDER BY t.id;


-- =========================================================
-- 3. Consultas con GROUP BY (estadísticas)
-- =========================================================

-- 3.1. Cantidad de tareas por prioridad dentro de un tablero
--     Ejemplo: tablero con id = 1
SELECT
    t.priority,
    COUNT(*) AS total_tareas
FROM boards b
JOIN columns c ON c.board_id = b.id
JOIN tasks t   ON t.column_id = c.id
WHERE b.id = 1
GROUP BY t.priority;

-- 3.2. Tareas por tablero de un usuario
SELECT
    u.username,
    b.name        AS board_name,
    COUNT(t.id)   AS total_tareas
FROM users u
JOIN boards b    ON b.owner_id = u.id
JOIN columns c   ON c.board_id = b.id
LEFT JOIN tasks t ON t.column_id = c.id
WHERE u.username = 'patricio'
GROUP BY u.username, b.name;

-- 3.3. Cuántas tareas tiene cada etiqueta
SELECT
    tag.name     AS etiqueta,
    COUNT(tt.task_id) AS total_tareas
FROM tags tag
LEFT JOIN task_tags tt ON tt.tag_id = tag.id
GROUP BY tag.name
ORDER BY total_tareas DESC;


-- =========================================================
-- 4. Consultas con fechas
-- =========================================================

-- 4.1. Tareas vencidas (due_date < hoy)
SELECT
    t.id,
    t.title,
    t.priority,
    t.due_date
FROM tasks t
WHERE t.due_date < CURDATE()
ORDER BY t.due_date;

-- 4.2. Tareas que vencen hoy
SELECT
    t.id,
    t.title,
    t.priority,
    t.due_date
FROM tasks t
WHERE t.due_date = CURDATE();

-- 4.3. Tareas sin fecha asignada
SELECT
    t.id,
    t.title,
    t.priority,
    t.due_date
FROM tasks t
WHERE t.due_date IS NULL;


-- =========================================================
-- 5. Consultas combinadas
-- =========================================================

-- 5.1. Tareas urgentes ordenadas por columna y tablero
SELECT
    b.name AS board,
    c.name AS column_name,
    t.title,
    t.priority,
    t.due_date
FROM boards b
JOIN columns c ON c.board_id = b.id
JOIN tasks t   ON t.column_id = c.id
WHERE t.priority = 'H'
ORDER BY b.name, c.position, t.position;

-- 5.2. Tareas de un usuario con etiqueta específica (ej: 'Estudio')
SELECT
    u.username,
    t.title,
    tag.name AS etiqueta,
    t.priority,
    t.due_date
FROM users u
JOIN boards b     ON b.owner_id = u.id
JOIN columns c    ON c.board_id = b.id
JOIN tasks t      ON t.column_id = c.id
JOIN task_tags tt ON tt.task_id = t.id
JOIN tags tag     ON tag.id = tt.tag_id
WHERE u.username = 'patricio'
  AND tag.name = 'Estudio'
ORDER BY t.due_date;


