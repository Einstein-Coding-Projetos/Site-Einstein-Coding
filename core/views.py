from django.shortcuts import render, get_object_or_404
from .models import News, Project, CodigoSocialCard, HealthcareJuniorCard, Product
from django.db.models import Q

def home(request):
    # Focando no "Pitch de Elevador" e Projetos, conforme solicitado.
    recent_projects = Project.objects.filter(is_active=True).order_by('-is_featured', '-created_at')[:3]
    featured_news = News.objects.filter(is_featured=True).order_by('-created_at')[:3]

    # Se quiser passar os cards da Healthcare também (mesmo que não exiba no layout "breve"), 
    # eles estão disponíveis aqui:
    healthcare_cards = HealthcareJuniorCard.objects.filter(is_active=True)

    return render(request, 'home.html', {
        'recent_projects': recent_projects,
        'featured_news': featured_news,
        'healthcare_cards': healthcare_cards 
    })

def sobre_nos(request):
    return render(request, 'sobre_nos.html')

def servicos(request):
    return render(request, 'servicos.html')

def codigo_social(request):
    # Agora puxa especificamente da tabela do Código Social
    cards = CodigoSocialCard.objects.filter(is_active=True)
    return render(request, 'codigo_social.html', {
        'cards': cards
    })

def news_detail(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'news_detail.html', {'news': news})

def projetos(request):
    projects = Project.objects.filter(is_active=True).order_by('-is_featured', '-created_at')
    query = request.GET.get('q')
    if query:
        projects = projects.filter(
            Q(title__icontains=query) |
            Q(summary__icontains=query)
        )
    return render(request, 'projetos.html', {'projects': projects})

def noticias(request):
    noticias_list = News.objects.all().order_by('-created_at')
    query = request.GET.get('q')
    if query:
        noticias_list = noticias_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
    return render(request, 'noticias.html', {'noticias': noticias_list})

def gestao(request):
    return render(request, "gestao.html")

def codigo_loja(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'loja.html', {
        'products': products
    })
