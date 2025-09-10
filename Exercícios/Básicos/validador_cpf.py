cpf = input("Digite seu CPF:")

# Coloque a lista de CPFs inválidos aqui
cpfs_invalidos = ["00000000000", "11111111111", ...]

if len(cpf) != 11:
    print("O CPF deve ter exatamente 11 dígitos.")
elif not cpf.isdigit():
    print("O CPF deve conter apenas números.")
elif cpf in cpfs_invalidos:
    print("CPF inválido por sequência.")
else:
    print("CPF válido!")