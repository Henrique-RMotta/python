idadehomem = 0
idademulher = 0
for pessoas in range (1,11):
    idade = int(input(f"Qual a idade da pessoa {pessoas} ?"))
    sexo = input("qual o seu sexo ? (H/M)")
    if(sexo == "H"):
        idadehomem = idade + idadehomem
    elif (sexo == "M"):
        idademulher = idade + idademulher
    else: 
        print("inválido")

    mediahomem = idadehomem/10
    mediamulher = idademulher/10
    media = (idadehomem+idademulher)/20

print(f"A média de idade dos homens é:{mediahomem}")
print(f"A média de idade das mulheres é:{mediamulher}")
print(f"A média total de idade é {media}")
