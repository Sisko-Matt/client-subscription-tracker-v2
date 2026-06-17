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
    path(
    'login/',
    auth_views.LoginView.as_view(
        template_name='tracker/login.html'
    ),
    name='login'
    ),

    path(
    'logout/',
    auth_views.LogoutView.as_view(),
    name='logout'
    ),
]