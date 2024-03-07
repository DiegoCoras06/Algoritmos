# EJERCICIO 14
# Escriba una función que reciba un conjunto de números
# y devuelva un conjunto con los números que no están duplicados.

def eliminar_duplicados(conjunto_numeros):

    lista_original = list(conjunto_numeros)

    lista_sin_duplicados = sorted(set(lista_original))

    conjunto_sin_duplicados = set(lista_sin_duplicados)

    return conjunto_sin_duplicados

conjunto_original = {5, 2, 8, 1, 3, 5, 2, 8}
resultado = eliminar_duplicados(conjunto_original)
print("Números sin duplicados:", resultado)
