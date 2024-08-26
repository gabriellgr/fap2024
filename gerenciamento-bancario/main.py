import json
from tabulate import tabulate

contas = {}

def cadastro_contas():
  conta = {}
  
  print("----- Cadastro de contas -----")
  conta['nome'] = input("Informe o nome do correntista: ")
  conta['data_abertura'] = input("Informe a data da abertura da conta: (dd/mm/aaaa) ")
  conta['saldo'] = 0
  
  numero_conta = 1
  
  while True:
    print("----- Tipo de conta -----")
    print("[1] Poupança")
    print("[2] Corrente")
    print("------------------------")
    try:
      escolha = int(input("Informe o tipo de conta: "))
    except ValueError:
      print("Valor inválido.")
      continue
    if escolha == 1:
      conta['tipo_conta'] = "Poupança"
      break
    if escolha == 2:
      conta['tipo_conta'] = "Corrente"
      break
      
  if not contas:
    conta['numero_conta'] = numero_conta
  else:
    for numero_conta in contas:
      numero_conta += 1
      if numero_conta not in contas:
        conta['numero_conta'] = numero_conta
        break

  contas[numero_conta] = conta
 
  print("\n---- Cadastro realizado com sucesso ----")

def operacoes():
  while True:
    try:
        numero_conta = int(input("Informe o número da conta: "))

        if numero_conta in contas:
            print("----- Operações Financeiras -----")
            print("[1] Depósito")
            print("[2] Saque")
            print("---------------------------------")
        
        try:
            opcao = int(input("Informe a operação que deseja fazer: "))
          
            if opcao == 1:
                while True:
                    try:
                        valor_deposito = float(input("Informe o valor do depósito: "))

                        if valor_deposito:
                            contas[numero_conta]['saldo'] += valor_deposito
                            print("-----------------------------")
                            print("Valor depositado com sucesso.")
                            print("-----------------------------")
                            break
                        break

                    except ValueError:
                        print("Valor inválido.")
                        continue
            else:
                break

            if opcao == 2:
                while True:
                    try:
                        valor_saque = float(input("Informe o valor do saque: "))

                        if valor_saque:
                            contas[numero_conta]['saldo'] -= valor_saque
                            break
                        break

                    except ValueError:
                        print("Valor inválido.")
                        continue
            else:
                break

        except ValueError:
            print("Valor inválido.")
            continue
        break

    except ValueError:
        print("Valor inválido.")
        continue

def listar_contas():
  if not contas:
    print("--------------------------")
    print("Não há contas cadastradas.")
    print("--------------------------")
    return

  data = [[
    numero_conta,
    conta['nome'],
    conta['data_abertura'],
    conta['saldo'],
    conta['tipo_conta'],
  ] for numero_conta, conta in contas.items()]

  print(
    tabulate(data, headers=['Número da conta', 'Nome do correntista', 'Data de abertura', 'Saldo', 'Tipo de conta'], tablefmt='simple_grid'))


def carregar_dados():
  global contas
  with open("dados_contas.json", "r") as arquivo_json:
      contas = json.load(arquivo_json)
  print("\nDados carregados com sucesso.\n")

def salvar_dados():
  with open("dados_contas.json", "w") as arquivo_json:
      json.dump(contas, arquivo_json)
  print("\nDados das contas salvos com sucesso.\n")

while True:
  print("[1] Cadastrar conta")
  print("[2] Listar todas as contas cadastradas")
  print("[3] Operações financeiras")
  print("[4] Excluir um aluno do sistema")
  print("[5] Calcular e exibir a média das notas de cada aluno")
  print("[6] Carregar dados de arquivo")
  print("[7] Salvar dados em arquivo")
  print("[0] Sair")

  try:
    opcao = int(input("Escolha uma opção: "))

    if opcao < 0 or opcao > 7:
      print("-\nOpção inválida. Tente novamente.\n-")
      continue

    if opcao == 1:
      cadastro_contas()
      continue

    if opcao == 2:
      listar_contas()
      continue

    if opcao == 3:
      operacoes()
      continue

    if opcao == 6:
      carregar_dados()
      continue

    if opcao == 7:
      salvar_dados()
      continue

    if opcao == 0:
      print("-\nSaindo do programa\n-")
      break

  except ValueError:
      print("-\nOpção inválida. Tente novamente.\n-")
