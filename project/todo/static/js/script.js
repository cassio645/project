function editFunction(todo_id) {
    location.replace("/editar/"+ todo_id)
  }

function deleteFunction(id, title) {
  var r = confirm(`Tem certeza que deseja apagar a tarefa\n "${title}"?`);
  if (r == true) {
    location.replace("/deletar/" + id);
  }
}

