# EJERCICIO 19
# Escriba una función que reciba un conjunto de números y
# devuelva un conjunto con los números que están ordenados de menor a mayor y que no están duplicados.
def numeros_ordenados_y_sin_duplicados(conjunto):
    numeros_ordenados = sorted(list(conjunto))
    return set(numeros_ordenados)

conjunto_de_numeros = {5, 3, 8, 2, 5, 8, 1, 2, 9, 4}
conjunto_ordenado_sin_duplicados = numeros_ordenados_y_sin_duplicados(conjunto_de_numeros)
print(conjunto_ordenado_sin_duplicados)
