#Abre o arquivo para leitura
with open("arquivo.csv", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

# Remove quebras de linha e separa por vírgula
dados = [linha.strip().split(",") for linha in linhas]

# Cabeçalho
cabecalho = dados[0]
print(f"{cabecalho[0]:<15} {cabecalho[1]:<10}")
print("-" * 25)

# Linhas da tabela
for linha in dados[1:]:
    print(f"{linha[0]:<15} {linha[1]:<10}")
