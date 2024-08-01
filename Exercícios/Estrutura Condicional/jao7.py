while True:
    try:
        dia = int(input("insira o numero de acordo com o mes :"))
        if dia in range(1, 12):
            break
        else:
            print("digite um numero de 1 a 12")
    except ValueError:
        print("digite um numero de 1 a 12")

if dia == 1:
    print("janeiro")
elif dia == 2:
    print("fevereiro")
elif dia == 3:
    print("marco")
elif dia == 4:
    print("abril")
elif dia == 5:
    print("maio")
elif dia == 6:
    print("junho")
elif dia == 7:
    print("julho")
elif dia == 8:
    print("agosto")
elif dia == 9:
    print("setembro")
elif dia == 10:
    print("outubro")
elif dia == 11:
    print("novembro")
elif dia == 12:
    print("dezembro")