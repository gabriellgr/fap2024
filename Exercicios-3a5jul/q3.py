def func_cript(frase, deslocamento):
  alfabeto = 'abcdefghijklmnopqrstuvwxyz'
  frase_criptografada = ""

  for e in frase.lower():
    if e in alfabeto:
      posicao = (alfabeto.index(e)+deslocamento) % len(alfabeto)
      frase_criptografada += alfabeto[posicao]
    else:
      frase_criptografada += e

  return frase_criptografada

frase = input("Digite uma frase para criptografar: ")
deslocamento = 3

resultado = func_cript(frase, deslocamento)
print(f"A frase utilizada é: {frase}")
print(f"A frase criptografada é: {resultado}")