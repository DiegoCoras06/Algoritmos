#ERERCICIO 2
# Escriba una función que reciba un conjunto de 
# palabras y devuelva un conjunto con las palabras que comienzan con una letra determinada.
conjunto_original = {"diego", "luis", "doraemon", "maría", "andres"}
letra_inicial = "d"

def palabras_que_comienzan_con_letra(conjunto_palabras, letra):
    
    palabras_seleccionadas = set()
    for palabra in conjunto_palabras:       
        if palabra.lower().startswith(letra.lower()):           
            palabras_seleccionadas.add(palabra)

    return palabras_seleccionadas
resultado = palabras_que_comienzan_con_letra(conjunto_original, letra_inicial)
print("Palabras que comienzan con la letra '{}': {}".format(letra_inicial, resultado))
