from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('form/receita', views.form_receita, name='form_receita'),
    path('edita/<int:receita_id>/', views.edita_receita, name='edita_receita'),
    path('atualiza_receita/', views.atualiza_receita, name='atualiza_receita'),
    path('deleta/<int:receita_id>/', views.deleta_receita, name='deleta_receita'),
    #path('login', auth_views.LoginView.as_view(template_name='login.html')),
]