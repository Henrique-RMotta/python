numpess = int(input("Quantas pessoas serão analisadas:"))#pede ao usuário quantas pessoas serão analisadas
media = 0 #declara a variável média
soma = 0 #declara a variável soma
i = 0
 # cria um laço de repetição em que ele se repetirá de acordo com o número de pessoas que o usuário indicou que serão analisadas
while (i < numpess):
    temp = float(input(f"Qual a temperatura do paciente {i + 1}: ")) #qual a temperatura do paciente 
    soma = soma + temp #soma as temperaturas dos pacientes analisados
    media = soma/numpess # faz a média das temperaturas analisadas
    i+= 1
    if temp <= 37.2: #se a temperatura for menor que 37,2 graus define como normal
        print(f"A temperatura do paciente {i + 1 } está normal")
    elif (37.2 < temp <= 38 ): #se a temperatura for maior que 37,2 graus e menor que 38 graus define como estado febril
        print(f"A temperatura do paciente {i + 1 } está em estado febril")
    elif (38 < temp <= 39 ): #se a temperatura for maior que 38 graus e menor que 39 graus define como estado febril
        print(f"A temperatura do paciente {i + 1 } está com febre")
    elif (temp > 39 ): #se a temperatura for maior que 39 graus  define como febre alta
        print(f"A temperatura do paciente {i + 1 } está com febre alta")


print(f"Pessoas Analisadas: {numpess}")
print(f"Média das temperaturas analisadas: {media}")

