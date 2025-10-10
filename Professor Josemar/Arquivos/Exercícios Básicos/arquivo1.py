with open("arquivo.txt", "r") as arq:
    conteudo = arq.read()
    print(conteudo)
    print("--")

with open("arquivo.txt", "r") as arq:
    for linha in arq:
        print(linha.strip())
        print("--")

with open("arquivo.txt", "r") as arq:
    linhas = arq.readlines()
    print(linhas)

print("")
print("")
print("")
