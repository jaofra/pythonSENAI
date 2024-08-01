import datetime
#tempo
while True:
    tempo_atual = datetime.datetime.now()



    print(f"são {tempo_atual.strftime("%H:%M)}")

    if tempo_atual.hour < 12:
        print("bom dia")


    elif tempo_atual.hour< 19:
        print("boa tarde")

    elif tempo_atual.hour > 19:
        print("boa noite")



    elif tempo_atual.hour < 5:
        print("esta de madrugada")
    break


