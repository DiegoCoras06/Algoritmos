# Ejercicio 2: Calcula la media, la mediana y la desviación estándar de los elementos de una matriz.

import numpy as np

# Definimos una matriz
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
# Calculamos la media de los elementos de la matriz
media = np.mean(matriz)
# Calculamos la mediana de los elementos de la matriz
mediana = np.median(matriz)

# Calculamos la desviación estándar de los elementos de la matriz
desviacion_estandar = np.std(matriz)

print("Matriz:")
print(matriz)

print("\nLa media de los elementos de la matriz es:", media)
print("La mediana de los elementos de la matriz es:", mediana)
print("La desviación estándar de los elementos de la matriz es:", desviacion_estandar)