# Validar la igualdad de dos objetos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Asigna el nombre de la persona al atributo "nombre"
        self.edad = edad  # Asigna la edad de la persona al atributo "edad"

    def __eq__(self, otro):
        # Sobrecarga del operador de igualdad (==)
        # Se llama cuando se utiliza el operador == con objetos de tipo Persona
        if isinstance(otro, Persona):  # Verifica si "otro" es una instancia de Persona
            # Compara los atributos nombre y edad de ambas personas
            return self.nombre == otro.nombre and self.edad == otro.edad
        return False  # Si "otro" no es una instancia de Persona, retorna False

# Ejemplo de uso
person1 = Persona("Diego", 10)  # Crea una instancia de Persona con nombre "Diego" y edad 10
person2 = Persona("Diego", 10)  # Crea otra instancia de Persona con los mismos atributos que person1
person3 = Persona("Sheyla", 15)  # Crea otra instancia de Persona con nombre "Sheyla" y edad 15

# Comprueba si person1 es igual a person2 utilizando el operador de igualdad sobrecargado
print(person1 == person2)  
print(person1 == person3) 