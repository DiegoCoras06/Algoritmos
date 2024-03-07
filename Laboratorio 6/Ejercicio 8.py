# Implementar una función que calcule la altura del árbol 
# (la longitud del camino más largo desde la raíz hasta una hoja).

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def altura_arbol(raiz):
    """Función que calcula la altura del árbol."""
    # Caso base: si la raíz es None, la altura es 0
    if raiz is None:
        return 0
    
    # Si la raíz no tiene hijos, la altura es 1 (la raíz es una hoja)
    if not raiz.hijos:
        return 1
    
    # Inicializamos una lista para almacenar las alturas de los hijos
    alturas_hijos = []
    
    # Calculamos la altura de cada hijo recursivamente
    for hijo in raiz.hijos:
        alturas_hijos.append(altura_arbol(hijo))
    
    # La altura del árbol es 1 más la altura máxima entre los hijos
    return 1 + max(alturas_hijos)

# Ejemplo de uso
# Crear un árbol de ejemplo
raiz = Nodo(1)
raiz.hijos.append(Nodo(2))
raiz.hijos.append(Nodo(3))
raiz.hijos[0].hijos.append(Nodo(4))
raiz.hijos[0].hijos.append(Nodo(5))
raiz.hijos[1].hijos.append(Nodo(6))

# Calcular la altura del árbol
altura = altura_arbol(raiz)
print("Altura del árbol:", altura)