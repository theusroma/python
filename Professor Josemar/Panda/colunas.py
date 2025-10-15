import pandas as pd

dados = pd.read_csv("dados.csv")

#informacaoes basicas
print("INFORMACOES BASICAS")
print(dados.info())
print("\n\n")

#estatiticas descrivitas
print("ESTATITICAS DESCRIVITAS")
print(dados.describe())
print("\n\n")

#coluans e linhas
print("COLUNAS E LINHAS")
print(dados.columns)
print(len(dados))
