import random

numero = random.randint(1, 100)
tentativas = 1

while True:
  numero_escolhido = int(input("Escolha um número: "))
  if numero_escolhido == numero:
    print("Parabéns você acertou o número!!")
    print(f"Você conseguiu em {tentativas} tentativas.")
    break
  elif numero_escolhido > numero:
    print("O número secreto é menor")
    tentativas += 1
  elif numero_escolhido < numero:
    print("O número secreto é maior")
    tentativas += 1