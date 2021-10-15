from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import ToDo


@method_decorator(login_required, name='dispatch')
class TodoList(ListView):
    model = ToDo
    context_object_name = 'list_todo'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_todo'] = context['list_todo'].filter(user=self.request.user)
        return context


@method_decorator(login_required, name='dispatch')
class CreateTodo(CreateView):
    model = ToDo
    fields = ['title', 'description', 'done']
    success_url = reverse_lazy('todo:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTodo, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class DetailTodo(DetailView):
    queryset = ToDo.objects.all()
    template_name = 'todo/detail.html'


@method_decorator(login_required, name='dispatch')
class UpdateTodo(UpdateView):
    model = ToDo
    fields = ["title", "description", "done"]
    success_url = reverse_lazy('todo:list')


@method_decorator(login_required, name='dispatch')
class DeleteTodo(DeleteView):
    queryset = ToDo.objects.all()
    success_url = reverse_lazy('todo:list')