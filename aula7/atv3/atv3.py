palavras = []
palavra = input("Digite uma palavra:")
for letras in palavra:
    palavras.append(letras)

palavras.reverse()
palavra_invert =  ''.join(palavras)
print(palavra_invert)
