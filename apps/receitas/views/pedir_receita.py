from django.shortcuts import render, get_object_or_404, redirect
from receitas.models.receita import Receita
from receitas.models.forms import PedirReceitaForms
from receitas.models.pedir_receita import PedirReceita
from django.contrib import messages
from django.contrib.auth.models import User

def pedir_receita(request):
    if request.method == 'POST':
        form = PedirReceitaForms(request.POST)
        if form.is_valid():
            pedir_receita = form.save(commit=False)
            pedir_receita.pessoa = get_object_or_404(User, pk=request.user.id)
            pedir_receita.save()
            messages.success(request, 'Pedido cadastrado com sucesso')
            receitas = Receita.objects.filter(pessoa=request.user.id)
            dados = {'receitas' : receitas}
            return render(request, 'usuarios/dashboard.html', dados)
    else:
        form = PedirReceitaForms()
    return render(request, 'receitas/pedir_receita.html', {'form': form})
           