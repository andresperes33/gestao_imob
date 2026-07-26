import secrets

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Tenant

INPUT_STYLE = (
    'background:rgba(255,255,255,0.05);'
    'border:1px solid rgba(255,255,255,0.1);'
    'border-radius:0.375rem;'
    'padding:0.625rem 0.875rem;'
    'color:#ffffff;'
    'font-family:\'Geist\',sans-serif;'
    'font-size:0.875rem;'
    'outline:none;'
    'width:100%;'
    'transition:border-color 0.2s, box-shadow 0.2s;'
)


class TenantForm(forms.ModelForm):
    usuario_email = forms.EmailField(
        label='E-mail do usuário',
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'email@corretor.com',
            'style': INPUT_STYLE,
        }),
    )
    usuario_nome = forms.CharField(
        label='Nome completo do usuário',
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nome do corretor',
            'style': INPUT_STYLE,
        }),
    )

    class Meta:
        model = Tenant
        fields = ['nome', 'slug', 'logo', 'cor_primaria', 'cor_secundaria', 'data_expiracao']
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Ex: Imobiliária ABC',
                'style': INPUT_STYLE,
            }),
            'slug': forms.TextInput(attrs={
                'placeholder': 'exemplo-abc',
                'style': INPUT_STYLE,
            }),
            'cor_primaria': forms.TextInput(attrs={
                'type': 'color',
                'style': 'width:60px;height:40px;padding:2px;border:1px solid rgba(255,255,255,0.1);border-radius:0.375rem;background:transparent;cursor:pointer;',
            }),
            'cor_secundaria': forms.TextInput(attrs={
                'type': 'color',
                'style': 'width:60px;height:40px;padding:2px;border:1px solid rgba(255,255,255,0.1);border-radius:0.375rem;background:transparent;cursor:pointer;',
            }),
            'data_expiracao': forms.DateInput(attrs={
                'type': 'date',
                'style': INPUT_STYLE,
            }),
        }
        labels = {
            'nome': 'Nome do tenant',
            'slug': 'Slug (URL amigável)',
            'logo': 'Logo do tenant',
            'cor_primaria': 'Cor primária',
            'cor_secundaria': 'Cor secundária',
            'data_expiracao': 'Data de expiração (deixe vazio para sem expiração)',
        }
        help_texts = {
            'slug': 'Usado na URL pública: /slug/',
        }

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        qs = Tenant.objects.filter(slug=slug)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError('Este slug já está em uso.')
        return slug

    def generate_password(self):
        return secrets.token_urlsafe(12)

    def save(self, commit=True):
        tenant = super().save(commit=False)
        created = not self.instance.pk

        if commit:
            tenant.save()
            self._save_m2m()

        if created:
            raw_password = self.generate_password()
            username = self.cleaned_data['slug'].replace('-', '_')
            nome = self.cleaned_data['usuario_nome'].strip().split(' ', 1)
            first_name = nome[0] if nome else ''
            last_name = nome[1] if len(nome) > 1 else ''
            user = User.objects.create_user(
                username=username,
                email=self.cleaned_data['usuario_email'],
                first_name=first_name,
                last_name=last_name,
                password=raw_password,
            )
            profile = user.profile
            profile.is_tenant = True
            profile.must_change_password = True
            profile.tenant = tenant
            profile.save()
            # store generated password for the flash message
            self._generated_password = raw_password
            self._generated_username = username

        return tenant

    def get_generated_password(self):
        return getattr(self, '_generated_password', None)

    def get_generated_username(self):
        return getattr(self, '_generated_username', None)
