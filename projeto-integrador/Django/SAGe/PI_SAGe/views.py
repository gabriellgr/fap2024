from django.shortcuts import render, redirect

from .models import Pacientes, Medicos

def home(request):
    return render(request, 'site_SAGe/home.html')

def gerenciar(request):
    if request.method == 'POST':  # Verifica se o formulário foi enviado
        novo_usuario = Pacientes()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.cpf = request.POST.get('cpf')
        novo_usuario.data_consulta = request.POST.get('data_consulta')
        novo_usuario.telefone = request.POST.get('telefone')
        novo_usuario.save()

        # Redireciona para a página de gerenciar
        return redirect('gerenciar')  # Adiciona o redirect aqui

    pacientes = Pacientes.objects.all()
    medicos = Medicos.objects.all()
    
    context = {
        "pacientes":pacientes,
        "medicos":medicos,
    }
    
    return render(request, 'site_SAGe/gerenciar.html', context ) 

def sobre(request):
    return render(request, 'site_SAGe/sobre.html')

#formulario
def cadastro(request):
    return render(request, 'site_SAGe/cadastro.html')

def login(request):
    return render(request, 'site_SAGe/login.html')

