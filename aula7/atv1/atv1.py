idademasculino = 0
idademfeminino = 0
contadormasculino = 0
contadorfeminino = 0
for pessoas in range (1,11):
    idade = int(input(f"Qual a idade da pessoa {pessoas} ?"))
    sexo = input("qual o seu sexo ? (M/F)")
    if(sexo == "M"):
        idademasculino = idade + idademasculino
        contadormasculino += 1
    elif (sexo == "F"):
        idadefeminino = idade + idadefeminino
        contadorfeminino += 1
    else: 
        print("inválido")

if contadormasculino > 0:
    mediamasculino= idademasculino / contadormasculino
else:
    mediamasculino= 0

if contadorfeminino > 0:
    mediafeminino = idadefeminino / contadorfeminino
else:
    mediafeminino = 0

media = (idademasculino + idadefeminino) / 10

print(f"A média de idade dos homens é:{mediamasculino}")
print(f"A média de idade das mulheres é:{mediafeminino}")
print(f"A média total de idade é {media}")
