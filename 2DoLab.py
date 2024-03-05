import numpy as np  # Importa la librería numpy para trabajar con matrices
# 1) Ejercicio1
def imprimir_pares(n):
    if n <= 0:
        return  # Caso base: si n es menor o igual a 0, termina la recursión
    if n % 2 == 0:
        imprimir_pares(n - 2)  # Llama recursivamente a la función con el número par anterior
        print(n)  # Imprime el número par actual

imprimir_pares(100)  # Llama a la función para imprimir los números pares del 1 al 100

# 2) Ejercicio2
def suma_recursiva(n):
    if n == 1:
        return 1  # Caso base: si n es 1, devuelve 1
    return n + suma_recursiva(n - 1)  # Retorna la suma del número actual más la llamada recursiva con el número anterior

print("La suma de los números del 1 al n es:", suma_recursiva(10))  # Llama a la función para calcular la suma de los números del 1 al 10

# 3) Ejercicio3
def imprimir_piramide_ascendente(n):
    if n <= 0:
        return  # Caso base: si n es menor o igual a 0, termina la recursión
    imprimir_piramide_ascendente(n - 1)  # Llama recursivamente a la función con un número menos
    print(" ".join(str(i) for i in range(1, n + 1)))  # Imprime la línea de números del 1 hasta n

imprimir_piramide_ascendente(5)  # Llama a la función para imprimir la pirámide ascendente con n=5

# 4) Ejercicio4
def imprimir_piramide_invertida(n):
    if n <= 0:
        return  # Caso base: si n es menor o igual a 0, termina la ejecucion
    print(" ".join(str(i) for i in range(1, n + 1)))  # Imprime la línea de números del 1 hasta n
    imprimir_piramide_invertida(n - 1)  # Llama recursivamente a la función con un número menos

imprimir_piramide_invertida(5)  # Llama a la función para imprimir la pirámide invertida con n=5

# 5) Ejercicio5
def tabla_multiplicar_recursiva(n, i=1):
    if i > 10:
        return  # Caso base: si i es mayor que 10, termina la recursión
    print(n, "x", i, "=", n * i)  # Imprime la multiplicación
    tabla_multiplicar_recursiva(n, i + 1)  # Llama a la función con el siguiente valor de i

tabla_multiplicar_recursiva(5)  # Llama a la función para imprimir la tabla de multiplicar del 5


# 6)
matriz_reales = np.array([[1.5, 2.3, 3.7],
                          [4.2, 5.1, 6.6],
                          [7.4, 8.9, 9.2]])

print("Matriz de números reales:")
print(matriz_reales)

# 7)
matriz_complejos = np.array([[1 + 2j, 3 + 4j, 5 + 6j],
                             [7 + 8j, 9 + 10j, 11 + 12j],
                             [13 + 14j, 15 + 16j, 17 + 18j]])

print("\nMatriz de números complejos:")
print(matriz_complejos)

# 8)
matriz_matrices = np.array([[[1, 2], [3, 4]],
                             [[5, 6], [7, 8]],
                             [[9, 10], [11, 12]]])

print("\nMatriz de matrices:")
print(matriz_matrices)

# 9)
fila_central = matriz_reales.shape[0] // 2  # Calcula la fila central de la matriz
columna_central = matriz_reales.shape[1] // 2  # Calcula la columna central de la matriz
elemento_central = matriz_reales[fila_central, columna_central]  # Accede al elemento central

print("\nElemento central de la matriz de números reales:", elemento_central)

# 10)
matriz_a = np.array([[1, 2, 3],
                     [4, 5, 6]])
matriz_b = np.array([[7, 8, 9],
                     [10, 11, 12],
                     [13, 14, 15]])

suma_matrices = matriz_a + matriz_b  # Realiza la suma de matrices

print("\nSuma de dos matrices:")
print(suma_matrices)

# 11)
matriz_c = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
escalar = 2
producto_escalar = escalar * matriz_c  # Realiza la multiplicación de la matriz por el escalar

print("\nMatriz multiplicada por un número:")
print(producto_escalar)

# 12)
media_matriz = np.mean(matriz_reales)  # Calcula la media de los elementos de la matriz

print("\nMedia de los elementos de la matriz de números reales:", media_matriz)
##PARTE2############################################################################################

# Ejercicio 1: Crea una matriz de números aleatorios de tamaño 100x100.
matriz_aleatoria = np.random.rand(100, 100)

# Ejercicio 2: Calcula la media, la mediana y la desviación estándar de los elementos de una matriz.
def estadisticas_matriz(matriz):
    media = np.mean(matriz)  # Calcula la media de los elementos de la matriz
    mediana = np.median(matriz)  # Calcula la mediana de los elementos de la matriz
    desviacion_estandar = np.std(matriz)  # Calcula la desviación estándar de los elementos de la matriz
    return media, mediana, desviacion_estandar

# Ejercicio 3: Escribe una función que encuentre el elemento máximo de una matriz.
def encontrar_maximo(matriz):
    return np.max(matriz)  # Encuentra el máximo elemento de la matriz

# Ejercicio 4: Escribe una función que encuentre la submatriz de mayor suma de una matriz.
def submatriz_mayor_suma(matriz):
    submatriz_max_suma = None
    suma_maxima = float('-inf')
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            for k in range(i, len(matriz)):
                for l in range(j, len(matriz[0])):
                    suma_actual = np.sum(matriz[i:k+1, j:l+1])
                    if suma_actual > suma_maxima:
                        suma_maxima = suma_actual
                        submatriz_max_suma = matriz[i:k+1, j:l+1]
    return submatriz_max_suma

# Ejercicio 5: Escribe una función que encuentre la matriz de covarianza de dos matrices.
def matriz_covarianza(matriz1, matriz2):
    return np.cov(matriz1, matriz2)  # Calcula la matriz de covarianza entre las dos matrices

# Generamos una matriz de ejemplo para los ejercicios
matriz_ejemplo = np.random.rand(5, 5)

# Ejemplo de uso de las funciones
print("Matriz aleatoria:")
print(matriz_aleatoria)
print("\nEstadísticas de la matriz aleatoria:")
print(estadisticas_matriz(matriz_aleatoria))
print("\nElemento máximo de la matriz de ejemplo:")
print(encontrar_maximo(matriz_ejemplo))
print("\nSubmatriz de mayor suma de la matriz de ejemplo:")
print(submatriz_mayor_suma(matriz_ejemplo))
print("\nMatriz de covarianza entre la matriz de ejemplo y su traspuesta:")
print(matriz_covarianza(matriz_ejemplo, matriz_ejemplo.T))
