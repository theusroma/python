import pandas as pd
import matplotlib.pyplot as plt

#lendo o arquivo
vendas = pd.read_csv("vendas_loja.csv")
print(vendas)

total_vendas = vendas.groupby("Quantidade")["Preço Unitário"].mean()
print(total_vendas)
