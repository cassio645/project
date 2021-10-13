from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from .models import ToDo


class TodoList(ListView):
    model = ToDo
    queryset = ToDo.objects.all()


class CreateTodo(CreateView):
    model = ToDo
    fields = ["title", "description", "done"]
    success_url = reverse_lazy('todo:list')




