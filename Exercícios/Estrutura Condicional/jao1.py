while True:
    try:
        numero = int(input("insira um numero:"))
        if numero > 0:
            break
        elif numero < 0:
            break
    except ValueError:
        print("insira um valor valido")
if numero > 0:
    print(f"o {numero} é positivo")
else:
    print("numero é negativo")