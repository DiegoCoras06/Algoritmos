
# EJERCICIO 12
# Escriba una función que reciba un conjunto de
# números y devuelva un conjunto con los números que están ordenados de mayor a menor.

def numeros_ordenados_descendente(conjunto_numeros):
    lista_ordenada = sorted(conjunto_numeros, reverse=True)
    conjunto_ordenado = set(lista_ordenada)

    return conjunto_ordenado

conjunto_original = {10, 12, 85, 13, 63}
resultado = numeros_ordenados_descendente(conjunto_original)

print("Números ordenados de mayor a menor:", resultado)