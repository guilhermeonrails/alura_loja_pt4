from django import forms
from .models_pedir_receita import PedirReceita

class PedirReceitaForms(forms.ModelForm):  
    class Meta:
        model = PedirReceita
        fields = ('nome_receita', 'categoria',)
        labels = {
            'nome_receita': 'Digite por favor o nome da receita',
            'categoria': 'Qual a categoria dessa receita?',
        }