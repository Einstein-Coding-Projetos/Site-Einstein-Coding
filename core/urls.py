from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('noticias/', views.noticias, name='noticias'),
    path('noticias/<int:id>/', views.news_detail, name='news_detail'),
    path('codigo-social/', views.codigo_social, name='codigo_social'), # Adicione esta linha
    path('loja/', views.codigo_loja, name='codigo_loja'),
    path('gestao/', views.gestao, name='gestao'),
    path('projetos/', views.projetos, name='projetos'),
]