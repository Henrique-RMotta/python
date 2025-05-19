tabuada = int(input("Qual tabuada você quer treinar:"))
contadoracertos = 0
contadorerros = 0
for numero in range (1,11):
    resultadocorreto = numero * tabuada
    resultado = int(input(f"Qual será o resultado de {numero}x{tabuada}:"))
    if (resultado == resultadocorreto):
        print("CORRETO")
        contadoracertos += 1
    else:
        print(f"QUE PENA, VOCÊ ERROU, O VALOR CORRETO É {resultadocorreto}")
        contadorerros += 1
    
print(f"Você acertou {contadoracertos} multiplicações")
print(f"Você errou {contadorerros} multiplicações")