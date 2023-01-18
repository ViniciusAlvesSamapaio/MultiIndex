import pandas as pd

# MultiIndex Arrays

infor = [[1, 2, 3, 4], ["dia", "semana", "mes", "ano"]]

t = pd.MultiIndex.from_arrays(infor)
print (t)


# MultiIndex Product 

numeros = [0, 1, 2]
cores = ["verde", "azul", "roxo"]
b = pd.MultiIndex.from_product([numeros, cores], names = ["numero","cor"])
print(b)
