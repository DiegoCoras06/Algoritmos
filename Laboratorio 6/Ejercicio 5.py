
# Implementar una función que cuente la cantidad de nodos en el árbol

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def contar_nodos(raiz):
    """Función que cuenta la cantidad de nodos en un árbol."""
    if raiz is None:
        return 0
    
    # Inicialmente, contamos el nodo actual
    contador = 1

    # Recorremos recursivamente los hijos del nodo actual
    for hijo in raiz.hijos:
        contador += contar_nodos(hijo)

    return contador

# Ejemplo de uso
# Crear un árbol de ejemplo
raiz = Nodo(1)
raiz.hijos.append(Nodo(2))
raiz.hijos.append(Nodo(3))
raiz.hijos[0].hijos.append(Nodo(4))
raiz.hijos[0].hijos.append(Nodo(5))
raiz.hijos[1].hijos.append(Nodo(6))

# Contar la cantidad de nodos en el árbol
cantidad_nodos = contar_nodos(raiz)
print("Cantidad de nodos en el árbol:", cantidad_nodos)