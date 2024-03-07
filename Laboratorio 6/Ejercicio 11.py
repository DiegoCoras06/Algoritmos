# Implementar una función que encuentre el nodo con el valor máximo en el árbol.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def encontrar_maximo(raiz):
    """Función que encuentra el nodo con el valor máximo en un árbol."""
    # Caso base: si la raíz es None, no hay máximo, retornamos None
    if raiz is None:
        return None
    
    # Inicializamos el valor máximo con el valor de la raíz
    maximo = raiz.valor
    
    # Recorremos recursivamente los hijos de la raíz para encontrar el máximo
    for hijo in raiz.hijos:
        # Llamamos recursivamente a la función para encontrar el máximo en el subárbol
        maximo_subarbol = encontrar_maximo(hijo)
        # Actualizamos el máximo si encontramos un valor mayor en el subárbol
        if maximo_subarbol is not None and maximo_subarbol > maximo:
            maximo = maximo_subarbol
    
    return maximo

# Ejemplo de uso
# Crear un árbol de ejemplo
raiz = Nodo(10)
raiz.hijos.append(Nodo(5))
raiz.hijos.append(Nodo(15))
raiz.hijos[0].hijos.append(Nodo(3))
raiz.hijos[0].hijos.append(Nodo(7))
raiz.hijos[1].hijos.append(Nodo(12))

# Encontrar el valor máximo en el árbol
valor_maximo = encontrar_maximo(raiz)
print("Valor máximo en el árbol:", valor_maximo)