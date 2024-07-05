lista1 = []
lista2 = []
print('---- PRIMEIRA LISTA ----')
for i in range(3):
    valor1 = int(input(f"selecione o valor número {i+1}: "))
    lista1.append(valor1)
print('\n---- SEGUNDA LISTA ----')
for i in range(3):
    valor2 = int(input(f"selecione o valor número {i+1}: "))
    lista2.append(valor2)

nova_lista = lista1+lista2

nova_lista.sort()

print(nova_lista)
