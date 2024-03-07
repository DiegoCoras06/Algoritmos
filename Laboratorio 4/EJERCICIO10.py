# Desarrollar el código de buscar nodo en la lista enlazada simple.

class Nodo:
    def _init_(self, dato):
        self.dato = dato  # Guarda el dato proporcionado en el atributo "dato"
        self.siguiente = None  # Inicializa el atributo "siguiente" como None

class ListaEnlazada:
    def _init_(self):
        self.inicio = None  # Inicializa el atributo "inicio" como None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)  # Crea un nuevo nodo con el dato proporcionado
        if not self.inicio:
            self.inicio = nuevo_nodo  # Si la lista está vacía, establece el nuevo nodo como el inicio
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo  # Agrega el nuevo nodo al final de la lista

    def buscar(self, valor):
        actual = self.inicio  # Comienza desde el nodo inicial
        while actual:
            if actual.dato == valor:  # Si se encuentra un nodo con el valor deseado, retorna ese nodo
                return actual
            actual = actual.siguiente  # Se mueve al siguiente nodo en la lista
        return None  # Retorna None si el valor no se encuentra en la lista

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)

# Buscar un nodo con valor 2
nodo_buscado = lista.buscar(2)
if nodo_buscado:
    print("Nodo encontrado con valor:", nodo_buscado.dato)
else:
    print("Nodo no encontrado")