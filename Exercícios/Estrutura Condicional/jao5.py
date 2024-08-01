while True:
    try:
        dia = int(input("insira o numero de acordo com o dia da semana :"))
        if dia in range(1, 8):
            break
        else:
            print("digite um numero de 1 a 7")
    except ValueError:
        print("digite um numero de 1 a 7")

if dia == 1:
    print("hoje é segunda")
elif dia == 2:
    print("hoje é terca")
elif dia == 3:
    print("hoje é quarta")
elif dia == 4:
    print("hoje é quinta")
elif dia == 5:
    print("hoje é sexta")
elif dia == 6:
    print("hoje é sabado")
elif dia == 7:
    print("hoje é domingo")
