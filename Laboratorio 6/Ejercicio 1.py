# Implementa una función que determine si una palabra es palíndroma o no.
# Utiliza una cola para comparar los caracteres de la palabra en orden original y reverso.

from collections import deque

def es_palindroma(palabra):
    # Convertir la palabra en una cola
    cola = deque(palabra)
    
    # Deque invertido para comparar con la palabra original
    cola_invertida = deque(reversed(palabra))
    
    # Comparar los caracteres de la palabra original y la invertida
    while cola and cola_invertida:
        if cola.popleft() != cola_invertida.popleft():
            return False
    
    # Si la cola está vacía, significa que la palabra es palíndroma
    return not cola and not cola_invertida

# Ejemplos de uso
print(es_palindroma("reconocer"))  # True
print(es_palindroma("python"))     # False