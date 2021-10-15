from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [ 
    path("", views.TodoList.as_view(), name='list'),
    path("nova-tarefa/", views.CreateTodo.as_view(), name="create"),
    path("detalhes/<int:pk>/", views.DetailTodo.as_view(), name="detail"),
    path("editar/<int:pk>/", views.UpdateTodo.as_view(), name="edit"),
    path("deletar/<int:pk>/", views.DeleteTodo.as_view(), name="delete"),
    path("sobre/", views.About.as_view(), name="about"),
    
]