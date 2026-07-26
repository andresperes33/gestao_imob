from django.contrib import admin

from .models import Tenant


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'ativo', 'data_expiracao', 'data_cadastro']
    list_filter = ['ativo']
    search_fields = ['nome', 'slug']
    prepopulated_fields = {'slug': ['nome']}
