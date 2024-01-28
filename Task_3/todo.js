const todoList = document.querySelector('.todo-list');
const todoInput = document.getElementById('todo-input');

function addTodo() {
  const todoText = todoInput.value.trim();
  if (todoText !== '') {
    const todoItem = document.createElement('li');
    todoItem.className = 'todo-item';
    todoItem.innerHTML = `
      <input type="checkbox">
      <span>${todoText}</span>
      <button class="delete-btn" onclick="deleteTodo(this)"><i class="fas fa-trash-alt"></i></button>
    `;
    todoList.appendChild(todoItem);
    todoInput.value = '';
  }
}

function deleteTodo(btn) {
  const todoItem = btn.parentNode;
  todoItem.classList.add('deleted');
  setTimeout(() => {
    todoList.removeChild(todoItem);
  }, 500);
}

todoInput.addEventListener('keyup', function (event) {
  if (event.key === 'Enter') {
    addTodo();
  }
});