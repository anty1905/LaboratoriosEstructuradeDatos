##PRIMER EJERCICIO##
a = int(input("Ingrese Un numero\n"))
b = int(input("Ingrese otro numero\n"))

suma = a + b
resta = a - b
multip = a * b
div = a / b
print("la Suma es:", suma)
print("la Resta es:", resta)
print("El Producto es:", multip)
print("El Cociente es :", round(div, 3))

##SEGUNDO EJERCICIO##
num = int(input("Ingrese un numero"))
if num % 2 == 0:
    print("El numero", num, "es par")
else:
    print("El numero", num, "es impar")

##TERCER EJERCICIO##
a = int(input("Ingresa la altura del triangulo"))
b = int(input("ingresa la Base del triangulo"))
area = (b * a) / 2
print("El area del triangulo es :", area, "m2")


##CUARTO EJERCICIO##
def factorial(num):
    if num == 0 or num == 1:
        rpta = 1
    elif num > 1:
        rpta = num * factorial(num - 1)
    return rpta


numero = int(input("Ingresa Un numero"))
print("El factorial de", numero, "es", factorial(numero))
##Quinto EJERCICIO##
n = int(input('Indroduzca un número\n'))

list_residuo = []
zeros = []
if n == 2:
    print(f'{n} Es número primo\t')
elif n % 2 == 0:
    print(f'{n} NO es un número primo\t')
else:
    for i in range(3, n + 1, 2):
        residuo = n % i
        list_residuo.append(residuo)
    for j in list_residuo:
        if j == 0:
            zeros.append(j)
    if len(zeros) > 1:
        print(f' {n} NO es número primo')
    else:
        print(f'¡{n} ES UN NÚMERO PRIMO!')


##Sexto Ejercicio##
def invertir(string):
    inverso = ""
    for c in string:
        inverso = c + inverso
    return inverso


string = "Guru99"
print(invertir(string))

##Septimo Ejercicio##
suma = 0
m = int(input('Numero inicial:'))
n = int(input('Numero final:'))

for i in range(m, n + 1):
    if i % 2 == 0:
        suma += i

print('\nLa suma es ', suma)

# 8) Lista de Cuadrados:
lista_cuadrados = [i**2 for i in range(1, 11)]  # Genera una lista de los cuadrados de los números del 1 al 10
print(lista_cuadrados)  # Imprime la lista de cuadrados

# 9) Contador de Vocales:
def contar_vocales(cadena):
    vocales = 'aeiouAEIOU'
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador

cadena = input("Ingresa una cadena de texto: ")  # Solicita al usuario ingresar una cadena de texto
print("Número de vocales:", contar_vocales(cadena))  # Imprime el número de vocales en la cadena ingresada por el usuario

# 10) Números de la Serie Fibonacci:
def fibonacci(n):
    fibonacci_nums = [0, 1]  # Inicializa los primeros dos números de la serie Fibonacci
    for i in range(2, n):  # Genera los siguientes números de la serie hasta llegar al número deseado
        fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])
    return fibonacci_nums

print(fibonacci(10))  # Imprime los primeros 10 números de la serie Fibonacci

# 11) Ordenamiento de Lista:
numeros = [int(x) for x in input("Ingresa una lista de números separados por espacios: ").split()]  # Solicita al usuario ingresar una lista de números
numeros.sort()  # Ordena la lista de números de menor a mayor
print("Lista ordenada:", numeros)  # Imprime la lista ordenada

# 12) Palíndromo:
def es_palindromo(palabra):
    return palabra == palabra[::-1]  # Comprueba si la palabra es igual a su reverso

palabra = input("Ingresa una palabra: ")  # Solicita al usuario ingresar una palabra
if es_palindromo(palabra):  # Verifica si la palabra ingresada es un palíndromo
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")

# 13) Generador de Tablas de Multiplicar:
numero = int(input("Ingresa un número para generar su tabla de multiplicar: "))  # Solicita al usuario ingresar un número
for i in range(1, 11):  # Itera desde 1 hasta 10
    print(numero, "x", i, "=", numero * i)  # Imprime la tabla de multiplicar del número ingresado

# 14) Cálculo del Área de un Círculo:
import math

radio = float(input("Ingresa el radio del círculo: "))  # Solicita al usuario ingresar el radio del círculo
area = math.pi * radio**2  # Calcula el área del círculo
print("El área del círculo es:", area)  # Imprime el área del círculo

# 15) Suma de Dígitos:
def suma_digitos(numero):
    suma = 0
    while numero > 0:  # mientras el número sea mayor que cero
        suma += numero % 10  # Suma el último dígito del número
        numero //= 10  # Elimina el último dígito del número
    return suma

numero = int(input("Ingresa un número entero: "))  # Solicita al usuario ingresar un número entero
print("La suma de sus dígitos es:", suma_digitos(numero))  # Imprime la suma de los dígitos del número ingresado

