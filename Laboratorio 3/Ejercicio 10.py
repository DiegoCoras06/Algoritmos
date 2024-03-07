# EJERCICIO 10
# Escriba una función que reciba un conjunto de palabras
# y devuelva un conjunto con las palabras que contienen una letra determinada.

conjunto_original = {"civil", "sistemas", "contabilidad", "educación", "social"}
letra_especificada = "s"
def palabras_con_letra(conjunto_palabras, letra):

    palabras_con_la_letra = set()

    for palabra in conjunto_palabras:
        if letra.lower() in palabra.lower():
            palabras_con_la_letra.add(palabra)

    return palabras_con_la_letra

resultado = palabras_con_letra(conjunto_original, letra_especificada)
print("Palabras que contienen la letra '{}': {}".format(letra_especificada, resultado))