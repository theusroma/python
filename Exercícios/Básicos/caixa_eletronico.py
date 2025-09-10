menu = True
saldo = 0

while menu:
    print("==CAIXA ELETRÔNICO==")
    print("1 - Depositar")
    print("2. Sacar")
    print("3. Ver Saldo")
    print("4. Sair")


    escolha = int(input("Selecione: "))

    match escolha:
        case 1:
            print(f"SALDO ATUAL: {saldo}")
            deposito = int(input("Selecione o valor que deseja depositar: "))
            saldo = saldo + deposito
            
        case 2:
            print(f"SALDO ATUAL: {saldo}")
            saque = int(input("Digite o valor que quer sacar: "))
            if saque < saldo:
                saldo = saldo - saque
            else:
                print("Saldo insuficiente")

        case 3:
            print(f"O saldo é: {saldo}")

        case 4:
            print("Saindo...")
            menu = False