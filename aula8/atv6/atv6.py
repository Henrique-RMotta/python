palavras = []
palavra = input("Digite uma palavra:")
i = 0 
while i < palavra:
    palavras.append(i)

palavras.reverse()
palavra_invert =  ''.join(palavras)
print(palavra_invert)
