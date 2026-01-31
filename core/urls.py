from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre-nos/', views.sobre_nos, name='sobre_nos'),
    path('servicos/', views.servicos, name='servicos'), # Nova rota
    path('projetos/', views.projetos, name='projetos'),
    path('noticias/', views.noticias, name='noticias'),
    path('noticias/<int:id>/', views.news_detail, name='news_detail'),
    path('codigo-social/', views.codigo_social, name='codigo_social'),
    path('gestao/', views.gestao, name='gestao'),
    path('loja/', views.codigo_loja, name='loja'),
]