from django.urls import path, include  
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("home", include("home.urls")),
]