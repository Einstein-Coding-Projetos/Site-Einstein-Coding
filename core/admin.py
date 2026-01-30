from django.contrib import admin
from .models import News
from .models import Project
from .models import CodigoSocialCard
from .models import HealthcareJuniorCard


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "is_featured", "created_at")
    search_fields = ("title", "content")

    list_filter = (
        'is_featured',
        'created_at',
    )

    search_fields = (
        'title',
        'summary',
        'content',
    )

    list_editable = (
        'is_featured',
    )

    ordering = ('-created_at',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title',)
    ordering = ('-created_at',)

@admin.register(CodigoSocialCard)
class CodigoSocialCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'is_active', 'created_at')
    list_filter = ('status', 'is_active')
    search_fields = ('title',)

@admin.register(HealthcareJuniorCard)
class HealthcareJuniorCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'is_active', 'created_at')
    list_filter = ('status', 'is_active')
    search_fields = ('title',)


