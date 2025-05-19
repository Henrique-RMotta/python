
tentativas = [1]
for i in tentativas:
    nome = input("Digite seu nome de usuário:")
    senha = input("Digite sua senha:")
    if nome == senha:
        print("Acesso não liberado, senha igual ao nome não é permitido")
        tentativas.append(i)
    else:
        print("Acesso liberado")
