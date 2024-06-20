temperatura = float(input("Insira uma temperatura: "))
converter = input("Digite 'C' para converter para Celsius, 'F' para converter para Fahrenheit: ")

while True:
  if converter == "C" or converter == "c":
    temperatura_c = (temperatura - 32) * 5/9
    print(f"{temperatura}°F em Celcius é {temperatura_c:.2f}°C")
    break
  elif converter == "F" or converter == "f":
    temperatura_f = (temperatura * 5/9) + 32
    print(f"{temperatura}°C em Fahrenheit é {temperatura_f:.2f}°F" )
    break
  else:
    converter = input(("Insira uma temperatura correta: "))