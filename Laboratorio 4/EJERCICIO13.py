# Implementa una función que concatene dos listas enlazadas simples.

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

    def mostrar(self):
        actual = self.inicio
        while actual:
            print(actual.dato, end=' -> ')  # Imprime el dato del nodo actual y una flecha "->"
            actual = actual.siguiente  # Se mueve al siguiente nodo en la lista
        print("None")  # Imprime "None" al final para indicar que la lista ha terminado

def concatenar_listas(lista1, lista2):
    if not lista1.inicio:  # Si la lista1 está vacía, simplemente retorna lista2
        return lista2
    if not lista2.inicio:  # Si la lista2 está vacía, simplemente retorna lista1
        return lista1

    actual = lista1.inicio
    while actual.siguiente:  # Recorre la lista1 hasta el último nodo
        actual = actual.siguiente
    actual.siguiente = lista2.inicio  # Conecta el último nodo de lista1 con el primer nodo de lista2
    return lista1 