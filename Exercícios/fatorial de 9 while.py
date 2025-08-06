fatorial = 1
aux = 1
contador = 0;

while (contador <= 8):
    
    fatorial = fatorial * aux;
    aux = aux + 1;
    contador = contador + 1;
    print("O fatorial de", contador, "é: ", fatorial)