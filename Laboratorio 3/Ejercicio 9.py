# EJERCICIO 9
# Escriba una función que reciba un conjunto de palabras y
# devuelva un conjunto con las palabras que tienen una longitud determinada.

def palabras_longitud(conjunto, longitud):
    return {palabra for palabra in conjunto if len(palabra) == longitud}