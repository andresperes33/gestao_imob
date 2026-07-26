from django.urls import path

from . import views

urlpatterns = [
    path('', views.tenant_list_view, name='tenant_list'),
    path('create/', views.tenant_create_view, name='tenant_create'),
    path('<slug:slug>/', views.tenant_detail_view, name='tenant_detail'),
    path('<slug:slug>/edit/', views.tenant_update_view, name='tenant_update'),
    path('<slug:slug>/toggle/', views.tenant_toggle_active_view, name='tenant_toggle'),
]
