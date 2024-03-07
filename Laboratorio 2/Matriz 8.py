# 8)Crea una matriz de matrices.

matriz_interna_1 = [[1, 2], [3, 4]]
matriz_interna_2 = [[5, 6], [7, 8]]

# Creamos la matriz de matrices utilizando listas anidadas
matriz_de_matrices = [matriz_interna_1, matriz_interna_2]

# Imprimimos la matriz de matrices
print("Matriz de matrices:")
for matriz in matriz_de_matrices:
    print(matriz)