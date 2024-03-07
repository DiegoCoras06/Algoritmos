# Ejercicio 3: Escribe una función que encuentre el elemento máximo de una matriz.
import numpy as np

def encontrar_maximo(matriz):
    """
    matriz (numpy.ndarray): La matriz de entrada.
    Returns:
    float: El valor del elemento máximo.
    """
    maximo = np.max(matriz)  # Utilizamos np.max() para encontrar el elemento máximo
    return maximo

# Ejemplo de uso:
matriz_ejemplo = np.array([[1, 2, 3],
                           [4, 9, 6],
                           [7, 8, 5]])

maximo = encontrar_maximo(matriz_ejemplo)
print("El elemento máximo de la matriz es:", maximo)