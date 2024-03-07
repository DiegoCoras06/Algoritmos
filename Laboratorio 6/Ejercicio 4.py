# Implementa un sistema de gestión de tareas que permita agregar tareas,
# marcar tareas como completadas y mostrar la próxima tarea pendiente.

from collections import deque

class SistemaGestionTareas:
    def __init__(self):
        # Inicialización de la lista de tareas como un deque vacío
        self.tareas = deque()

    def agregar_tarea(self, tarea):
        """Agrega una tarea a la lista."""
        # Agrega la tarea al final de la lista
        self.tareas.append(tarea)
        print(f"Tarea agregada: {tarea}")

    def marcar_completada(self):
        """Marca la próxima tarea como completada."""
        # Verifica si hay tareas pendientes
        if self.tareas:
            # Obtiene y elimina la primera tarea de la lista
            tarea_completada = self.tareas.popleft()
            print(f"Tarea completada: {tarea_completada}")
        else:
            print("No hay tareas pendientes.")

    def proxima_tarea_pendiente(self):
        """Muestra la próxima tarea pendiente."""
        # Verifica si hay tareas pendientes
        if self.tareas:
            # Muestra la primera tarea de la lista (próxima tarea pendiente)
            print(f"Próxima tarea pendiente: {self.tareas[0]}")
        else:
            print("No hay tareas pendientes.")

# Ejemplo de uso
sistema_tareas = SistemaGestionTareas()
sistema_tareas.agregar_tarea("Limpiar el garaje")
sistema_tareas.agregar_tarea("Hacer la compra")
sistema_tareas.agregar_tarea("Estudiar para el examen")
sistema_tareas.proxima_tarea_pendiente()
sistema_tareas.marcar_completada()
sistema_tareas.proxima_tarea_pendiente()
sistema_tareas.marcar_completada()
sistema_tareas.proxima_tarea_pendiente()
sistema_tareas.marcar_completada()
sistema_tareas.proxima_tarea_pendiente()