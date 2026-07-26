from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Tenant(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug')
    logo = models.ImageField(upload_to='tenants/logos/', blank=True, null=True, verbose_name='Logo')
    cor_primaria = models.CharField(max_length=7, default='#1d4ed8', verbose_name='Cor primária')
    cor_secundaria = models.CharField(max_length=7, default='#f59e0b', verbose_name='Cor secundária')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    data_expiracao = models.DateField(blank=True, null=True, verbose_name='Data de expiração')
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='tenants_criados', verbose_name='Criado por',
    )
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro')

    class Meta:
        verbose_name = 'Tenant'
        verbose_name_plural = 'Tenants'
        ordering = ['-data_cadastro']

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.nome)
            slug = base
            counter = 1
            while Tenant.objects.filter(slug=slug).exists():
                slug = f'{base}-{counter}'
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def is_expired(self):
        from datetime import date
        if self.data_expiracao and self.data_expiracao < date.today():
            return True
        return False
