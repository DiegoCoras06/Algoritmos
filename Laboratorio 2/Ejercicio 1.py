# Ejercicio parte 01:

# Ejercicio 1: Crea una matriz de números aleatorios de tamaño 100x100.
import numpy as np
# Definimos las dimensiones de la matriz
filas = 100
columnas = 100
# Creamos la matriz de números aleatorios
matriz_aleatoria = np.random.rand(filas, columnas)

print("Matriz de números aleatorios de tamaño 100x100:")
print(matriz_aleatoria)