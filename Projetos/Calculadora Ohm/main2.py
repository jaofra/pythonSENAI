print("olá mundo")
 #escolha uma opção
print("calculadora de grandezas")
print(" [1] resistencia eletrica")
print(" [2] corrente eletrica")
print(" [3] tensao eletrica")

def transforma_tensao(resistencia, corrente):
    tensao = resistencia * corrente
def recebe_tensao():
    while True:
        try:
            tensao = float(input("insira o valor da tensao"))
            if tensao > 0:
                return tensao

        except ValueError:
            print("tente novamnete com valores númericos")


def recebe_corrente():
    corrente = float(input("digite a corrente em amperes"))
    return corrente


def transforma_resistencia(tensao, corrente):
    resistencia = tensao * corrente
    return resistencia
opçao = int(input("escolha o numero"))

if opçao == 1:
    print("resistencia")
    print(**)


    recebe_tensao()
    recebe_corrente()
    transforma_resistencia()

    print(f"a resistencia é de{transforma_resistencia()}")

elif opçao == 2:
    print("tençao")
    print(**)

    def recebe_resistencia():
        resistencia = float(input("digite a resistencia em ohms"))
        return resistencia

    recebe_corrente()





    print(f"a tensão é de{transforma_tensao()}volts")



elif opçao == 3:

    print("resistencia resitor")
elif opçao == 4:
    print("digitaçao invalida")

