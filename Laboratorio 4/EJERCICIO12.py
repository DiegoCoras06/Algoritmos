# Crea una función que devuelva la longitud de una lista enlazada simple.

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

    def longitud(self):
        contador = 0  # Inicializa un contador para contar la longitud de la lista
        actual = self.inicio  # Comienza desde el nodo inicial
        while actual:
            contador += 1  # Incrementa el contador en 1 por cada nodo visitado
            actual = actual.siguiente  # Se mueve al siguiente nodo en la lista
        return contador  # Retorna la longitud de la lista

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)

longitud = lista.longitud()
print("Longitud de la lista:", longitud)