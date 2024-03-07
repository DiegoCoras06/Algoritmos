###OPERACIONES BÁSICAS
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
# Función para sumar dos números
def suma():
   return a + b

# Función para restar dos números
def resta():
   return a - b

# Función para multiplicar dos números
def multiplicacion():
   return a * b

# Función para dividir dos números
def division():
   if b != 0:
       return a / b
   else:
       return "No se puede dividir entre cero"
print(suma())
print(resta())
print(multiplicacion())
print(division())

#############################################
#VERIFICACIÓN DE NÚMERO PAR E IMPAR

num = int(input("Ingresa un número entero para determinar si es par o impar: "))

def determinar():
   if num % 2 == 0:
       return "El número es PAR."
   else:
       return "El número es IMPAR."

print(determinar())

#############################################
#ÁREA DEL TRIÁNGULO
##
base= int(input("Ingrese la base del triángulo: "))
altura= int(input("Ingrese la altura del triángulo: "))

def area():
   return base*altura/2
print(int(area()))

#############################################
#CALCULADORA DE FACTORIAL
##
def factorial(n):
   if n==0:
       return 1
   else:
       return n*factorial(n-1)
       
print(factorial(5))    

#############################################
#NÚMERO PRIMO

def esprimo(n):  # Definición de la función esprimo 
    if n <= 1:   # Verifica si el número es menor o igual a 1.
        return False  # Devuelve False si el número es menor o igual a 1, ya que los números primos son mayores que 1.
    elif n == 2:  # Verifica si el número es igual a 2.
        return True  # Devuelve True si el número es igual a 2, ya que 2 es un número primo.
    else:  # En caso contrario, para cualquier número mayor que 2:
        for i in range(2, n):  # Itera sobre todos los números desde 2 hasta n-1.
            if n % i == 0:  # Verifica si n es divisible por algún número en el rango (2, n-1).
                return False  # Si n es divisible por algún número en el rango, devuelve False, ya que n no es primo.
        return True  # Si no se encuentra ningún divisor entre (2, n-1), devuelve True, indicando que n es primo.

print(esprimo(7)) 
#############################################
#INVERSIÓN DE CADENAS

def invertir_cadena(cadena):  # Define una función llamada invertir_cadena que toma una cadena como argumento.
    return cadena[::-1]  # Utiliza la técnica de rebanado (slicing) con el paso -1 para invertir la cadena y la devuelve.

print(invertir_cadena("luis"))

#############################################
#SUMA DE NÚMEROS PARES
def suma_pares_en_rango(a, b):  # Define una función llamada suma_pares_en_rango que toma dos números enteros a y b como argumentos.
    suma = 0  # Inicializa una variable suma para almacenar la suma de los números pares.
    for i in range(a, b + 1):  # Itera sobre todos los números en el rango desde a hasta b (incluyendo b).
        if i % 2 == 0:  # Verifica si el número i es par (es decir, si su residuo al dividirlo por 2 es 0).
            suma += i  # Si i es par, se suma a la variable suma.
    return suma  # Devuelve la suma de los números pares en el rango dado.

print(suma_pares_en_rango(2, 8))

#############################################
#LISTA DE CUADRADOS
##
cuadrados = [i ** 2 for i in range(1, 11)]  
# Se utiliza una comprensión de lista para generar los cuadrados de los números del 1 al 10.
# Para cada número i en el rango de 1 a 10 (exclusivo), se calcula su cuadrado i ** 2 y se agrega a la lista.

print(cuadrados)

#############################################
#CONTADOR DE VOCALES
def contar_vocales(cadena):  # Define una función llamada contar_vocales que toma una cadena como argumento.
    cadena = cadena.lower()  # Convierte la cadena a minúsculas para que coincida con las vocales en minúsculas.
    vocales = ['a', 'e', 'i', 'o', 'u']  # Crea una lista de vocales.
    contador = 0  # Inicializa un contador para contar las vocales.

    # Recorre cada carácter en la cadena y cuenta las vocales.
    for caracter in cadena:
        if caracter in vocales:  # Comprueba si el carácter actual es una vocal.
            contador += 1  # Incrementa el contador si el carácter es una vocal.

    return contador  # Devuelve el número total de vocales encontradas en la cadena.

print(contar_vocales("DIEGO"))

#############################################
#FIBONACCI
def fibonacci(n):  # Define una función llamada fibonacci que toma un entero n como argumento.
    # Inicializar la lista con los dos primeros términos de la serie
    fibo = [0, 1]  # Crea una lista inicializada con los dos primeros términos de la serie de Fibonacci.

    for i in range(2, n):  # Itera a través de los índices de 2 a n-1 para calcular los términos de Fibonacci restantes.
        fibo.append(fibo[i - 1] + fibo[i - 2])  # Calcula el siguiente término de Fibonacci como la suma de los dos términos anteriores y lo agrega a la lista.

    return fibo  # Devuelve la lista que contiene los primeros n términos de la serie de Fibonacci.

print(fibonacci(10)) 

#############################################
#ORDENAR LISTAS
entrada = input("Ingresa una lista de números separados por comas: ")

numeros = [int(x) for x in entrada.split(',')]
#ordenar
numeros.sort()

print("La lista ordenada de menor a mayor es:", numeros)


#############################################
#PALÍNDROMO
palabra_ingresada = input("Ingresa una palabra para verificar si es un palíndromo: ")
def es_palindromo(palabra):
   # Convertir la palabra a minúsculas y eliminar espacios en blanco
   palabra = palabra.lower().replace(" ", "")
   return palabra == palabra[::-1]
#Verificar si la palabra ingresada es un palíndromo
if es_palindromo(palabra_ingresada):
   print(f"'{palabra_ingresada}' es un palíndromo.")
else:
   print(f"'{palabra_ingresada}' no es un palíndromo.")

#############################################
#TABLA DE MULTIPLICAR
numero = int(input("Introduzca un número: "))  # Solicita al usuario que introduzca un número y lo convierte a entero.

for i in range(0, 11):  # Itera sobre los números del 0 al 10.
    resultado = i * numero  # Calcula el resultado de multiplicar el número ingresado por el número del ciclo.
    print(numero, "x", i, "=", resultado) 
    
#############################################
#ÁREA DE UN CÍRCULO
# Importa el módulo math para acceder a la constante pi y otras funciones matemáticas.
import math  
# Solicita al usuario que ingrese el radio del círculo y lo convierte a flotante.
radio_ingresado = float(input("Ingrese el radio del círculo: "))  
# Define una función llamada calcular_area_circulo que toma el radio del círculo como argumento.
def calcular_area_circulo(radio):  
    return math.pi * radio ** 2  # Calcula el área del círculo utilizando la fórmula π * radio al cuadrado y lo devuelve.

area_circulo = calcular_area_circulo(radio_ingresado) 

# Imprime el área del círculo con el radio ingresado, formateando el resultado para mostrar solo dos decimales.
print(f"El área del círculo con radio {radio_ingresado} es: {area_circulo:.2f}")


#############################################
#SUMA DE DÍGITOS
# Solicita al usuario que ingrese un número entero y lo convierte a entero.
numero = int(input("Ingresa un número entero para calcular la suma de sus dígitos: "))  

def suma_digitos():  # Define una función llamada suma_digitos que no toma argumentos.
   numero_str = str(numero)  # Convierte el número entero en una cadena para poder iterar sobre sus dígitos.
   suma = 0  # Inicializa una variable para almacenar la suma de los dígitos.
   for digito in numero_str:  # Itera sobre cada dígito en la cadena de dígitos.
       suma += int(digito)  # Convierte cada dígito nuevamente a entero y lo suma a la variable suma.
       
   return suma  # Devuelve la suma de los dígitos.

resultado = suma_digitos()  # Llama a la función suma_digitos y guarda el resultado en la variable resultado.

# Imprime la suma de los dígitos del número ingresado por el usuario.
print(f"La suma de los dígitos del número {numero} es: {resultado}")



