from django.db import models


class News(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Título"
    )

    summary = models.TextField(
        max_length=500,
        verbose_name="Resumo"
    )

    content = models.TextField(
        verbose_name="Conteúdo completo"
    )

    image = models.ImageField(
        upload_to='news/',
        blank=True,
        null=True,
        verbose_name="Imagem da notícia"
    )
    
    is_featured = models.BooleanField(
        default=False,
        verbose_name="Destaque na Home"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de criação"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Última atualização"
    )

    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

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


from django.db import models

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

class News(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    
    external_link = models.URLField(
        blank=True,
        null=True,
        help_text="Link externo relacionado à notícia (opcional)"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title