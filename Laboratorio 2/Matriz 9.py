# 9)Accede al elemento central de una matriz.

import numpy as np

# Creamos una matriz de ejemplo utilizando NumPy
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Calculamos las dimensiones de la matriz
filas, columnas = matriz.shape
# Calculamos el índice del elemento central
fila_central = filas // 2
columna_central = columnas // 2
# Accedemos al elemento central
elemento_central = matriz[fila_central, columna_central]

print("El elemento central de la matriz es:", elemento_central)