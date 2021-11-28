from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from todo.api.viewsets import TodoApiView

router = routers.DefaultRouter()
router.register("", TodoApiView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/',include(router.urls)),
]
