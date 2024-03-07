# Crea una lista con al menos 9 nodos, cuenta cuántos nodos tienen un dato par y cuántos tienen un dato
# impar e imprime la lista hacia adelante y hacia atrás.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, nuevo_dato):
        # Aquí se crea un nuevo nodo utilizando la clase Nodo,
        # que contiene el nuevo_dato proporcionado.
        # Este nodo es el que se agregará a la lista enlazada.
        nuevo_nodo = Nodo(nuevo_dato)
        if self.cabeza is None:
            # se asigna nuevo_nodo como la cabeza de la lista (self.cabeza)
            self.cabeza = nuevo_nodo
            return
        ultimo = self.cabeza
        # Este bucle se ejecuta para encontrar el último nodo de la lista enlazada.
        while ultimo.siguiente:
            ultimo = ultimo.siguiente
        ultimo.siguiente = nuevo_nodo

    def imprimir_lista(self):
        temp = self.cabeza
        while temp:
            print(temp.dato, end=" ")
            temp = temp.siguiente

    def imprimir_reversa(self):
        # Se inicializan dos punteros, anterior y actual.
        # actual se inicializa como la cabeza de la lista enlazada,
        # mientras que anterior se inicializa como None
        anterior = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior
        temp = self.cabeza
        while temp:
            print(temp.dato, end=" ")
            temp = temp.siguiente
    # Este bucle itera sobre la lista enlazada mientras temp no sea None        
    def contar_pares_impares(self):
        pares = 0
        impares = 0
        temp = self.cabeza
        while temp:
            if temp.dato % 2 == 0:
                pares += 1
            else:
                impares += 1
            temp = temp.siguiente
        print("\nNúmero de nodos pares:", pares) 
        print("Número de nodos impares:", impares)
                

lista = ListaEnlazada()
lista.agregar(1)  
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)
lista.agregar(5)
lista.agregar(6)
lista.agregar(7)
lista.agregar(8)  
lista.agregar(9)

print("Lista original:")
lista.imprimir_lista()
print("\nLista inversa:")
lista.imprimir_reversa()

lista.contar_pares_impares()