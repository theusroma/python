import pandas as pd
import matplotlib.pyplot as plt

receita = pd.read_csv("vendas_loja.csv")

receita["Região"].hist()
plt.title("RECEITA POR REGIÃO")
plt.xlabel("Região")
plt.ylabel("Receita")
plt.show()

receita_por_regiao = receita.groupby("Região")["Nota"].mean()
print(receita_por_regiao)

receita_por_regiao.plot(kind="bar")
plt.show()