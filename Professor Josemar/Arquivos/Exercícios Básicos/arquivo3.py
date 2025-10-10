#PROGRAMA QUE COPIA O CONTEUDO DE ARQUIVO PARA OUTRO
with open("arquivo.txt", "r") as arq_origem:
    conteudo = arq_origem.read()

with open("copia.txt", "w") as arq_destino:
    arq_destino.write(conteudo)

print("Arquivo copiado com sucesso!")
