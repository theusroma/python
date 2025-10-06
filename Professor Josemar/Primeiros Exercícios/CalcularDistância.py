import math

x1 = int(input("Digite o valor de x1: "))
y1 = int(input("Digite o valor de y1: "))

x2 = int(input("Digite o valor de x2: "))
y2 = int(input("Digite o valor de y2: "))


um = ((x2 - x1) ** 2)
dois = ((y2 - y1) ** 2)
soma = um + dois

distancia = math.sqrt(soma)

print("(x2 - x1) ** 2")
print(um)

print("(y2 - y1) ** 2")
print(dois)

print("distancia")
print(distancia)


rounded = round(distancia, 2)
print(rounded)

