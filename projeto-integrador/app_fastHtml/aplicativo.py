from fasthtml.common import *
from componentes import *

app, routes = fast_app()

lista_pacientes = []

@routes("/")
def homepage():
    formulario = form()
    print(lista_pacientes)
    elemento_lista_pacientes = listar_pacientes(lista_pacientes)
    return Titled("Cadastro de pacientes", formulario, elemento_lista_pacientes)

@routes("/adicionar_paciente", methods=["post"])
def adicionar_paciente(request):
    form_data = form()
    paciente = form_data.get('paciente')
    data_nasc = form_data.get('data_nasc')
    cpf = form_data.get('cpf')
    contato = form_data.get('contato')

    pacientes = {
        'paciente': paciente,
        'data_nasc': data_nasc,
        'cpf': cpf,
        'contato': contato
    }

    if pacientes:
        lista_pacientes.append(pacientes)
    return RedirectResponse(url="/", status_code=303)

if __name__ == '__main__':
    serve(app)
