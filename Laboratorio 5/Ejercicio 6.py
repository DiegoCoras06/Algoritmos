# Utilizar una pila para invertir el orden de los caracteres de una cadena.

class Pila:
    # El método init inicia una lista vacía para almacenar los elementos
    def __init__(self):
        self.items = []
    # Método está_vacía() retorna True si la lista de la pila está vacía
    def está_vacía(self):
        return self.items == []
    # Método apilar() agrega un elemento al final de la lista
    def apilar(self, item):
        self.items.append(item)
    # Método desapilar() elimina y retorna el último elemento de la lista
    def desapilar(self):
        return self.items.pop() 

def invertir_cadena(cadena):
    pila = Pila()
    # Recorre la cadena y apila cada caracter
    for caracter in cadena:
        pila.apilar(caracter)
    # Desapila cada caracter y lo agrega a una nueva cadena
    cadena_invertida = ""
    while not pila.está_vacía():
        cadena_invertida += pila.desapilar()
    
    return cadena_invertida

mi_cadena = "Hola Mundo"
print(mi_cadena)

mi_cadena_invertida = invertir_cadena(mi_cadena)
print(mi_cadena_invertida)