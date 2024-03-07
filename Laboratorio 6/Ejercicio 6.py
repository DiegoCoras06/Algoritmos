# Implementar una función que cuente la cantidad de nodos hoja (que no tienen hijos).

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def contar_nodos_hoja(raiz):
    """Función que cuenta la cantidad de nodos hoja en un árbol."""
    # Caso base: si la raíz es None, retornamos 0
    if raiz is None:
        return 0
    
    # Si el nodo actual no tiene hijos, es una hoja, por lo tanto, retornamos 1
    if not raiz.hijos:
        return 1
    
    # Inicializamos el contador de nodos hoja en 0
    contador_hoja = 0
    
    # Recorremos recursivamente los hijos del nodo actual
    for hijo in raiz.hijos:
        # Sumamos la cantidad de nodos hoja en el subárbol del hijo actual
        contador_hoja += contar_nodos_hoja(hijo)
    
    return contador_hoja

# Ejemplo de uso
# Crear un árbol de ejemplo
raiz = Nodo(1)
raiz.hijos.append(Nodo(2))
raiz.hijos.append(Nodo(3))
raiz.hijos[0].hijos.append(Nodo(4))
raiz.hijos[0].hijos.append(Nodo(5))
raiz.hijos[1].hijos.append(Nodo(6))

# Contar la cantidad de nodos hoja en el árbol
cantidad_nodos_hoja = contar_nodos_hoja(raiz)
print("Cantidad de nodos hoja en el árbol:", cantidad_nodos_hoja)