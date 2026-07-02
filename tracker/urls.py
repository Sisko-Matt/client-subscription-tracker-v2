from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.client_list, name='client-list'),
    path('add/', views.add_client, name='add-client'),
    path('edit/<int:pk>/', views.edit_client, name='edit-client'),
    path('subscriptions/', views.subscription_list, name='subscription-list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path(
    'subscription/add/',
    views.add_subscription,
    name='add-subscription'),
    path('login/', views.login_view, name='login'),
    path(
        'export/subscriptions/',
        views.export_subscriptions_csv,
        name='export_subscriptions'
    ),
    path('logout/', views.logout_view, name='logout'),
]