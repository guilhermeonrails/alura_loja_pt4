from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:receita_id>', receita, name='receita'),
    path('buscar', buscar, name='buscar'),
    path('pedir_receita', pedir_receita, name='pedir_receita'),
    path('form/receita', form_receita, name='form_receita'),
    path('edita/<int:receita_id>/', edita_receita, name='edita_receita'),
    path('atualiza_receita/', atualiza_receita, name='atualiza_receita'),
    path('deleta/<int:receita_id>/', deleta_receita, name='deleta_receita'),
]