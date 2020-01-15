from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita
from django.conf import settings

def cadastro(request):
    """Cadastra uma nova pessoa no sistema"""
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if not nome.strip():
            print('inválido')
            messages.error(request, 'O campo nome não pode ficar vazio')
            return redirect('cadastro')
        # validando senhas
        if password != password2:
            messages.error(request, 'As senhas não conferem')
            return redirect('cadastro')
        # verificando se o usuário já está cadastrado
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastradado. Por favor utilize outro email')
            print('email já cadastrado')
            return redirect('cadastro')
        else:
            user = User.objects.create_user(username=nome, email=email, password=password)
            user.save()
            messages.success(request, 'Cadastro realizado com sucesso')
            return redirect('login')        
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email== "" or senha == "":
            messages.error(request, 'O campos email e senha precisam ser preenchidos')
        else:
            if User.objects.filter(email=email).exists():
                nome = User.objects.filter(email=email).values_list('username',flat=True).get()
                user = auth.authenticate(request, username=nome, password=senha)
                if user is not None:
                    auth.login(request, user)
                    print('login realizado com sucesso')
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Email ou senha não estão corretos')
                    redirect('login')
            else:
                messages.error(request, 'Email não encontrado')
                redirect('login')
    return render(request,'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        todas_as_receitas = Receita.objects.order_by('-date_receita')
        receitas = todas_as_receitas.filter(pessoa=id)

        dados = {
            'receitas' : receitas
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return render(request,'receitas/index.html')

