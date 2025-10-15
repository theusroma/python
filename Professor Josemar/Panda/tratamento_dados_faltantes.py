import pandas as pd

dados = pd.read_csv("dados.csv")
print("====DADOS ORIGINAIS====")
print(dados)
print("\n")

print("====VERIFICANDO VALORES FALTANTES====")
print(dados.isnull())
print("\n")

print("====CONTAGEM DE VALORES FALTANTES====")
print(dados.isnull().sum())
print("\n")

dados["Idade"] = dados["Idade"].fillna(dados["Idade"].mean())
dados["Nota"] = dados["Nota"].fillna(dados["Nota"].mean())

print("====DADOS CORRIGIDOS====")
print(dados)
print("\n")

dados.to_csv("dados_corrigidos.csv", index=False)
print("Arquivo 'dados_corrigidos.csv' salvo com sucesso")