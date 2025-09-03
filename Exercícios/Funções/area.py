def calcular_area(altura, largura):

    return altura * largura;

alturaa = int(input("Digite a altura: "))
larguraa = int(input("Digite a largura: "))

area = calcular_area(alturaa, larguraa)

print(f"A area eh: {area}")