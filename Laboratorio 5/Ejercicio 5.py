# Crea una lista con al menos 6 nodos, invierte el orden de la lista (el último elemento se convierte en el
# primero y viceversa) e imprime la lista hacia adelante y hacia atrás.

class Nodo:
  def __init__(self, dato):
    self.dato = dato
    self.siguiente = None
    self.anterior = None

class ListaDoble:
  def __init__(self):
    self.primero = None
    self.ultimo = None

  def insertar(self, dato):
    nuevo = Nodo(dato)
    if self.primero is None:
        self.primero = nuevo
        self.ultimo = nuevo
    else:
        self.ultimo.siguiente = nuevo
        nuevo.anterior = self.ultimo
        self.ultimo = nuevo

  def invertir(self):
    temporal = None
    actual = self.primero
    while actual:
        temporal = actual.siguiente
        actual.siguiente = actual.anterior
        actual.anterior = temporal
        actual = actual.anterior
    self.primero = self.ultimo
    self.ultimo = temporal
  
  def imprimir_adelante(self):
    actual = self.primero
    while actual:
        print(actual.dato, end=" ")
        actual = actual.siguiente

  def imprimir_atras(self):
    actual = self.ultimo
    while actual:
        print(actual.dato, end=" ")
        actual = actual.anterior

lista = ListaDoble()
lista.insertar(1)
lista.insertar(2)
lista.insertar(3)
lista.insertar(4)
lista.insertar(5)
lista.insertar(6)

print("Lista original:")
lista.imprimir_adelante()

lista.invertir()

print("\nLista invertida:")
lista.imprimir_adelante()

print("\nLista invertida impresa atrás:")  
lista.imprimir_atras()