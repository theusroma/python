'''LEIA UM ARQUIVO COM DIVERSOS NOMES DE ANIMAIS, PEÇA PRO
USUÁRIO DIGITAR UM ANIMAL E VERIFIQUE SE EXISTE NO MESMO ARQUIVO'''

nome = input("Digite o nome do animal: ")

with open("animais.txt", "r") as arquivo:
    for linha in arquivo:
        if nome in linha:
            print(nome.strip())
    
