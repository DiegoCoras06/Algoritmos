# EJERCICIO 16
# Escriba una función que reciba un conjunto de palabras y devuelva un conjunto
# con las palabras que son palíndromos y están ordenadas de menor a mayor.

def palindromos_ordenados(conjunto_palabras):
    palindromos = {palabra for palabra in conjunto_palabras if palabra.lower() == palabra.lower()[::-1]}

    palindromos_ordenados = sorted(palindromos)

    conjunto_ordenado = set(palindromos_ordenados)

    return conjunto_ordenado

conjunto_original = {"ana", "sistemas", "luis", "reconocer", "oso", "level"}
resultado = palindromos_ordenados(conjunto_original)

print("Palíndromos ordenados de menor a mayor:", resultado)