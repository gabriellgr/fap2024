peso = int(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))

while True: 
  if (peso > 10 and peso < 350):
    imc = peso / altura**2
    break
  else:
    print("Digite um peso entre 10 a 350")
    peso = int(input("Qual o seu peso? "))

if imc < 18.5:
  print("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
  print("Peso adquado")
elif imc >= 25 and imc <= 29.9:
  print("Sobrepeso")
elif imc >= 30 and imc <= 34.9:
  print("Obesidade grau 1")
elif imc >= 35 and imc <= 39.9:
  print("Obesidade grau 2")
else:
  print("Obesidade grau 4")
print(f"Seu IMC é {imc:.2f}")