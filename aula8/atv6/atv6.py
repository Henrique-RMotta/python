palavra = input("Digite uma palavra: ")
i = len(palavra) - 1
palavra_invert = []
while i >= 0:
    palavra_invert += palavra[i]
    i -= 1
res = "".join(palavra_invert)
print(res)
