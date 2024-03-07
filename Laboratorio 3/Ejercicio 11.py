# EJERCICIO 11
# Escriba una función que reciba un conjunto de números y
# devuelva un conjunto con los números que están ordenados de menor a mayor.

def numeros_ordenados(conjunto):
    # Convierte el conjunto a una lista, ordena la lista y luego vuelve a convertirla en un conjunto
    conjunto_ordenado = set(sorted(list(conjunto)))
    return conjunto_ordenado

# Ejemplo de uso:
conjunto_original = {5, 2, 8, 1, 3}
conjunto_resultante = numeros_ordenados(conjunto_original)

print(conjunto_resultante)
