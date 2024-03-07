# Crear un programa que evalúe una expresión matemática en notación posfija utilizando una pila

class Pila:

    def __init__(self):
        self.items = []

    def está_vacía(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

    def inspeccionar(self):
        return self.items[len(self.items)-1]


def eval_posfija(expresión):
    # Se crea una pila para almacenar valores.
    pila = Pila()
    # Se itera sobre los elementos de la expresión.
    for elemento in expresión:
        # Si el elemento es un dígito, se convierte a entero y se apila.
        if elemento.isdigit():
            pila.apilar(int(elemento))
        else:
            # Se desapilan dos números de la pila.
            número2 = pila.desapilar()
            número1 = pila.desapilar()
            # Se evalua el operador y se calcula el resultado.
            if elemento == "+":
                resultado = número1 + número2
            elif elemento == "-":
                resultado = número1 - número2
            elif elemento == "*":
                resultado = número1 * número2
            else:
                resultado = número1 / número2
                
            pila.apilar(resultado)
    
    return pila.desapilar()

            
print(eval_posfija(['4','13','5','/','+'])) # 6