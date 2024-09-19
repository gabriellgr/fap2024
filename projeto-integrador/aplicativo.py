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
def adicionar_paciente(paciente:str, data_nasc:str, cpf:str, contato:str):
    pacientes = {
        'paciente': paciente,
        'data_nasc': data_nasc,
        'cpf': cpf,
        'contato': contato
    }

    if pacientes:
        lista_pacientes.append(pacientes)
    return RedirectResponse(url="/", status_code=303)

    # for paciente in lista_pacientes:
    #     return P(f"{paciente['nome']} {paciente['data_nasc']} {paciente['cpf']} {paciente['contato']}")

    

serve()