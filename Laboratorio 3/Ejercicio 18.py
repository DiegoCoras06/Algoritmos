# EJERCICIO 18
# Escriba una función que reciba un conjunto de palabras y devuelva
# un conjunto con las palabras que contienen una letra determinada
# y están ordenadas de mayor a menor.

def palabras_con_letra_ordenadas(conjunto_palabras, letra):

    palabras_con_la_letra = {palabra for palabra in conjunto_palabras if letra.lower() in palabra.lower()}

    palabras_ordenadas = sorted(palabras_con_la_letra, key=lambda x: (len(x), x.lower()), reverse=True)

    conjunto_ordenado = set(palabras_ordenadas)

    return conjunto_ordenado

conjunto_original = {"ardilla", "amor", "luis", "diego", "mirar", "Código"}
letra_especificada = "a"
resultado = palabras_con_letra_ordenadas(conjunto_original, letra_especificada)

print("Palabras que contienen la letra '{}' y están ordenadas de mayor a menor:".format(letra_especificada), resultado)