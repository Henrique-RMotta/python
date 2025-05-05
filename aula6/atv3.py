numpess = int(input("Quantas pessoas serão analisadas:"))
media = 0
soma = 0
for numerodetemps in range(numpess):
    temp = float(input(f"Qual a temperatura do paciente {numerodetemps + 1 }: "))
    soma = soma + temp
    media = soma/numpess
    if temp <= 37.2:
        print(f"A temperatura do paciente {numerodetemps + 1 } está normal")
    elif (37.2 < temp <= 38 ):
        print(f"A temperatura do paciente {numerodetemps + 1 } está em estado febril")
    elif (38 < temp <= 39 ):
        print(f"A temperatura do paciente {numerodetemps + 1 } está com febre")
    elif (temp < 39 ):
        print(f"A temperatura do paciente {numerodetemps + 1 } está com febre alta")


print(f"Pessoas Analisadas: {numpess}")
print(f"Média das temperaturas analisadas: {media}")

