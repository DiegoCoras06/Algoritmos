# Eliminar los elementos duplicados de una pila.

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def esta_vacia(self):
        return len(self.items) == 0


def eliminar_duplicados(pila):
    pila_unica = Pila()
    elementos_unicos = set()

    while not pila.esta_vacia():
        elemento = pila.desapilar()
        if elemento not in elementos_unicos:
            pila_unica.apilar(elemento)
            elementos_unicos.add(elemento)

    return pila_unica


# Ejemplo de uso
pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(2)
pila.apilar(4)
pila.apilar(1)

print("Pila original:", pila.items)

pila_sin_duplicados = eliminar_duplicados(pila)

print("Pila sin duplicados:", pila_sin_duplicados.items)