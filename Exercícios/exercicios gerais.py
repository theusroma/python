import math

num1 = int(input("Digite o numero 1: "));
num2 = int(input("Digite o numero 2: "));

print("\n")

soma = num1 + num2;
print("soma dos numeros: ", soma);
print("\n")

produto = num1 * (num2 * num2);
print("produto do primeiro pelo quadrado do segundo: ", produto);
print("\n")

quadrado = num1 * num1;
print("o quadrado do primeiro numero: ", quadrado);
print("\n")

raiz = math.sqrt(num1**2 + num2**2);
print("a raiz quadrado da soma dos quadrados", raiz)
print("\n")

seno = math.sin(num1 - num2)
print("o seno da diferenca do primeiro numero pelo segundo: ", seno);


print("o modulo do primeiro numero: ");
if num1 >= 0:
    print(num1)
    
elif num1 < 0:
    print(num1 * -1)
