# Ordenar los elementos de una pila de manera ascendente utilizando estructuras adicionales.

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, x):
        self.items.append(x)   
    
    def desapilar(self):
        return self.items.pop()
  
    def inspeccionar(self):
        return self.items[-1]

    def está_vacía(self):
        return self.items == []

    def tamaño(self):
        return len(self.items)

def ordenar_pila(pila):
    # Crea una pila auxiliar vacía.
    pila_aux = Pila()
    # Mientras la pila original no esté vacía:
    while not pila.está_vacía():
        var = pila.desapilar()
    # Mientras haya elementos en la pila auxiliar y el tope sea mayor a var:
    while not pila_aux.está_vacía() and pila_aux.inspeccionar() > var:
        pila.apilar(pila_aux.desapilar())

    pila_aux.apilar(var)

    return pila_aux

pila = Pila()
pila.apilar(3)
pila.apilar(5) 
pila.apilar(1)
pila.apilar(4)
pila.apilar(2)

print("Pila original:")
print(pila.items)

pila_ordenada = ordenar_pila(pila)

print("Pila ordenada:")
print(pila_ordenada.items)