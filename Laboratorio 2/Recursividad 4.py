# Ejercicio 4: Escribe una función recursiva que imprima la pirámide de números invertidos del 1 al n.

def imprimir_piramide_invertida(n, nivel=1):
    # Comprueba si el nivel actual es mayor que el número máximo n. Si lo es, termina la recursión.
    if nivel > n:
        return
    # Imprime una fila de la pirámide invertida. Utiliza la función join 
    # para convertir los números del nivel actual al 1 en una cadena, separados por espacios.
    print(" " * (n - nivel) + " ".join(str(i) for i in range(nivel, 0, -1)))
    # Llama recursivamente a la función imprimir_piramide_invertida con el siguiente nivel. 
    # Esto imprime la siguiente fila de la pirámide invertida.
    imprimir_piramide_invertida(n, nivel + 1)
n = 5
imprimir_piramide_invertida(n) 