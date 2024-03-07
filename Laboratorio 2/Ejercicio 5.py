# Escribe una función que encuentre la submatriz de mayor suma de una matriz.


def submatriz_mayor_suma(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    max_suma = float('-inf')  # Inicializa la variable max_suma con un valor muy pequeño para comparar con las sumas de las submatrices.
    submatriz = None  # Inicializa la variable submatriz para almacenar las coordenadas de la submatriz de mayor suma.

    # Iterar sobre todas las posibles submatrices
    for fila_inicio in range(filas):
        for fila_fin in range(fila_inicio, filas):
            for col_inicio in range(columnas):
                for col_fin in range(col_inicio, columnas):
                    suma_actual = 0
                    # Calcular la suma de la submatriz actual
                    for i in range(fila_inicio, fila_fin + 1):
                        for j in range(col_inicio, col_fin + 1):
                            suma_actual += matriz[i][j]
                    # Actualizar la submatriz de mayor suma si corresponde
                    if suma_actual > max_suma:
                        max_suma = suma_actual
                        submatriz = (fila_inicio, fila_fin, col_inicio, col_fin)

    return submatriz, max_suma

# Ejemplo de uso
matriz_ejemplo = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

submatriz, suma = submatriz_mayor_suma(matriz_ejemplo)
print("Submatriz de mayor suma:", submatriz)
print("Suma de la submatriz:", suma)