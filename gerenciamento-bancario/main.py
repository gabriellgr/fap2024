from tabulate import tabulate

contas = {}

def cadastro_contas():
  conta = {}
  
  numero_conta = 1
  
  conta['nome'] = input("Informe o nome do correntista: ")
  conta['data_abertura'] = input("Informe a data da abertura da conta: (dd/mm/aaaa)")
  conta['saldo'] = 0
  
  while True:
    print("[1] Poupança")
    print("[2] Corrente\n")
    
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

  
  for numero_conta in contas:
    numero_conta += 1
    if numero_conta in contas:
      print("ID já cadastrado.")
    else:
      conta['numero_conta'] = numero_conta
      break
 

  contas[numero_conta] = conta

def operacoes():
  print("----- Operações Financeiras -----")
  print("[1] Depósito")
  print("[2] Saque")

  while True:
    try:
      numero_conta = int(input("Informe o número da conta: "))
      if numero_conta in contas:
        try:
          opcao = int(input("Informe a operação que deseja fazer: "))
        except ValueError:
          print("Valor inválido.")
          continue
          if opcao == 1:
            while True:
              try:
                valor_deposito = float(input("Informe o valor do depósito: "))
              except ValueError:
                print("Valor inválido.")
                continue
  
                if valor_deposito:
                  contas[numero_conta]['saldo'] += valor_deposito
                  break
    except ValueError:
      print("Valor inválido.")
      continue

def listar_contas():
  if not contas:
    print("Não há contas cadastradas.")
    return

  data = [[
    numero_conta,
    conta['nome'],
    conta['data_abertura'],
    conta['saldo'],
    conta['tipo_conta'],
  ] for numero_conta, conta in contas.items()]

  print(
    tabulate(data, headers=['Numero conta', 'Nome do correntista', 'Data de abertura', 'Saldo', 'Tipo conta'], tablefmt='simple_grid'))
  

def carregar_dados():
  global contas
  with open("dados_contas.json", "r") as arquivo_json:
      contas = json.load(arquivo_json)
  print("Dados carregados com sucesso.")

def salvar_dados():
  with open("dados_contas.json", "w") as arquivo_json:
      json.dump(contas, arquivo_json)
  print("Dados das contas salvos com sucesso.")

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
