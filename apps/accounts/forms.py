from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

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


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuário ou e-mail',
        widget=forms.TextInput(attrs={
            'placeholder': 'Seu usuário ou e-mail',
            'autocomplete': 'username',
            'autofocus': True,
            'style': INPUT_STYLE,
            'onfocus': 'this.style.borderColor="#c6f91f";this.style.boxShadow="0 0 12px rgba(198,249,31,0.14)";',
            'onblur': 'this.style.borderColor="rgba(255,255,255,0.1)";this.style.boxShadow="none";',
        }),
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Sua senha',
            'autocomplete': 'current-password',
            'style': INPUT_STYLE,
            'onfocus': 'this.style.borderColor="#c6f91f";this.style.boxShadow="0 0 12px rgba(198,249,31,0.14)";',
            'onblur': 'this.style.borderColor="rgba(255,255,255,0.1)";this.style.boxShadow="none";',
        }),
    )


class FirstAccessPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Senha atual',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Senha fornecida pelo administrador',
            'autocomplete': 'current-password',
            'autofocus': True,
            'style': INPUT_STYLE,
            'onfocus': 'this.style.borderColor="#c6f91f";this.style.boxShadow="0 0 12px rgba(198,249,31,0.14)";',
            'onblur': 'this.style.borderColor="rgba(255,255,255,0.1)";this.style.boxShadow="none";',
        }),
    )
    new_password1 = forms.CharField(
        label='Nova senha',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Nova senha',
            'autocomplete': 'new-password',
            'style': INPUT_STYLE,
            'onfocus': 'this.style.borderColor="#c6f91f";this.style.boxShadow="0 0 12px rgba(198,249,31,0.14)";',
            'onblur': 'this.style.borderColor="rgba(255,255,255,0.1)";this.style.boxShadow="none";',
        }),
    )
    new_password2 = forms.CharField(
        label='Confirmar nova senha',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repita a nova senha',
            'autocomplete': 'new-password',
            'style': INPUT_STYLE,
            'onfocus': 'this.style.borderColor="#c6f91f";this.style.boxShadow="0 0 12px rgba(198,249,31,0.14)";',
            'onblur': 'this.style.borderColor="rgba(255,255,255,0.1)";this.style.boxShadow="none";',
        }),
    )
