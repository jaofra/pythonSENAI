import random

print("jogo de par ou impar")
print("vamos começar a jogar")
print("escolha um numero de 0 a 5")
print("o numero escolhido pelo computador")

while True:

    par_ou_impar = input("escolha par ou impar:")
    while True:
        try:
            numero_usuario = float(input("escolha sua escolha de 0 a 5:"))

            if numero_usuario <= 5 and numero_usuario >= 0 :
                break
        except ValueError:
            print("entrada invalida")

    numero_computador = random.randint(0, 5)
    print("o computador escolheu", numero_computador)
    soma = numero_computador + numero_usuario
    print(soma)
    if soma % 2 == 0:
        resultado_do_jogo = "par"
    elif soma % 2 != 0:
        resultado_do_jogo = "impar"

    if par_ou_impar == resultado_do_jogo:
        print("voce ganhou")
        continuar = input("Deseja continuar? [Sim/Nao] ")
        if continuar != "Sim":
            break

    else:
        print("voce perdeu")
        continuar = input("Deseja continuar? [Sim/Nao] ")
        if continuar != "Sim":
            break