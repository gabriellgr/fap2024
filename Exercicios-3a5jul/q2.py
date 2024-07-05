def contar_ocorrencias(texto):
    for e in ",.?:;!":
        texto = texto.replace(e, " ")
    
    texto = texto.lower()
    palavras = texto.split()
    
    contador = {}

    for palavra in palavras:
        if palavra in contador:
            contador[palavra] += 1
        else:
            contador[palavra] = 1
    return contador

texto = input("Digite uma frase como exemplo: ")
resultado = contar_ocorrencias(texto)
print(f"A quantidade é {resultado}")