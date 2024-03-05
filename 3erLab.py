#Ejercicio1
def es_primo(n):
    if n <= 1:  # Si el número es 0 o 1, no es primo
        return False
    elif n <= 3:  # 2 y 3 son primos
        return True
    elif n % 2 == 0 or n % 3 == 0:  # Si es divisible por 2 o 3, no es primo
        return False
    i = 5
    while i * i <= n:  # Comprobar divisibilidad hasta la raíz cuadrada de n
        if n % i == 0 or n % (i + 2) == 0:  # Si es divisible por i o i+2, no es primo
            return False
        i += 6
    return True
def numeros_primos(conjunto):
    return {num for num in conjunto if es_primo(num)}

#Ejercicio2
def palabras_con_letra(conjunto, letra):
    return {palabra for palabra in conjunto if palabra.startswith(letra)}

#Ejercicio3
def numeros_divisibles(conjunto, divisor):
    return {num for num in conjunto if num % divisor == 0}

#Ejercicio4
def numeros_en_ambos(conjunto1, conjunto2):
    return conjunto1.intersection(conjunto2)

#Ejercicio5
def numeros_en_primero(conjunto1, conjunto2):
    return conjunto1.difference(conjunto2)

#Ejercicio6
def numeros_en_segundo(conjunto1, conjunto2):
    return conjunto2.difference(conjunto1)

#Ejercicio7
def anagramas(palabras):
    anagrama_conjunto = set()
    for palabra in palabras:
        if len(palabra) > 1:
            anagrama_conjunto.add("".join(sorted(palabra)))
    return {palabra for palabra in palabras if "".join(sorted(palabra)) in anagrama_conjunto}

#Ejercicio8
def palindromos(palabras):
    return {palabra for palabra in palabras if palabra == palabra[::-1]}

#Ejercicio9
def palabras_con_longitud(palabras, longitud):
    return {palabra for palabra in palabras if len(palabra) == longitud}
# Ejercicio10
def palabras_con_letra_determinada(palabras, letra):
    # Utilizamos un conjunto de comprensión para filtrar las palabras que contienen la letra dada
    return {palabra for palabra in palabras if letra in palabra}

#Ejercicio11
def numeros_ordenados_menor_a_mayor(conjunto):
    # Utilizamos la función sorted para ordenar el conjunto de números
    return sorted(conjunto)

#Ejercicio12
def numeros_ordenados_mayor_a_menor(conjunto):
    # Utilizamos la función sorted con el parámetro reverse=True para ordenar de mayor a menor
    return sorted(conjunto, reverse=True)

#Ejercicio13
def numeros_duplicados(conjunto):
    duplicados = set()
    unicos = set()
    # Iteramos sobre el conjunto y comprobamos si un número está presente más de una vez
    for num in conjunto:
        if num in unicos:  # Si ya está en el conjunto de únicos, lo añadimos a duplicados
            duplicados.add(num)
        else:
            unicos.add(num)  # Si no, lo añadimos al conjunto de únicos
    return duplicados

#Ejercicio14
def numeros_no_duplicados(conjunto):
    # Utilizamos un conjunto de comprensión para filtrar los números que no están duplicados
    unicos = set()
    # Creamos un conjunto para almacenar los números duplicados
    duplicados = set()
    # Iteramos sobre los números en el conjunto
    for num in conjunto:
        # Si el número ya está en el conjunto de únicos, lo agregamos al conjunto de duplicados
        # de lo contrario, lo agregamos al conjunto de únicos
        if num in unicos:
            duplicados.add(num)
        else:
            unicos.add(num)
    # Devolvemos el conjunto de únicos restando los duplicados
    return unicos - duplicados

#Ejercicio15
def numeros_primos_ordenados_menor_a_mayor(conjunto):
    # Utilizamos un conjunto de comprensión para obtener los números primos y luego los ordenamos
    return sorted({num for num in conjunto if es_primo(num)})

#Ejercicio16
def palabras_palindromas_ordenadas_menor_a_mayor(palabras):
    # Utilizamos un conjunto de comprensión para obtener las palabras palíndromas y luego las ordenamos
    return sorted({palabra for palabra in palabras if palabra == palabra[::-1]})

#Ejercicio17
def palabras_con_longitud_ordenadas_menor_a_mayor(palabras, longitud):
    # Utilizamos un conjunto de comprensión para filtrar las palabras con la longitud dada y luego las ordenamos
    return sorted({palabra for palabra in palabras if len(palabra) == longitud})

#Ejercicio18
def palabras_con_letra_determinada_ordenadas_mayor_a_menor(palabras, letra):
    # Utilizamos un conjunto de comprensión para obtener las palabras con la letra dada y luego las ordenamos
    return sorted({palabra for palabra in palabras if letra in palabra}, reverse=True)

#Ejercicio19
def numeros_ordenados_menor_a_mayor_sin_duplicados(conjunto):
    # Convertimos el conjunto a una lista para eliminar los duplicados y luego lo ordenamos
    return sorted(set(conjunto))

#Ejercicio20
def palabras_palindromas_longitud_ordenadas_menor_a_mayor(palabras, longitud):
    # Utilizamos un conjunto de comprensión para obtener las palabras palíndromas con longitud dada y luego las ordenamos
    return sorted({palabra for palabra in palabras if palabra == palabra[::-1] and len(palabra) == longitud})


#SALIDAS
if __name__ == "__main__":
    numeros = {2, 3, 4, 5, 6, 7, 8, 9, 10}
    print("Números primos:", numeros_primos(numeros))

    palabras = {"gato", "perro", "ganso", "loro", "elefante", "tigre"}
    letra = "g"
    print("Palabras que comienzan con la letra", letra + ":", palabras_con_letra(palabras, letra))

    print("Números divisibles por 3:", numeros_divisibles(numeros, 3))

    numeros2 = {3, 4, 5, 11, 12}
    print("Números en ambos conjuntos:", numeros_en_ambos(numeros, numeros2))

    print("Números en el primero pero no en el segundo:", numeros_en_primero(numeros, numeros2))

    print("Números en el segundo pero no en el primero:", numeros_en_segundo(numeros, numeros2))

    palabras_anagrama = {"roma", "mora", "amor", "papel", "lappe"}
    print("Anagramas:", anagramas(palabras_anagrama))

    palabras_palindromo = {"oso", "reconocer", "cívico", "motor", "radar"}
    print("Palíndromos:", palindromos(palabras_palindromo))

    print("Palabras con longitud 5:", palabras_con_longitud(palabras, 5))

    print("Palabras con letra 'o':", palabras_con_letra_determinada(palabras, letra))


    print("Números ordenados de menor a mayor:", numeros_ordenados_menor_a_mayor(numeros))


    print("Números ordenados de mayor a menor:", numeros_ordenados_mayor_a_menor(numeros))


    print("Números duplicados:", numeros_duplicados(numeros))


    print("Números que no están duplicados:", numeros_no_duplicados(numeros))


    print("Números primos ordenados de menor a mayor:", numeros_primos_ordenados_menor_a_mayor(numeros))


    print("Palabras palíndromas ordenadas de menor a mayor:",
          palabras_palindromas_ordenadas_menor_a_mayor(palabras_palindromo))


    print("Palabras de longitud 5 ordenadas de menor a mayor:",
          palabras_con_longitud_ordenadas_menor_a_mayor(palabras, 5))


    print("Palabras con letra 'o' ordenadas de mayor a menor:",
          palabras_con_letra_determinada_ordenadas_mayor_a_menor(palabras, "o"))


    print("Números ordenados de menor a mayor y no duplicados:",
          numeros_ordenados_menor_a_mayor_sin_duplicados(numeros))

    print("Palabras palíndromas con longitud 5 ordenadas de menor a mayor:",
          palabras_palindromas_longitud_ordenadas_menor_a_mayor(palabras_palindromo, 5))


