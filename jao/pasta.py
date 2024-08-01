# o while repete tudo que esta dentro dele
while True:
    #o try vai tentar executar esse bloco de codigo
    try:
        idade = int(input('Digite sua idade: '))

        #o if verifica se idade é valida
        if idade > 0 and idade < 100:
            print("idade:", idade)
            # o break sai do while
            break
        else:
            print("idade invalida")
    except ValueError:
        # caso der erro execute aqui
        print("digite sua idade em numeros. ex 26")