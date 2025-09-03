while True:
    print("-----")
    print("[1] SOMA")
    print("[2] SUBTRACAO")
    print("[3] MULTIPLICACAO")
    print("[4] DIVISAO")
    print("[5] SAIR")

    print("-----")
    
    opcao = int(input("Digite a opção desejada: "))
    
    
    match opcao:
        case 1:
            num1 = int(input("Digite o primeiro valor: "))
            num2 = int(input("Digite o segundo valor: "))
            soma = num1 + num2
            print("SOMA: ", soma)
    
        case 2:
            num1 = int(input("Digite o primeiro valor: "))
            num2 = int(input("Digite o segundo valor: "))
            sub = num1 - num2
            print("SUBTRACAO: ", sub)
            
        case 3:
            num1 = int(input("Digite o primeiro valor: "))
            num2 = int(input("Digite o segundo valor: "))
            multi = num1 * num2
            print("MULTIPLICACAO: ", multi)
            
        case 4:
            num1 = int(input("Digite o primeiro valor: "))
            num2 = int(input("Digite o segundo valor: "))
            div = num1 / num2
            print("DIVISAO: ", div)

        case 5:
            print("Saindo...")
            break
        
        case _:
            print("Opção inválida! Tente novamente.")
