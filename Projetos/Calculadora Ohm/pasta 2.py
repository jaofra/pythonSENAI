def calcular_tensao(corrente, resistencia):
    return corrente * resistencia

def calcular_corrente(tensao, resistencia):
    return tensao / resistencia

def calcular_resistencia(tensao, corrente):
    return tensao / corrente

def menu():
    print("Escolha o que deseja calcular:")
    print("1. Tensão (V)")
    print("2. Corrente (I)")
    print("3. Resistência (R)")
    print("0. Sair")

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            print("Saindo...")
            break
        elif escolha in ["1", "2", "3"]:
            valor1 = float(input("Insira o primeiro valor: "))
            valor2 = float(input("Insira o segundo valor: "))

            if escolha == "1":
                resultado = calcular_tensao(valor1, valor2)
                print("A tensão é", resultado, "V")
            elif escolha == "2":
                resultado = calcular_corrente(valor1, valor2)
                print("A corrente é", resultado, "A")
            elif escolha == "3":
                resultado = calcular_resistencia(valor1, valor2)
                print("A resistência é", resultado, "Ω")
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()