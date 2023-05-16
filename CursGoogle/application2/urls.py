from django.urls import path
from . import views

urlpatterns = [
    path('', views.company_list, name='company_list'),
    path('company/add/', views.company_add, name='company_add'),
    path('company/<int:pk>/edit/', views.company_edit, name='company_edit'),
    path('company/<int:pk>/delete/', views.company_delete, name='company_delete'),
    path('company/<int:pk>/activate/', views.company_activate, name='company_activate'),
    path('company/<int:pk>/deactivate/', views.company_deactivate, name='company_deactivate'),
]
