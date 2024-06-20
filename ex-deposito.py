comprimento_d = float(input("Insira o comprimento: "))
largura_d = float(input("Insira a largura: "))
altura_d = float(input("Insira a altura: "))

volume_deposito = comprimento_d*largura_d*altura_d
print("-------Escolha uma das bolas--------")
print("Basquete Adulto\nBasquete Infantil\nFutebol\nVôlei\nFutsal\nHandball\nOutros")
lista_bola = ["Basquete Adulto", "Basquete Infantil", "Futebol", "Vôlei", "Handball", "Futsal", "Outros"]

print("------------------------------------")

i = input("Esolha uma bola: ")

while True:
    if i in lista_bola:
        break
    else:
        print("Insira uma das bolas listadas.")
        i = input("Escolha uma bola: ")

if i == "Basquete Adulto":
    volume_ba = 24**3
    quantidade = volume_deposito/volume_ba
    print(f"A quantidade de bolas que cabem no depósito é aproximadamente: {int(quantidade)}")
elif i == "Basquete Infantil" or i == "Futebol":
    volume_bif = 23**3
    quantidade = volume_deposito/volume_bif
    print(f"A quantidade de bolas que cabem no depósito é aproximadamente: {int(quantidade)}")
elif i == "Vôlei":
    volume_v = 21**3
    quantidade = volume_deposito/volume_v
    print(f"A quantidade de bolas que cabem no depósito é aproximadamente: {int(quantidade)}")
elif i == "Handball":
    volume_h = 19**3
    quantidade = volume_deposito/volume_h
    print(f"A quantidade de bolas que cabem no depósito é aproximadamente: {int(quantidade)}")
elif i == "Futsal":
    volume_fs = 20**3
    quantidade = volume_deposito/volume_fs
    print(f"A quantidade de bolas que cabem no depósito é aproximadamente: {int(quantidade)}")
elif i == "Outros":
    volume_o = float(input("Insira o diâmetro da bola: "))
    volume_o = volume_o**3
    quantidade = volume_deposito/volume_o
    print(f"A quantidade de bolas que cabem no depósito é aproximadamente: {int(quantidade)}")