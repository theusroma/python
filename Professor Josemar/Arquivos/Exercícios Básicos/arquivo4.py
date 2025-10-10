vogais = "AEIOUaeiou"
with open("animais.txt", "r") as arq:
    for linha in arq:
        if linha and linha [0] in vogais:
            print(linha.strip())
