
num1 = int(input("Digite a primeira medida: "))
num2 = int(input("Digite a segunda medida: "))
num3 = int(input("Digite a terceira medida: "))

if num1 != num2 and num1 != num3:
    print("O triângulo é ESCALENO")
elif num2 != num3 and num2 != num1:
    print("O triângulo é ESCALENO")



if num1 == num2 and num1 == num3:
    print("O triângulo é EQUILATERO")
    

if num1 == num2 and num1 != num3:
    print("O triângulo é ISOSCELES")
elif num2 == num3 and num1 != num1:
    print("O triângulo é ISOSCELES")
elif num3 == num1 and num1 != num2:
    print("O triângulo é ISOSCELES")



