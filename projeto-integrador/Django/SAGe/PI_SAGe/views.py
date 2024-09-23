from django.shortcuts import render

from .models import Cadastro

def home(request):
    return render(request, 'site_SAGe/home.html')

def portal_do_paciente(request):
    return render(request, 'site_SAGe/portal_do_paciente.html')

def sobre(request):
    return render(request, 'site_SAGe/sobre.html')

def cadastro(request):
    return render(request, 'site_SAGe/cadastro.html')

def login(request):
    return render(request, 'site_SAGe/login.html')

def cadastrados(request):
    novo_usuario = Cadastro()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.cpf = request.POST.get('cpf')
    novo_usuario.data = request.POST.get('data')
    novo_usuario.telefone = request.POST.get('telefone')
    novo_usuario.save()
    
    #Exibir dados
    cadastros = {
        'cadastrados':Cadastro.objects.all()
    }
    #Retornar dados
    return render(request,'PI_SAGe/cadastro.html', cadastros)