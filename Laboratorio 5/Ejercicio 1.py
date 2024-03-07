# Crea una lista con al menos 4 nodos, duplica cada nodo de la lista e imprime la lista original y la lista
# duplicada hacia adelante y hacia atrás.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

# Definir la clase ListaEnlazada
class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar_nodo(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    def duplicar_nodos(self):
        # Obtiene el primer nodo en la variable nodo_actual.
        nodo_actual = self.primero
        # Recorre la lista mientras nodo_actual no sea None.
        while nodo_actual is not None:
            # Crea un nuevo nodo con el mismo dato que nodo_actual.
            nuevo_nodo = Nodo(nodo_actual.dato)
            nuevo_nodo.siguiente = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
            # Si el nuevo nodo no es el último:
            if nuevo_nodo.siguiente is not None:
                nuevo_nodo.siguiente.anterior = nuevo_nodo
            # Si nodo_actual era el último,
            if nodo_actual == self.ultimo:
                self.ultimo = nuevo_nodo
            nodo_actual = nuevo_nodo.siguiente

    def imprimir_adelante(self):
        # Obtiene el primer nodo en la variable nodo_actual.
        nodo_actual = self.primero
        # Recorre la lista mientras nodo_actual no sea None.
        while nodo_actual is not None:
            print(nodo_actual.dato)
            # Avanza nodo_actual al siguiente nodo.
            nodo_actual = nodo_actual.siguiente

    def imprimir_atras(self):
        # Obtiene el último nodo en la variable nodo_actual.
        nodo_actual = self.ultimo
        # Recorre la lista mientras nodo_actual no sea None.
        while nodo_actual is not None:
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.anterior

# Crear una instancia de la lista enlazada
lista = ListaEnlazada()

# Agregar nodos a la lista
lista.agregar_nodo(1)
lista.agregar_nodo(2)
lista.agregar_nodo(3)
lista.agregar_nodo(4)

# Duplicar los nodos
lista.duplicar_nodos()

# Imprimir la lista original hacia adelante
print("Lista original hacia adelante:")
lista.imprimir_adelante()

# Imprimir la lista duplicada hacia adelante
print("Lista duplicada hacia adelante:")
lista.imprimir_adelante()

# Imprimir la lista original hacia atrás
print("Lista original hacia atrás:")
lista.imprimir_atras()

# Imprimir la lista duplicada hacia atrás
print("Lista duplicada hacia atrás:")
lista.imprimir_atras()