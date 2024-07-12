alunos = []

while True:
  print("Menu de cadastro de alunos.")
  print("[1] Cadastrar novo aluno")
  print("[2] Listar alunos cadastrados")
  print("[3] Atualizar cadastro")
  print("[4] Remover aluno")
  print("[5] Pesquisar alunos")
  print("[6] Média das notas")
  print("[0] Sair")

  opcao = int(input("Escolha uma opção: "))
  print("----------------------")
  
  if opcao == 0:
    print("Encerrando...")
    break
  
  if opcao == 1:
    # Cadastrar novo aluno
    novo_aluno = {}

    novo_aluno['nome'] = input("Nome do aluno: ")
    novo_aluno['curso'] = input("Curso: ")
    novo_aluno['matricula'] = int(input("Matrícula: "))
    novo_aluno['nota1'] = float(input("Nota da primeira unidade: "))
    novo_aluno['nota2'] = float(input("Nota da segunda unidade: "))
    novo_aluno['nota3'] = float(input("Nota da terceira unidade: "))
    

    alunos.append(novo_aluno)

    print("\nAluno cadastrado com sucesso!\n")

  elif opcao == 2:
    if len(alunos) == 0:
      print("Não temos alunos cadastrados.")
    else:
      for aluno in alunos:
        print(f"Nome do aluno: {aluno['nome']}")
        print(f"Curso: {aluno['curso']}")
        print(f"Matrícula: {aluno['matricula']}")
        """print(f"Notas:\nPrimeira unidade -> {aluno['nota1']}\nSegunda unidade -> {aluno['nota2']}\nTerceira unidade -> {aluno['nota3']}")"""
        print("----------------------")

  elif opcao == 3:
    aluno_atualizar = input("Nome do aluno que deseja atualizar: ")
    for aluno_atualizar in alunos:
      if aluno_atualizar in alunos:
        print("Qual o opção deseja atualizar: ")
        print("[1] Nome\n[2] Curso")
        print("[3] Nota da primeira unidade\n[4] Nota da segunda unidade\n[5] Nota da terceira unidade")
        opcao_att = int(input("\nEscolha uma opção: "))
          
      else:
        print("\nError...")
        print("Aluno não encontrado\n")
  elif opcao == 4:
    aluno_remover = input("Nome do aluno que deseja remover: ")
    for aluno in alunos:
      if aluno_remover == aluno['nome']:
        alunos.remove(aluno)
      else:
        print("Aluno não encontrado.")
        break
      print("Aluno removido com sucesso.")

  elif opcao == 5:
    nome_p = input("Digite um nome que deseja pesquisar: ")
    for aluno in alunos:
      if nome_p == aluno['nome']:
        print(f"Nome do aluno: {aluno['nome']}")
        print(f"Curso: {aluno['curso']}")
        print(f"Matrícula: {aluno['matricula']}")
        print(f"Notas:\nPrimeira unidade -> {aluno['nota1']}\nSegunda unidade -> {aluno['nota2']}\nTerceira unidade -> {aluno['nota3']}")
        print("----------------------")


  
  else:
    print("Opção inválida, selecione alguma das opções listadas.")