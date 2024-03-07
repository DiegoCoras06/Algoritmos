# Implementar una función que calcule la profundidad de un nodo (la longitud del camino desde la raíz hasta el nodo).

class Nodo:
    def __init__(self, valor):
        self.valor = valor  # Valor del nodo
        self.hijos = []     # Lista de hijos del nodo

def profundidad_nodo(raiz, valor_buscado, profundidad=0):
    """Función que calcula la profundidad de un nodo en un árbol."""
    # Caso base: si la raíz es None, retornamos None
    if raiz is None:
        return None
    
    # Si encontramos el valor buscado en la raíz, retornamos la profundidad actual
    if raiz.valor == valor_buscado:
        return profundidad
    
    # Buscamos recursivamente en los hijos de la raíz
    for hijo in raiz.hijos:
        profundidad_encontrada = profundidad_nodo(hijo, valor_buscado, profundidad + 1)
        if profundidad_encontrada is not None:
            return profundidad_encontrada
    
    # Si el valor buscado no se encuentra en el subárbol con raíz en este nodo, retornamos None
    return None

# Ejemplo de uso
# Crear un árbol de ejemplo
raiz = Nodo(1)
raiz.hijos.append(Nodo(2))
raiz.hijos.append(Nodo(3))
raiz.hijos[0].hijos.append(Nodo(4))
raiz.hijos[0].hijos.append(Nodo(5))
raiz.hijos[1].hijos.append(Nodo(6))

# Calcular la profundidad de un nodo con valor 5
valor_buscado = 5
profundidad = profundidad_nodo(raiz, valor_buscado)
if profundidad is not None:
    print(f"La profundidad del nodo con valor {valor_buscado} es: {profundidad}")
else:
    print(f"No se encontró un nodo con valor {valor_buscado} en el árbol.")