from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

app_name = "auth"

urlpatterns = [ 
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("cadastro/", views.SignupView.as_view(), name="signup"),


]

'''path("cadastro/", views.SignupView.as_view(), name="signup"),
path("login/", views.LoginView.as_view(), name="login"),
path("logout/", views.LogoutView.as_view(),
name="logout"),'''