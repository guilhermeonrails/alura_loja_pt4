from django import forms
from receitas.models.pedir_receita import PedirReceita

class PedirReceitaForms(forms.ModelForm):  
    class Meta:
        model = PedirReceita
        fields = ('nome_receita', 'categoria',)
        labels = {
            'nome_receita': 'Digite por favor o nome da receita',
            'categoria': 'Qual a categoria dessa receita?',
        }
    def clean_nome_receita(self):
        nome_receita = self.cleaned_data.get('nome_receita')
        if 'receita' in nome_receita:
            raise forms.ValidationError('Não inclua a palavra receita no nome da receita')
        if any(char.isdigit() for char in nome_receita):
            raise forms.ValidationError('Não inclua números no nome da receita')
        return nome_receita
            