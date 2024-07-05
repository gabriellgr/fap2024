def remove_vogais(string):
    apagar = " "
    for e in string:
        if e.lower() not in 'aeiou':
            apagar += e
    return apagar

frase = input("Insira uma frase como exemplo: ")
resultado = remove_vogais(frase)
print(f"A frase sem as vogais seria '{resultado}'")