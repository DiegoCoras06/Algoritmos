# Ejercicio 1: Escribe una función recursiva que imprima los números pares del 1 al 100.

def imprimir_pares(num):
    """
    num (int): El número actual que se está evaluando.
    """
    if num <= 100:  # Verificar si el número actual es menor o igual a 100
        if num % 2 == 0:  # Verificar si el número actual es par
            print(num)  # Imprimir el número par
        imprimir_pares(num + 1)  # Llamar recursivamente a la función con el siguiente número

imprimir_pares(1)