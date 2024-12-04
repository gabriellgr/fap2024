from fasthtml.common import *

def corpo_pagina(titulo, subtitulo):
    return Div(
        H1(titulo),
        P(subtitulo),
        P("Esse componente foi gerado com FastHTML")
    )

def form():
    formulario = Form(
        Input(type="text", name="paciente", placeholder="Insira o nome do paciente"),
        Input(type="text", name="data_nasc", placeholder="Insira a data de nascimento"),
        Input(type="text", name="cpf", placeholder="Insira o CPF"),
        Input(type="text", name="contato", placeholder="Número de telefone"),
        Button("Enviar"),
        method="post",
        action="/adicionar_paciente"
    )
    return formulario

def listar_pacientes(lista_pacientes):

    itens_lista = [Li(f"Paciente: {paciente['paciente']}", Br(f"CPF: {paciente['cpf']}")) for paciente in lista_pacientes]

    lista = Ul(
        *itens_lista
    )
    return lista