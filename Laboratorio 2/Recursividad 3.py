# Ejercicio 3: Escribe una función recursiva que imprima la pirámide de números del 1 al n.

def imprimir_piramide(n, nivel=1):
    # Comprueba si el nivel actual es mayor que el número máximo n. Si lo es, termina la recursión.
    if nivel > n:
        return
    """Imprime una fila de la pirámide. Calcula la cantidad de 
    espacios en blanco a imprimir antes de los números para centrar la fila. 
    Luego, utiliza la función join para convertir los números del 1 al nivel 
    actual en una cadena, separados por espacios."""
    print(" " * (n - nivel) + " ".join(str(i) for i in range(1, nivel + 1)))
    # Llama recursivamente a la función imprimir_piramide 
    # con el siguiente nivel. Esto imprime la siguiente fila de la pirámide.
    imprimir_piramide(n, nivel + 1)
n = 5
imprimir_piramide(n)