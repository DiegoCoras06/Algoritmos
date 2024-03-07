# Desarrolla un programa que encuentre el camino más corto a través de un laberinto. Utiliza una cola 
# para realizar un recorrido en anchura (BFS) desde el punto de inicio hasta el punto de destino.

from collections import deque

def encontrar_camino_laberinto(laberinto, inicio, destino):
    # Definir movimientos posibles: arriba, abajo, izquierda, derecha
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    filas = len(laberinto)
    columnas = len(laberinto[0])

    # Función para verificar si una celda es válida y no ha sido visitada
    def es_celda_valida(fila, columna):
        return 0 <= fila < filas and 0 <= columna < columnas and laberinto[fila][columna] == 1

    # Inicializar cola para BFS y visitados
    cola = deque([(inicio[0], inicio[1], 0)])  # Incluir la distancia desde el inicio
    visitados = set([(inicio[0], inicio[1])])

    while cola:
        fila, columna, distancia = cola.popleft()

        # Si alcanzamos el destino, retornar la distancia mínima
        if (fila, columna) == destino:
            return distancia

        # Explorar movimientos posibles
        for movimiento in movimientos:
            nueva_fila = fila + movimiento[0]
            nueva_columna = columna + movimiento[1]

            # Verificar si la nueva celda es válida y no ha sido visitada
            if es_celda_valida(nueva_fila, nueva_columna) and (nueva_fila, nueva_columna) not in visitados:
                # Agregar la nueva celda a la cola y marcarla como visitada
                cola.append((nueva_fila, nueva_columna, distancia + 1))
                visitados.add((nueva_fila, nueva_columna))

    # Si no se puede llegar al destino, retornar -1
    return -1

# Ejemplo de uso
laberinto = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1]
]
inicio = (0, 0)
destino = (4, 4)

distancia_minima = encontrar_camino_laberinto(laberinto, inicio, destino)
if distancia_minima != -1:
    print(f"La distancia mínima desde el punto de inicio hasta el destino es: {distancia_minima}")
else:
    print("No se puede llegar al destino desde el punto de inicio.")