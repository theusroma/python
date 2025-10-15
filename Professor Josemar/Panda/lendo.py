import pandas as pd

#lendo o arquivo
dados = pd.read_csv("dados.csv")

#filtrar apenas alunos de computação
comp = dados[dados["Curso"] == "Computação"]
print(comp)

#ordenar por nota (decrescente)
ordenado = dados.sort_values(by="Nota", ascending=False)
print(ordenado)