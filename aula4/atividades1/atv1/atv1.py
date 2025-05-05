timeA = int(input("Quantos gols o time A marcou ?:"))
timeB = int(input("Quantos gols o time B marcou ?:"))

if (timeA > timeB): 
    print(f"o time A venceu com {timeA}gols contra {timeB}gols do time B")
elif (timeA < timeB):
     print(f"o time B venceu com {timeB}gols contra {timeA}gols do time A")
else:
     print(f"o jogo empatou em {timeA} a {timeB}")