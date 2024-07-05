def soma_pares(soma):
    lista = []
    soma = 0
    for i in range(5):
        num = int(input())
        lista.append(num)
    for e in lista:
        if e%2 == 0:
            soma += e
    return soma
soma = 0
resultado = soma_pares(soma)
print(resultado)