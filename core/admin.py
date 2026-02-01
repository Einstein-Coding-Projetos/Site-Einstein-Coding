from django.contrib import admin
from .models import News, Project, CodigoSocialCard, HealthcareJuniorCard, Product


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_featured')
    search_fields = ('title', 'summary')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'summary')

@admin.register(CodigoSocialCard)
class CodigoSocialCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'is_active', 'created_at')
    list_filter = ('status', 'is_active')
    search_fields = ('title', 'description')

@admin.register(HealthcareJuniorCard)
class HealthcareJuniorCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'is_active', 'created_at')
    list_filter = ('status', 'is_active')
    search_fields = ('title', 'description')
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
