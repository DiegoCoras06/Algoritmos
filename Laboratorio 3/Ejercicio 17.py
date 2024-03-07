
# EJERCICIO 17
# Escriba una función que reciba un conjunto de palabras y
# devuelva un conjunto con las palabras que tienen una
# longitud determinada y están ordenadas de menor a mayor.

def palabras_segun_longitud_ordenadas(conjunto_palabras, longitud):
    return {palabra for palabra in conjunto_palabras if len(palabra) == longitud and palabra == ''.join(sorted(palabra))}