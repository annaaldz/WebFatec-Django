from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendario_geral, name='home'),  
    path('calendario/', views.calendario_geral, name='calendario_geral'),
    path('calendario_filtrado/', views.calendario_filtrado, name='calendario_filtrado'),
    path('atualizar_aulas/', views.atualizar_aulas, name='atualizar_aulas'),
]