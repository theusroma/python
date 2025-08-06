n = int(input("Digite um numero: "))
vezes = int(input("Quantas vezes: "))
contador = 0

primeiro = n
segundo = 1


while contador <= vezes:
    print(primeiro)
    proximo = primeiro + segundo;
    segundo = proximo;
    
    contador += 1;