idade = int(input("Digite a idade do narrador:"))

if (5 <= idade <= 7):
    print("sua classifiação é Infantil A")
elif (8 <= idade <= 11):
    print("sua classifiação é Infantil B")
elif (12 <= idade <= 13):
    print("sua classifiação é Juvenil A ")
elif (14 <= idade <= 17): 
    print("sua classifiação é Juvenil B")
elif (idade >= 18):
    print("sua classficação é Adultos")