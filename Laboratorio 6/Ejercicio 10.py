# Implementar una función que encuentre el nodo con el valor mínimo en el árbol.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def encontrar_minimo(raiz):
    """Función que encuentra el nodo con el valor mínimo en un árbol."""
    # Caso base: si la raíz es None, no hay mínimo, retornamos None
    if raiz is None:
        return None
    
    # Inicializamos el valor mínimo con el valor de la raíz
    minimo = raiz.valor
    
    # Recorremos recursivamente los hijos de la raíz para encontrar el mínimo
    for hijo in raiz.hijos:
        # Llamamos recursivamente a la función para encontrar el mínimo en el subárbol
        minimo_subarbol = encontrar_minimo(hijo)
        # Actualizamos el mínimo si encontramos un valor menor en el subárbol
        if minimo_subarbol is not None and minimo_subarbol < minimo:
            minimo = minimo_subarbol
    
    return minimo

# Ejemplo de uso
# Crear un árbol de ejemplo
raiz = Nodo(10)
raiz.hijos.append(Nodo(5))
raiz.hijos.append(Nodo(15))
raiz.hijos[0].hijos.append(Nodo(3))
raiz.hijos[0].hijos.append(Nodo(7))
raiz.hijos[1].hijos.append(Nodo(12))

# Encontrar el valor mínimo en el árbol
valor_minimo = encontrar_minimo(raiz)
print("Valor mínimo en el árbol:", valor_minimo)