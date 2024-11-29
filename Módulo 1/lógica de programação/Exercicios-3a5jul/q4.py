def converter_expressao(expressao):
    return eval(expressao)

string = input("Digite a expressão que deseja calcular: ")
resultado = converter_expressao(string)

print(f"O resultado é: {resultado}")