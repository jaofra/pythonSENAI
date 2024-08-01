print("olá mundo")
 #escolha uma opção
print("calculadora de grandezas")
print(" [1] tensão eletrica")
print(" [2] corrente eletrica")
print(" [3] resistencia eletrica")

opçao = int(input("escolha o numero"))

if opçao == 1:
    print("resistencia")
    print(**)
    tensao = float(input("digite a tensão em volts"))
    corrente = float(input("digite a corrente em amperes"))

    resistencia = tensao * corrente

    print(f"a resistencia é de{resistencia}")

elif opçao == 2:
    print("tençao")
    print(**)
    resistencia = float(input("digite a resistencia em ohms"))
    corrente = float(input("digite a corrente em amperes"))

    tensao = resistencia * corrente



    print(f"a tensão é de{tensao}volts")


elif opçao == 3
    print("corrente")
elif opçao == 3
    print("resistencia resitor")
elif opçao == 4
    print("digitaçao invalida")

