# 6)Crea una matriz de números reales.

import numpy as np
# Creamos una lista de listas que representan las filas de la matriz.
# Cada sublista representa una fila de la matriz, y contiene números reales.
# En este ejemplo, creamos una matriz de 3x3.
matriz = [
        [1.5, 2.3, 3.7],
        [4.2, 5.1, 6.8],
        [7.4, 8.6, 9.9]]
# Convertimos la lista de listas en una matriz NumPy usando la función array().
matriz_numpy = np.array(matriz)
# Imprimimos la matriz original.
print("Matriz original:")
print(matriz)
# Imprimimos la matriz NumPy.
print("\nMatriz NumPy:")
print(matriz_numpy)