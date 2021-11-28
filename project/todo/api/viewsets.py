from rest_framework import viewsets
from todo.models import ToDo
from .serializer import ToDoSerializer


class TodoApiView(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer