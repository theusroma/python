import random

# Gera um número inteiro entre 1 e 10 (incluindo 1 e 10)
aleatorio = random.randint(1, 100)
tentativas = 10;
num = 0

print(f"Número inteiro aleatório: {aleatorio}")

while num != aleatorio and tentativas > 0:
    num = int(input("Digite um número: "))
    tentativas = tentativas - 1

    if num < aleatorio:
        print("O numero é maior")
    elif num > aleatorio:
        print("O numero é menor")
    elif num == aleatorio:
        print("Voce acertou")

if tentativas == 0:
    print("Suas tentativas acabaram")



