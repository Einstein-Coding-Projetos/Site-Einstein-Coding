from django.db import models

class News(models.Model):
    title = models.CharField("Título", max_length=200)
    summary = models.TextField("Resumo", max_length=500)
    content = models.TextField("Conteúdo completo")
    image = models.ImageField("Imagem", upload_to='news/', blank=True, null=True)
    is_featured = models.BooleanField("Destaque na Home", default=False)
    
    external_link = models.URLField(
        "Link externo", 
        blank=True, 
        null=True,
        help_text="Link externo relacionado à notícia (opcional)"
    )
    
    created_at = models.DateTimeField("Data de criação", auto_now_add=True)
    updated_at = models.DateTimeField("Última atualização", auto_now=True)

    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField("Título", max_length=200)
    summary = models.TextField("Resumo")
    image = models.ImageField("Imagem", upload_to='projects/', blank=True, null=True)
    link = models.URLField("Link do Projeto", blank=True, null=True)
    created_at = models.DateTimeField("Data de criação", auto_now_add=True)
    is_active = models.BooleanField("Ativo", default=True)

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class CodigoSocialCard(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Processo Seletivo Aberto'),
        ('fechado', 'Processo Seletivo Fechado'),
    ]

    title = models.CharField("Título", max_length=100)
    description = models.TextField("Descrição")
    status = models.CharField(
        "Status",
        max_length=10,
        choices=STATUS_CHOICES,
        default='fechado'
    )

    form_link = models.URLField(
        "Link do formulário (Microsoft Forms)",
        blank=True,
        null=True
    )

    opening_date = models.CharField(
        "Data de abertura",
        max_length=50,
        blank=True,
        null=True
    )

    is_active = models.BooleanField("Ativo", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Card do Código Social"
        verbose_name_plural = "Cards do Código Social"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class HealthcareJuniorCard(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Processo Seletivo Aberto'),
        ('fechado', 'Processo Seletivo Fechado'),
    ]

    title = models.CharField("Título", max_length=100)
    description = models.TextField("Descrição")
    status = models.CharField(
        "Status",
        max_length=10,
        choices=STATUS_CHOICES,
        default='fechado'
    )

    form_link = models.URLField(
        "Link do formulário (Microsoft Forms)",
        blank=True,
        null=True
    )

    opening_date = models.CharField(
        "Data de abertura",
        max_length=50,
        blank=True,
        null=True
    )

    is_active = models.BooleanField("Ativo", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Card da Healthcare Júnior Einstein"
        verbose_name_plural = "Cards da Healthcare Júnior Einstein"
        ordering = ['-created_at']

    def __str__(self):
        return self.title