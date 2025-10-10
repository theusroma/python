with open("animais.txt", "r") as arq:
    for linha in arq:
        if "gato" in linha:
            print(linha)
