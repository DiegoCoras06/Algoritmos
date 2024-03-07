# 12)Calcula la media de los elementos de una matriz.
import numpy as np

# Definimos una matriz
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
# Calculamos la media de los elementos de la matriz
media = np.mean(matriz)

print("Matriz:")
print(matriz)
print("\nLa media de los elementos de la matriz es:", media)
