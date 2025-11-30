// JS puro: agregar tareas de ejemplo a la columna "Por hacer"
document.addEventListener("DOMContentLoaded", () => {
  const btnAdd = document.getElementById("btn-add-task");
  const todoList = document.getElementById("todo-list");

  if (btnAdd && todoList) {
    let contador = 1;

    btnAdd.addEventListener("click", () => {
      const li = document.createElement("li");
      li.textContent = `Tarea nueva #${contador}`;
      li.className = "small";
      todoList.appendChild(li);
      contador++;
    });
  }
});

// jQuery: resaltar la columna "En progreso" al hacer clic
$(function () {
  $("#progress-card").on("click", function () {
    $(this).toggleClass("border border-warning");
  });
});
