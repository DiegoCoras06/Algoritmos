# Crea una función que elimine los nodos duplicados de una lista enlazada simple.
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

def eliminar_duplicados(lista):
    if lista is None:
        return lista  # Si la lista está vacía, no hay nada que hacer

    valores_vistos = set()  # Utilizamos un conjunto para registrar los valores vistos
    current = lista
    valores_vistos.add(current.valor)  # Agregamos el primer valor a los valores vistos

    while current.siguiente:
        if current.siguiente.valor in valores_vistos:  # Si el valor siguiente ya ha sido visto
            current.siguiente = current.siguiente.siguiente  # Eliminamos el nodo duplicado
        else:
            valores_vistos.add(current.siguiente.valor)  # Agregamos el valor a los valores vistos
            current = current.siguiente  # Movemos el puntero al siguiente nodo

    return lista  # Devolvemos la lista modificada


# Ejemplo de uso
def imprimir_lista(lista):
    current = lista
    while current:
        print(current.valor, end=" ")
        current = current.siguiente
    print()

# Creamos una lista enlazada con duplicados
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(2)
nodo5 = Nodo(4)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5

print("Lista original:")
imprimir_lista(nodo1)

# Eliminamos los nodos duplicados
nodo1 = eliminar_duplicados(nodo1)

print("Lista sin duplicados:")
imprimir_lista(nodo1)