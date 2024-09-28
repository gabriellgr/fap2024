from django.urls import path
from PI_SAGe import views

urlpatterns = [
    path('', views.home, name='home'),  # URL base para a página inicial
    path('gerenciar/', views.gerenciar, name='gerenciar'),
    path('sobre/', views.sobre, name='sobre'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    
]