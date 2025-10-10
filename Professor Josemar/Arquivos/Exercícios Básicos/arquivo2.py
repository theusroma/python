#LER UM ARQUIVO DE TEXTO E CONTAR QUANTAS PALAVARAS ELE POSSUI
with open("arquivo.txt", "r") as arq:
    conteudo = arq.read()
    palavras = conteudo.split() #o comando split separa a palavra pelo espaço
    print("Quantidade de poalavras: ", len(palavras))
    
