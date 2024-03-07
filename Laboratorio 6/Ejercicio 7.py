# Implementar una función que cuente la cantidad de nodos internos (que tienen al menos un hijo).

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def contar_nodos_internos(raiz):
    """Función que cuenta la cantidad de nodos internos en un árbol."""
    if raiz is None:
        return 0
    
    # Inicialmente, consideramos el nodo actual como interno si tiene hijos
    contador = 0
    if raiz.hijos:
        contador = 1

    # Recorremos recursivamente los hijos del nodo actual
    for hijo in raiz.hijos:
        contador += contar_nodos_internos(hijo)

    return contador

# Ejemplo de uso
# Crear un árbol de ejemplo
raiz = Nodo(1)
raiz.hijos.append(Nodo(2))
raiz.hijos.append(Nodo(3))
raiz.hijos[0].hijos.append(Nodo(4))
raiz.hijos[0].hijos.append(Nodo(5))
raiz.hijos[1].hijos.append(Nodo(6))

# Contar la cantidad de nodos internos en el árbol
cantidad_nodos_internos = contar_nodos_internos(raiz)
print("Cantidad de nodos internos en el árbol:", cantidad_nodos_internos)