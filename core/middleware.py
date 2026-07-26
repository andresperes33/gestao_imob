from django.contrib.auth import logout
from django.shortcuts import redirect


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tenant = None
        if request.user.is_authenticated:
            try:
                profile = request.user.profile
                tenant = profile.tenant
                if tenant and (not tenant.ativo or tenant.is_expired()):
                    logout(request)
                    return redirect('login')
            except Exception:
                pass
        request.tenant = tenant
        return self.get_response(request)
