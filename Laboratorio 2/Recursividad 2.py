# Ejercicio 2: Escribe una función recursiva que imprima la suma de los números del 1 al n.

def suma_n(n):
    """
    n (int): El número hasta el cual se quiere calcular la suma.
    Returns:
    int: La suma de los números del 1 al n.
    """
    if n == 1:  # Caso base: Si n es igual a 1, la suma es simplemente 1
        return 1
    else:
        return n + suma_n(n - 1)  # Llamar recursivamente a la función con n-1 y sumarlo con n
n = 5
print("La suma de los números del 1 al", n, "es:", suma_n(n))