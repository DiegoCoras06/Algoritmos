# Validar el rango de una calificación.
def validar_calificacion(calificacion):
    assert 0 <= calificacion <= 20, "La calificación debe estar en el rango de 0 a 20"
print(validar_calificacion(134))