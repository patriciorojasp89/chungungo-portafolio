-- 1. Crear base de datos 
CREATE DATABASE IF NOT EXISTS chungungo_kanban
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

USE chungungo_kanban;

-- 2. Tabla USERS (versión simplificada de auth_user de Django)
CREATE TABLE users (
    id          INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username    VARCHAR(150) NOT NULL UNIQUE,
    email       VARCHAR(254) NOT NULL UNIQUE
) ENGINE=InnoDB;

-- 3. Tabla BOARDS
--   Representa los tableros Kanban de un usuario.
CREATE TABLE boards (
    id           INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name         VARCHAR(100) NOT NULL,
    description  TEXT NULL,
    owner_id     INT UNSIGNED NOT NULL,

    CONSTRAINT fk_boards_owner
        FOREIGN KEY (owner_id)
        REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 4. Tabla COLUMNS
--   Columnas dentro de cada tablero (Por hacer, En progreso, Completado, etc.).
CREATE TABLE columns (
    id         INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name       VARCHAR(100) NOT NULL,
    position   INT UNSIGNED NOT NULL,
    board_id   INT UNSIGNED NOT NULL,

    CONSTRAINT fk_columns_board
        FOREIGN KEY (board_id)
        REFERENCES boards(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 5. Tabla TAGS
--   Etiquetas definidas por el usuario (Urgente, Trabajo, Estudio, etc.).
CREATE TABLE tags (
    id         INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name       VARCHAR(100) NOT NULL,
    color      VARCHAR(20) NOT NULL,
    owner_id   INT UNSIGNED NOT NULL,

    CONSTRAINT fk_tags_owner
        FOREIGN KEY (owner_id)
        REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 6. Tabla TASKS
--   Tareas dentro de una columna (tarjetas del Kanban).
CREATE TABLE tasks (
    id          INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    title       VARCHAR(200) NOT NULL,
    description TEXT NULL,
    priority    ENUM('H', 'M', 'L') NOT NULL DEFAULT 'M',
    due_date    DATE NULL,
    position    INT UNSIGNED NOT NULL,
    column_id   INT UNSIGNED NOT NULL,

    CONSTRAINT fk_tasks_column
        FOREIGN KEY (column_id)
        REFERENCES columns(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 7. Tabla TASK_TAGS
--   Relación N:M entre TASKS y TAGS.
CREATE TABLE task_tags (
    task_id  INT UNSIGNED NOT NULL,
    tag_id   INT UNSIGNED NOT NULL,

    PRIMARY KEY (task_id, tag_id),

    CONSTRAINT fk_task_tags_task
        FOREIGN KEY (task_id)
        REFERENCES tasks(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT fk_task_tags_tag
        FOREIGN KEY (tag_id)
        REFERENCES tags(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;


