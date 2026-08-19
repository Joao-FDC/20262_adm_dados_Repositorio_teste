import pandas as pd

# Ler a base
dados = pd.read_excel("Vendas.xlsx")

print("\nQuantidade de vendas:")
print(len(dados))


print("\nTotal vendido:")
print(dados["Valor Final"].sum())
