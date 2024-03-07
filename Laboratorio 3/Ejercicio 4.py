#EJECICIO 4
# Escriba una función que reciba dos conjuntos 
# de números y devuelva un conjunto con los números que están en ambos conjuntos.

conjunto_a = {6, 2, 9, 4, 5}
conjunto_b = {3, 9, 5, 6, 7}

def numeros_en_comun(conjunto1, conjunto2):
    
    union = conjunto1.union(conjunto2)
    return union

resultado = numeros_en_comun(conjunto_a, conjunto_b)
print("Números en común:", resultado)
