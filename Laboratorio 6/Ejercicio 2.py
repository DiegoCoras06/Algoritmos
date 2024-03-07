# Crea un sistema de gestión de pedidos que utilice una cola para procesar
# los pedidos en el orden en que fueron recibidos.
# Implementa funciones para agregar pedidos, procesar pedidos y mostrar el estado actual de la cola.

from collections import deque

class SistemaGestionPedidos:
    def __init__(self):
        # Inicialización de la cola de pedidos como un deque vacío
        self.cola_pedidos = deque()

    def agregar_pedido(self, pedido):
        """Agrega un pedido a la cola."""
        # Agrega el pedido al final de la cola
        self.cola_pedidos.append(pedido)
        print(f"Pedido agregado: {pedido}")

    def procesar_pedido(self):
        """Procesa el próximo pedido en la cola."""
        # Verifica si la cola de pedidos no está vacía
        if self.cola_pedidos:
            # Obtiene y elimina el primer pedido de la cola
            pedido = self.cola_pedidos.popleft()
            print(f"Procesando pedido: {pedido}")
        else:
            print("No hay pedidos pendientes.")

    def mostrar_estado_cola(self):
        """Muestra el estado actual de la cola de pedidos."""
        # Verifica si la cola de pedidos no está vacía
        if self.cola_pedidos:
            print("Estado actual de la cola de pedidos:")
            # Itera sobre la cola de pedidos para mostrar cada pedido
            for i, pedido in enumerate(self.cola_pedidos, start=1):
                print(f"{i}. {pedido}")
        else:
            print("No hay pedidos en la cola.")

# Ejemplo de uso
sistema_pedidos = SistemaGestionPedidos()
sistema_pedidos.agregar_pedido("Pizza")
sistema_pedidos.agregar_pedido("Hamburguesa")
sistema_pedidos.agregar_pedido("Ensalada")
sistema_pedidos.mostrar_estado_cola()
sistema_pedidos.procesar_pedido()
sistema_pedidos.mostrar_estado_cola()
sistema_pedidos.procesar_pedido()
sistema_pedidos.mostrar_estado_cola()