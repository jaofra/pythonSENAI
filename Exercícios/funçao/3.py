def menu():
    print("[0] sair\n[1] soma\n[2] subtração\n[3] multiplicação\n[4] divisão\n[5] todas")
    opcao = input(">>")
    while opcao not in ["0","1","2","3","4","5"]:
        print("erro, tente novamente")
        opcao = input(">>")


def solicitar_numero():
    while True:
        try:
            numero = float(input("Digite um numero: "))
            if numero < 0:
                raise ValueError
        except ValueError:
            print("entrada invalida")


def soma_numero(numero_1, numero_2):
    soma = numero_1 + numero_2
    return soma

def subtrair_numero(numero_1, numero_2):
    subtracao = numero_1 - numero_2
    return subtracao

def multiplicao_numero(numero_1, numero_2):
    multiplicacao = numero_1 * numero_2
    return multiplicacao

def divisao_numero(numero_1, numero_2):
    divisao = numero_1 / numero_2
    return divisao

def exibir_resultado(divisao, multiplicacao, soma, subtracao):





