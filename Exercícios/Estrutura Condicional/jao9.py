import datetime
#tempo atual

tempo_atual = datetime.datetime.now()
print(f"hoje é dia {tempo_atual.day}")
if tempo_atual.strftime("%w") == "1":
    print("segunda feira")
elif tempo_atual.strftime("%w") == "2":
    print("terca feira")
elif tempo_atual.strftime("%w") == "3":
    print("quarta feira")
elif tempo_atual.strftime("%w") == "4":
    print("quinta feira")
elif tempo_atual.strftime("%w") == "5":
    print("sexta feira")
elif tempo_atual.strftime("%w") == "6":
    print("sabado")
elif tempo_atual.strftime("%w") == "0":
    print("-domingo")


while True:



    if tempo_atual.month == 1:
        mes = "janeiro"
    elif tempo_atual.month == 2:
        mes = "fevereiro"
    elif tempo_atual.month == 3:
        mes = "março"
    elif tempo_atual.month == 4:
        mes = "abril"
    elif tempo_atual.month == 5:
        mes = ("maio")
    elif tempo_atual.month == 6:
        mes = "junho"
    elif tempo_atual.month == 7:
        mes = "julho"
    elif tempo_atual.month == 8:
        mes = "agosto"
    elif tempo_atual.month == 9:
        mes = "setembro"
    elif tempo_atual.month == 10:
        mes = "outubro"
    elif tempo_atual.month == 11:
        mes = "novembro"
    elif tempo_atual.month == 12:
        mes = "dezembro"
    else:
        mes = "dezembro"
    print(f"do mes de  {mes}")
    print(f"de {tempo_atual.year}")
    print(f"são {tempo_atual.time()}")
    if tempo_atual.hour< 12:
        print("bom dia")


    elif tempo_atual.hour < 19:
        print("boa tarde")

    if tempo_atual.hour > 19:
        print("boa noite")
    break





