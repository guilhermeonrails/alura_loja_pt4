from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita
from .forms import PedirReceitaForms
from .models_pedir_receita import PedirReceita
from django.contrib import messages
from django.contrib.auth.models import User

def index(request):
    receitas = Receita.objects.order_by('-nome_receita').filter(publicada=True)

    dados = {
        'receitas' : receitas
    }
    return render(request,'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita' : receita
    }

    return render(request,'receita.html', receita_a_exibir)

def buscar(request):
    lista_receitas = Receita.objects.order_by('nome_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar) 

    dados = {
        'receitas' : lista_receitas
    }

    return render(request, 'buscar.html', dados)

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
    return render(request, 'pedir_receita.html', {'form': form})
           