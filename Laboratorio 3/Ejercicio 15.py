# EJERCICIO 15
# Escriba una función que reciba un conjunto de números y
# devuelva un conjunto con los números que son primos y
# están ordenados de menor a mayor.
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def numeros_primos_ordenados(conjunto):
    primos = {num for num in conjunto if es_primo(num)}
    return sorted(primos)