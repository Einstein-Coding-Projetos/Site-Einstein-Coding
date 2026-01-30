from django.shortcuts import render, get_object_or_404
from .models import News
from .models import Project
from .models import CodigoSocialCard
from .models import HealthcareJuniorCard





def home(request):
    featured_news = News.objects.filter(is_featured=True).order_by('-created_at')
    latest_news = News.objects.filter(is_featured=False).order_by('-created_at')[:4]

    healthcare_cards = HealthcareJuniorCard.objects.filter(is_active=True)

    return render(request, 'home.html', {
        'featured_news': featured_news,
        'latest_news': latest_news,
        'healthcare_cards': healthcare_cards
    })



def news_detail(request, id):
    news = get_object_or_404(News, id=id)

    return render(request, 'news_detail.html', {
        'news': news
    })

def codigo_social(request):
    cards = CodigoSocialCard.objects.filter(is_active=True)

    return render(request, 'codigo_social.html', {
        'cards': cards
    })

def codigo_loja(request):
    return render(request, 'loja.html')

def gestao(request):
    return render(request, "gestao.html")

from django.db.models import Q

def projetos(request):
    projects = Project.objects.filter(is_active=True).order_by('-created_at')
    query = request.GET.get('q')
    order = request.GET.get('order')
    if query:
        projects = projects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
    if order == 'oldest':
        projects = projects.order_by('created_at')
    else:
        projects = projects.order_by('-created_at')    
    return render(request, 'projetos.html', {
        'projects': projects
    })
    
from django.db.models import Q

def noticias(request):
    noticias = News.objects.all()

    # Busca por palavra-chave
    query = request.GET.get('q')
    if query:
        noticias = noticias.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    # Ordenação
    order = request.GET.get('order')
    if order == 'antigas':
        noticias = noticias.order_by('created_at')
    else:
        noticias = noticias.order_by('-created_at')

    return render(request, 'noticias.html', {
        'noticias': noticias
    })
