#somando números do intervalo informando limitando o maior número
inicio = int (input("Informe o primeiro número"))
fim = int(input("Informe o número final"))
salto = int (input("Informe o salto"))
texto = "calculo:"
soma =0 
for numero in range(inicio,fim,salto):
    soma = soma + numero
    texto = texto + str(numero)
    if numero >50:
        texto = texto + "\nPassou de 50"
        break
    if numero != fim -1:
        texto = texto + "1"
print(f"{texto}")
print(f"Soma: {soma}")