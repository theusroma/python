'''PEÇA AO USUARIO PARA DIGITAR O NOME DE 5 ALUNOS. GRAVE ESSES NOMES
EM UM ARQUIVO CHAMADO alunos.txt DEPOIS REABRA O ARQUIVO E MOSTRE NA TELA
A LISTA DE ALUNOS CADASTRADOS'''

lista = []  #crio a lista

for i in range(5):
    alunos = input(f"Digite o nome do aluno {i + 1}: ")
    lista.append(alunos)

with open("aluno.txt", "w") as arquivo:
    for alunos in lista:
        arquivo.write(alunos + "\n")
print("deu certo")

with open("aluno.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha)

