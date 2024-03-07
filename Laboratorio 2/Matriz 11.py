# 11)Multiplica una matriz por un número.

import numpy as np

# Definimos una matriz
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Definimos el número por el cual queremos multiplicar la matriz
numero = 2

# Multiplicamos la matriz por el número
resultado = matriz * numero

print("Matriz original:")
print(matriz)

print("\nMatriz multiplicada por", numero, ":")
print(resultado)
