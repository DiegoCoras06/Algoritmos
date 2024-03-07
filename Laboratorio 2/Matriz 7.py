
# 7)Crea una matriz de números complejos.
import numpy as np

# Creamos una matriz de números complejos utilizando la función array() de NumPy.
# En este ejemplo, creamos una matriz de 2x2 con números complejos.
matriz_compleja = np.array([
    [1 + 2j, 3 - 4j],
    [5j, 6 - 7j]
], dtype=complex)  # Especificamos el tipo de datos como 'complex' para números complejos.

# Imprimimos la matriz de números complejos.
print("Matriz de números complejos:")
print(matriz_compleja)