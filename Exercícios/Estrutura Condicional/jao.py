import random

print("media")
print("-"*70)
while True:
    numero1 = int(input("Digite um valor: "))
    numero2 = int(input("Digite outro valor: "))

    media: float = (numero1+numero2)/2

    if media < 70: reprovado = media
    elif media > 70: aprovado = media
