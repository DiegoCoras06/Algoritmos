# EJERCICIO 8
# Escriba una función que reciba
# un conjunto de palabras y devuelva un conjunto con las palabras que son palíndromos.

conjunto_original = {"ana", "python", "cívico", "programación", "oso"}
def palabras_palindromas(conjunto_palabras):
    palindromos = set()

    for palabra in conjunto_palabras:
        if palabra.lower() == palabra.lower()[::-1]:

            palindromos.add(palabra)

    return palindromos

resultado = palabras_palindromas(conjunto_original)
print("Palabras palíndromas:", resultado)