# Crear una calculadora que pueda realizar operaciones básicas (+, -, *, /) 
# utilizando una pila para evaluar 

class Pila:
    # Se define la clase Pila, el método init inicializa una lista
    # vacía para almacenar los elementos de la pila.
    def __init__(self):
        self.items = []
    # El método apilar() agrega un elemento x al final de la lista de la pila.
    def apilar(self, x):
        self.items.append(x)
    # El método desapilar() elimina y retorna el último elemento de la lista de la pila.
    def desapilar(self):
        return self.items.pop()
    # El método inspeccionar() retorna el último elemento de la pila sin eliminarlo.
    def inspeccionar(self):
        return self.items[-1]
    # El método esta_vacia() retorna True si la pila no tiene elementos.
    def esta_vacia(self):
        return self.items == []

def calcular(expresion):
    pila = Pila()
    # Recorre la expresión elemento por elemento. Si es un operador,
    # desapila 2 elementos, aplica la operación y apila el resultado.
    # Si no es operador, convierte a entero y apila.
    for elemento in expresion:
        if elemento in ["+", "-", "*", "/"]:
            op2 = pila.desapilar()
            op1 = pila.desapilar()
            resultado = aplicar_operacion(op1, op2, elemento)
            pila.apilar(resultado)
        else:
            pila.apilar(int(elemento))

    return pila.desapilar()
# Esta función aplica la operación correspondiente entre op1 y op2 según el operador.
def aplicar_operacion(op1, op2, operador):
    if operador == "+":
        return op1 + op2
    elif operador == "-":
        return op1 - op2
    elif operador == "*":
        return op1 * op2
    else:
        return op1 / op2

print(calcular(["2", "3", "+"])) 
print(calcular(["4", "2", "*", "3", "-", "1", "+"]))