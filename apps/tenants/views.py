from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import TenantForm
from .models import Tenant


def is_super_admin(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(is_super_admin, login_url='login')
def tenant_list_view(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenants/tenant_list.html', {'tenants': tenants})


@user_passes_test(is_super_admin, login_url='login')
def tenant_create_view(request):
    form = TenantForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        tenant = form.save()
        password = form.get_generated_password()
        username = form.get_generated_username()
        messages.success(
            request,
            f'Tenant "{tenant.nome}" criado com sucesso!',
        )
        messages.warning(
            request,
            f'Usuário: {username} | Senha: {password} — Esta é a única vez que a senha será exibida.',
        )
        return redirect('tenant_detail', slug=tenant.slug)
    return render(request, 'tenants/tenant_form.html', {'form': form, 'is_create': True})


@user_passes_test(is_super_admin, login_url='login')
def tenant_update_view(request, slug):
    tenant = get_object_or_404(Tenant, slug=slug)
    form = TenantForm(request.POST or None, request.FILES or None, instance=tenant)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f'Tenant "{tenant.nome}" atualizado com sucesso.')
        return redirect('tenant_detail', slug=tenant.slug)
    return render(request, 'tenants/tenant_form.html', {'form': form, 'is_create': False})


@user_passes_test(is_super_admin, login_url='login')
def tenant_detail_view(request, slug):
    tenant = get_object_or_404(Tenant, slug=slug)
    users = tenant.userprofile_set.select_related('user').all()
    return render(request, 'tenants/tenant_detail.html', {'tenant': tenant, 'users': users})


@user_passes_test(is_super_admin, login_url='login')
def tenant_toggle_active_view(request, slug):
    tenant = get_object_or_404(Tenant, slug=slug)
    if request.method == 'POST':
        tenant.ativo = not tenant.ativo
        tenant.save(update_fields=['ativo'])
        status = 'ativado' if tenant.ativo else 'desativado'
        messages.success(request, f'Tenant "{tenant.nome}" foi {status}.')
    return redirect('tenant_detail', slug=tenant.slug)
