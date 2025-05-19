numeros = []
i =0 
while i < 10:
    i+= 1
    numero = int(input(f"Digite um número{i}:"))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)
media = (maior + menor)/2
print(f"o maior número é: {maior}")
print(f"o menor número é: {menor}")
print(f"A média é: {media}")