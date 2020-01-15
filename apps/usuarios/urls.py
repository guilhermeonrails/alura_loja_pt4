from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard')
    #path('login', auth_views.LoginView.as_view(template_name='login.html')),
]