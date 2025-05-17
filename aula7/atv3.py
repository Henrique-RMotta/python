palavras = []
palavra = input("Digite uma palavra:")
for letras in palavra:
    palavras.append(letras)

palavras.reverse()
palavra_ivert =  ''.join(palavras)
print(palavra_ivert)
