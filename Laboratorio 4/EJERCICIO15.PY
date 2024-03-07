# Implementa una función que invierta el orden de una lista enlazada simple.

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

def invertir_lista_enlazada_simple(lista):
    # Inicializamos tres punteros: actual, previo y siguiente
    actual = lista.primero
    previo = None
    siguiente = None

    # Recorremos la lista mientras hay nodos
    while actual:
        # Guardamos el siguiente nodo en la variable siguiente
        siguiente = actual.siguiente

        # Invertimos la dirección del enlace
        actual.siguiente = previo

        # Actualizamos los punteros para avanzar en la lista
        previo = actual
        actual = siguiente

    # Al finalizar el bucle, previo apunta al último nodo invertido,
    # por lo que lo establecemos como el nuevo primero de la lista
    lista.primero = previo

# Función para imprimir la lista enlazada (solo para fines de demostración)
def imprimir_lista_enlazada_simple(lista):
    actual = lista.primero
    while actual:
        print(actual.dato, end=" -> ")
        actual = actual.siguiente
    print("None")

# Ejemplo de uso
if __name__ == "__main__":
    # Creamos una lista enlazada simple
    lista = Nodo(1)
    lista.siguiente = Nodo(2)
    lista.siguiente.siguiente = Nodo(3)
    lista.siguiente.siguiente.siguiente = Nodo(4)

    print("Lista original:")
    imprimir_lista_enlazada_simple(lista)

    # Invertimos el orden de la lista
    invertir_lista_enlazada_simple(lista)

    print("\nLista invertida:")
    imprimir_lista_enlazada_simple(lista)