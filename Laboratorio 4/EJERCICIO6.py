# Asegurar que un ciclo while se ejecuta al menos una vez

contador = 0  # Inicializa la variable contador en 0

while contador < 10:  # Itera mientras el contador sea menor que 10
    contador += 1  # Incrementa el contador en 1 en cada iteración

    # Verifica si el contador es igual a 10. Si no lo es, lanza una AssertionError con el mensaje "el contador no se repite"
    assert contador == 10, "el contador no se repite"
