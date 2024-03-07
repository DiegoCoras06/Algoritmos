# Asegurar que una función retorna un valor específico.
def suma(a, b):
    return a + b
# Llamamos la función
resultado = suma(10, 30)
assert resultado == 40, "La función suma no está retornando el valor esperado"

print("La función suma devuelve el valor esperado:", resultado)