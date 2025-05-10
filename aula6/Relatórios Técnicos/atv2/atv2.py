soma = 0 #Define a soma como 0
num = 0 #Define um número específico como 0
numlist = [] #cria um array onde são alocadas a lista dos números inteiros
for numero in range (1,11,1): # cria um laço de repetição de 10 vezes para adicionar 10 números
    soma = soma + num #soma os números
    media = soma/numero #faz a média dos números
    num = int(input(f"digite o número {numero}:")) #declara os números inteiros um a um
    numlist.append(num) #puxa os números inteiros para o array

maior = max(numlist) #pega o maior valor da array
menor = min(numlist) #pega o menor valor da array

#imprime sos resultados
print(f"Maior = {maior}")
print(f"Menor = {menor}")
print(f"Média = {media}")