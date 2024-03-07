
# Crea una lista con nodos que contengan datos duplicados, elimina todos los nodos duplicados, dejando
# solo una instancia de cada dato e imprime la lista hacia adelante y hacia atrás.

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, nuevo_dato):
        nuevo_nodo = Nodo(nuevo_dato)
        # Aquí se verifica si la lista enlazada está vacía o no. Si self.
        # cabeza es None, significa que la lista está vacía. 
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        # Si la lista no está vacía, se inicializa un puntero llamado 
        # ultimo que apunta al primer nodo de la lista (self.cabeza).
        ultimo = self.cabeza
        # Luego, se recorre la lista hasta encontrar el último nodo 
        while ultimo.siguiente:
            ultimo = ultimo.siguiente
        ultimo.siguiente = nuevo_nodo

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente

    def imprimir_reversa(self):
        anterior = None
        actual = self.cabeza
        # Se inicia un ciclo while mientras actual no sea None, para recorrer la lista.
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior
        
        actual = self.cabeza
        # Se imprime la lista en orden inverso desde la cabeza actualizada.
        while actual:
            print(actual.dato, end=" ")  
            actual = actual.siguiente

    def eliminar_duplicados(self):
        # Se obtiene el primer nodo en la variable actual.
        actual = self.cabeza
        datos_vistos = set()
        # Se agrega el dato del primer nodo al conjunto.
        datos_vistos.add(self.cabeza.dato)
        # Se guarda el primer nodo en la variable anterior.
        anterior = self.cabeza
        actual = actual.siguiente
        # Se inicia un ciclo mientras actual no sea None para recorrer la lista.
        while actual:
            if actual.dato in datos_vistos:
                anterior.siguiente = actual.siguiente
                actual = actual.siguiente
            else:
                datos_vistos.add(actual.dato)
                anterior = actual
                actual = actual.siguiente
                

lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(2)  
lista.agregar(4)
lista.agregar(1)

print("Lista original:")
lista.imprimir()

lista.eliminar_duplicados()

print("\nLista sin duplicados:")   
lista.imprimir()

print("\nLista inversa sin duplicados:")
lista.imprimir_reversa()