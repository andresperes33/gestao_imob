from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as AuthLoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import FirstAccessPasswordChangeForm, LoginForm


class LoginView(AuthLoginView):
    form_class = LoginForm
    template_name = 'login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.get_user()
        profile = user.profile
        if profile.tenant and (not profile.tenant.ativo or profile.tenant.is_expired()):
            form.add_error(None, 'Seu acesso expirou ou foi desativado. Entre em contato com o administrador.')
            return self.form_invalid(form)
        login(self.request, user)
        if profile.must_change_password:
            return redirect('first_access')
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('dashboard')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def first_access_view(request):
    profile = request.user.profile

    if not profile.must_change_password:
        return redirect('dashboard')

    if request.method == 'POST':
        form = FirstAccessPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            profile.must_change_password = False
            profile.save(update_fields=['must_change_password'])
            return redirect('dashboard')
    else:
        form = FirstAccessPasswordChangeForm(request.user)

    return render(request, 'first_access.html', {'form': form})


@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')
