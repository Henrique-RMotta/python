nota1 = float(input("nota 1"))
nota2 = float(input("nota 2"))
media = nota1 + nota2 / 2

if media > 7:
    print(nota1)
    print(nota2)
    print("Aprovado")
elif media < 5:
    print(nota1)
    print(nota2)
    print("reprovado")
else:
    print(nota1)
    print(nota2)
    print("recuperação")
