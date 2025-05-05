salario = float(input("digite seu salário atual"))
acréscimo = float(input("digite o acréscimo de salario em porcentagem"))
salarioacrescimo = salario * (acréscimo/100)
salarionovo = salarioacrescimo + salario
print(f"Seu novo salário é: {salarionovo}")