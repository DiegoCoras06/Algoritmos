
# EJERCICIO 6
# Escriba una función que reciba dos
# conjuntos de números y devuelva un conjunto con los
# números que están en el segundo conjunto pero no en el primero.

conjunto_a = {5, 2, 3, 4, 5}
conjunto_b = {3, 5, 2, 9, 7}
def numeros_en_segundo_no_en_primero(conjunto_a, conjunto_b):
    diferencia = conjunto_b.difference(conjunto_a)
    
    return diferencia
resultado = numeros_en_segundo_no_en_primero(conjunto_a, conjunto_b)

print("Números en el segundo conjunto pero no en el primero:", resultado)