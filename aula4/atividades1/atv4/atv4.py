num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
operador = int(input("Digite o operador com o número respectivo de cada:\n1-soma\n2-subtração\n3-multiplicação\n4-divisão\n"))
if (operador == 1):
    print(f"a soma é: {num1 + num2}")
elif (operador == 2):
    print(f"a subtração é: {num1 - num2}")
elif (operador == 3):
    print(f"a multiplicação deu: {num1 * num2}")
elif (operador == 4):
    print(f"a divisão é: {num1 / num2}")
else:
    print("Não esxiste este operador.")