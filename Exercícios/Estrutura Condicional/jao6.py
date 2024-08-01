while True:
    try:

        numero1 = int(input('Digite um numero: '))
        if numero1 <= 0:
            print("numero invalido")
        else:
            break


    except ValueError:
        print('Numero invalido')

while True:
    try:

        numero2 = int(input('Digite um numero: '))
        if numero2 <= 0:
            print("numero invalido")
        else:
            break

        numero3 = int(input('Digite um numero: '))
        if numero3 <= 0:
            print("numero invalido")
        else:
            break


    except ValueError:
        print('Numero invalido')
if numero2 > numero1:
    print(f'{numero2} é maior que o {numero1}')
elif numero1 > numero2:
    print(f"{numero1} maior que o {numero2}")
elif numero1 > numero3:
    print(f"{numero1} maior que o {numero3}")
elif numero2 > numero3:
    print(f"{numero2} maior que o {numero3}")
elif numero3 > numero2:
    print(f"{numero3} maior que o {numero2}")
elif numero3 > numero1:
    print(f"{numero3} maior que o {numero1}")