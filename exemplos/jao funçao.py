from datetime import datetime

def menu_calculadora():
    print("menu calculadora")
    print("1 - adiçao")
    print("2 - subtraçao")
    print("3 - multiplicaçao")
    print("4 - divisao")


def ola_nome(nome):
    print("ola", nome)

# menu_calculdora()

ola_nome("lulu")

def calcula_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade


def solicita_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento: "))
            if ano_nascimento < datetime.now().year:
                return ano_nascimento
            else:
                print("digite um ano menor que  o atual")
        except ValueError:
            print("digite apenas numeros. ex: 2007")

#idade = calcula_idade(ano_nascimento)
#exibir_idade(calcula_idade(ano_nascimento))


