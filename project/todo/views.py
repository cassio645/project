from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import ToDo


class TodoList(ListView):
    model = ToDo
    queryset = ToDo.objects.all()


class CreateTodo(CreateView):
    model = ToDo
    fields = ["title", "description", "done"]
    success_url = reverse_lazy('todo:list')


class DetailTodo(DetailView):
    queryset = ToDo.objects.all()
    template_name = 'todo/detail.html'


class UpdateTodo(UpdateView):
    model = ToDo
    fields = ["title", "description", "done"]
    success_url = reverse_lazy('todo:list')


class DeleteTodo(DeleteView):
    queryset = ToDo.objects.all()
    success_url = reverse_lazy('todo:list')