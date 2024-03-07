# Validar la edad de un usuario.
edad = input("Ingrese la edad: ")
def validar_edad(nombre, edad):
    assert isinstance(edad, int), f"La edad de {nombre} debe ser un número entero"
    # assert 0 <= edad <= 100, f"La edad de {nombre} debe estar entre 0 y 100 años"

print(validar_edad("Diego", edad))