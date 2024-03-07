# Utilizar una pila para comprobar si una palabra o frase es un palíndromo.
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()


def es_palindromo(palabra):
    # Creamos una instancia de la clase Pila
    pila = Pila()
    # Convertimos la palabra a minúsculas y eliminamos espacios en blanco
    palabra = palabra.lower().replace(" ", "").strip()
    # Apilamos cada letra de la palabra en la pila
    for letra in palabra:
        pila.apilar(letra)

    palabra_invertida = ""
    # Desapilamos las letras de la pila para formar la palabra invertida
    while not pila.esta_vacia():
        palabra_invertida += pila.desapilar()

    # Comparamos la palabra original con la palabra invertida para determinar si es un palíndromo
    return palabra == palabra_invertida

# Ejemplo de uso
palabra = "Anita lava la tina"
if es_palindromo(palabra):
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")
  


