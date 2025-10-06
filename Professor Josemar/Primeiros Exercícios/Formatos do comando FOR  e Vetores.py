#Formatos do comando FOR

#de 0 até 4
foi i in range(5):
    print (i)


#de 2 até 6
for i in range(2, 7)
    print(i)


#de 10 até 0, de -2 em -2
for in range(10, -1, -2)
    print(i)


#percorrendo listas
frutas = ["maça", "banana", "uva"]
for i in frutas:
    print(i)


#percorrendo strings
for letra in "Python":
    print(letra)


#percorrendo tuplas
numeros = (10, 20, 30)
for i in numeros:
    print(i)


#percorrendo dicionarios
pessoa = {"nome": "Lambarildo", "idade": 23, "cidade": "Recife"}

for i pessoa:
    print(i)
for i, j in pessoa.items():
    print(i "->", j)


#For com enumerate() Permite acessar o índice e o valor ao mesmo tempo
nomes = ["Ana", "Bruno", "Carlos"]
for i, nome in enumerate(nomes):
    print(i, nome)


#For com zip() Percorre duas (ou mais) listas ao mesmo tempo
alunos = ["Ana", "Bruno", "Carlos"]
notas = [8, 9, 7]
for aluno, nota in zip(alunos, notas):
    print(aluno, "tirou", nota)


#Criando lista (vetores)
#Vetor vazio
vetor []

#Vetor com valores
vetor = [10, 20, 30, 40]

#Adicionais e removendo
vetor.append(50) #adiciona no fim
vetor.insert(2, 15) #insere 2 na posicao
vetor.pop() #remove o ultimo elemento
vetor.remove(20) #remove o valor 20


#Criando uma matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

#Percorrendo a matriz
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()
    
