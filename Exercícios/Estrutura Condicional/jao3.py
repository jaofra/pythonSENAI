while True:
    try:
        ano = int(input('Digite o ano de nascimento: '))

        idade = 2024 - ano
        if idade < 0:
            print("data invalida")
        if idade > 120:
            print("idade invalida")
        faixa_etaria = ""
        if idade > 2007:
            print("menor de idade")
        elif idade < 2006:
            print("idade maior de idade")


        print("voce tem {} anos.".format(idade))
    except ValueError:
        print("digite novate")
