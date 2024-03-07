# EJERCICIO 20
# Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
# son palíndromos, tienen una longitud determinada y
# están ordenadas de menor a mayor.

def palindromos_longitud_ordenadas(conjunto_palabras, longitud):

    palindromos_filtrados = {palabra for palabra in conjunto_palabras if len(palabra) == longitud and palabra.lower() == palabra.lower()[::-1]}

    palabras_ordenadas = sorted(palindromos_filtrados)

    conjunto_ordenado = set(palabras_ordenadas)

    return conjunto_ordenado

# Ejemplo de uso
conjunto_original = {"radar", "python", "solos", "level", "noon", "reconocer"}
longitud_especificada = 5
resultado = palindromos_longitud_ordenadas(conjunto_original, longitud_especificada)

print(f"Palíndromos de longitud {longitud_especificada} ordenados de menor a mayor:", resultado)