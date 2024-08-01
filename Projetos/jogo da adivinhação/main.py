import random

print("advinhação humano VS maquina")
print("vamos começar a jogarr")
print("acerte um numero de 0 a 100 que a maquina escolher")
print("o numero escolhido pelo computador")

numero_aleatorio = random.randint(1, 100)

while True:
    escolha_um_numero = float(input("Digite um numero: "))

    if escolha_um_numero == numero_aleatorio:
        print("parabéns voce acertou o numero escolhido pelo computador")
        continuar = input("Deseja continuar? [Sim/Nao] ")
        if continuar != "Sim":
            break
        numero_aleatorio = random.randint(1, 100)
    elif escolha_um_numero > numero_aleatorio:
        print("tente novamente o numero escolhido é maior que o numero escolhido pelo computador")

    elif escolha_um_numero < numero_aleatorio:
        print("tente novamente o numero escolhido é menor que o numero escolhido pelo computador")
