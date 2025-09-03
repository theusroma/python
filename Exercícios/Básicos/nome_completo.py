# Solicita o nome completo do usuário
nome_completo = input("Digite seu nome completo: ")

# 1. Remove espaços em branco no início e no fim
nome_formatado = nome_completo.strip()

# 2. Converte todas as letras para maiúsculas
nome_formatado = nome_formatado.upper()

# 3. Substitui todas as letras 'A' pela letra 'O'
nome_formatado = nome_formatado.replace('A', 'O')

# Exibe o resultado final
print(f"Nome formatado: {nome_formatado}")
