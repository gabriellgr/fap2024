from django.shortcuts import render

def home(request):
    return render(request, 'site_SAGe/home.html')

def portal_do_paciente(request):
    return render(request, 'site_SAGe/portal_do_paciente.html')

def sobre(request):
    return render(request, 'site_SAGe/sobre.html')

def cadastro(request):
    return render(request, 'site_SAGe/cadastro.html')
    