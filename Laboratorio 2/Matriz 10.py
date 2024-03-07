# 10)Suma dos matrices de diferentes tamaños.

import numpy as np

# Definimos dos matrices de diferentes tamaños
matriz1 = np.array([[1, 2, 3],
                    [4, 5, 6]])

matriz2 = np.array([[7, 8, 9],
                    [10, 11, 12],
                    [13, 14, 15]])

# Verificamos las dimensiones de las matrices
print("Dimensiones de la matriz 1:", matriz1.shape)
print("Dimensiones de la matriz 2:", matriz2.shape)

# Añadimos nuevas dimensiones a la matriz más pequeña para hacerla compatible para la suma
# En este caso, añadimos una dimensión adicional al principio (eje 0) para que tenga el mismo número de filas que la otra matriz
if matriz1.shape[0] < matriz2.shape[0]:
    matriz1 = np.pad(matriz1, ((0, matriz2.shape[0] - matriz1.shape[0]), (0, 0)), mode='constant')
elif matriz1.shape[0] > matriz2.shape[0]:
    matriz2 = np.pad(matriz2, ((0, matriz1.shape[0] - matriz2.shape[0]), (0, 0)), mode='constant')

# Sumamos las matrices
resultado = matriz1 + matriz2

print("La matriz resultante después de la suma es:")
print(resultado)
