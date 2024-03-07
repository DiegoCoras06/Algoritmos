# Ejercicio 5: Escribe una función que encuentre la matriz de covarianza de dos matrices.
import numpy as np

def matriz_covarianza(matriz1, matriz2):
    """
    Calcula la matriz de covarianza entre dos matrices.
    Returns:
    numpy.ndarray: La matriz de covarianza entre las dos matrices.
    """
    covarianza = np.cov(matriz1, matriz2)
    return covarianza

# Ejemplo de uso:
matriz1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matriz2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

covarianza = matriz_covarianza(matriz1, matriz2)
print("La matriz de covarianza entre las dos matrices es:")
print(covarianza)