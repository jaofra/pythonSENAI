nota1 = int(input("Digite a nota do aluno: "))
nota2 = int(input("Digite a nota do aluno: "))
while True:
    try:
        if nota1 > 100:
            print("nota invalida")
        elif nota2 > 100:
            print("nota invalida")

        else:
            break

    except ValueError:
        print("Digite um valor menor que 100")
resultado = nota1 + nota2
media = resultado / 2

if media >= 70:
    saudacao = "Aprovado"

elif media < 70:
    saudacao = "Reprovado"

print("devido a nota do aluno: ", saudacao)


