# EJERCICIO 13
# Escriba una función que reciba un conjunto de números y
# devuelva un conjunto con los números que están duplicados.

def numeros_duplicados(conjunto):
    duplicados = set()

    # Utilizamos el conjunto original para evitar crear una lista en cada iteración
    for num in conjunto:
        # Utilizamos el método count() solo una vez para obtener el número de ocurrencias de num
        if list(conjunto).count(num) > 1:
            duplicados.add(num)

    return duplicados

conjunto = {1, 2, 2, 2, 3, 4, 4, 3}
print(numeros_duplicados(conjunto))