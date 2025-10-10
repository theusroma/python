#CRIE UM PROGRAMA QUE LEIA NÚMEROS DIGITADOS PELO USUÁRIO E GRAVE EM UM ARQUIVO

num = input("Digite um numero: ")
with open("numero.txt", "w") as arq_destino:
    arq_destino.write(num)

    print("armazenado com sucesso")
    
