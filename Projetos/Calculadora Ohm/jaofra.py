
while True:
    try:
        deseja_continuar = int(input('Deseja continuar? [1] sim/ [2] nao : '))
        if deseja_continuar == 1:
            break
        else:
            print("sair_do_jogo == 2")

    except ValueError:
        print("Erro, digite apenas [1] pra sim/ [2] pra nao :")
