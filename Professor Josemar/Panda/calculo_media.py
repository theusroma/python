import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("dados.csv")

dados["Nota"].hist()
plt.title("Distribuição das Notas")
plt.xlabel("Nota")
plt.ylabel("Quantidade de Alunos")
plt.show()

media_por_curso = dados.groupby("Curso")["Nota"].mean()
print(media_por_curso)

media_por_curso.plot(kind="bar")
plt.title("Média de Notas por Curso")
plt.ylabel("Nota Média")
plt.show()