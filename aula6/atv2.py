soma = 0
num = 0
numlist = []
for numero in range (1,11,1):
    soma = soma + num
    media = soma/numero 
    num = int(input(f"digite o número {numero}:"))
    numlist.append(num)

maior = max(numlist)
menor = min(numlist)
print(f"Maior = {maior}")
print(f"Menor = {menor}")
print(f"Média = {media}")