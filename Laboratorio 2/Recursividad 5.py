# Ejercicio 5: Escribe una función recursiva que imprima la tabla de multiplicar del n.

def imprimir_tabla_multiplicar(n, multiplicador=1):
    # límite superior de la tabla de multiplicar. 
    # Si lo es, termina la recursión.
    if multiplicador > 10:
        return
    # Imprime la multiplicación del número n por el multiplicador actual.
    print(f"{n} x {multiplicador} = {n * multiplicador}")
    # Llama recursivamente a la función imprimir_tabla_multiplicar con el mismo número n,
    # pero con el siguiente multiplicador. 
    # Esto imprime la siguiente fila de la tabla de multiplicar.
    imprimir_tabla_multiplicar(n, multiplicador + 1)

# Ejemplo de uso:
n = 5
imprimir_tabla_multiplicar(n) 