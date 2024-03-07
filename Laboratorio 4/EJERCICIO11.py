# Implementa una función que sume todos los nodos de una lista enlazada simple.

class Nodo:
    def _init_(self, valor):
        self.valor = valor  # Almacena el valor proporcionado en el atributo "valor" del nodo
        self.siguiente = None  # Inicializa el atributo "siguiente" como None

def sumar_nodos(lista):
    suma = 0  # Inicializa la variable suma como 0
    nodo_actual = lista  # Comienza desde el nodo proporcionado como argumento
    while nodo_actual is not None:  # Itera mientras haya nodos en la lista
        suma += nodo_actual.valor  # Suma el valor del nodo actual a la suma total
        nodo_actual = nodo_actual.siguiente  # Avanza al siguiente nodo en la lista
    return suma  # Retorna la suma total de los valores de los nodos

# Ejemplo de uso
nodo1 = Nodo(5)  # Crea el primer nodo con valor 5
nodo2 = Nodo(10)  # Crea el segundo nodo con valor 10
nodo3 = Nodo(15)  # Crea el tercer nodo con valor 15

nodo1.siguiente = nodo2  # Establece el siguiente nodo de nodo1 como nodo2
nodo2.siguiente = nodo3  # Establece el siguiente nodo de nodo2 como nodo3

resultado = sumar_nodos(nodo1)  # Calcula la suma de los nodos comenzando desde nodo1
print("La suma de los nodos es:", resultado)  # Imprime el resultado de la suma