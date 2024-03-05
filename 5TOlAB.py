class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

# Clase para la lista doblemente enlazada
class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    # Método para agregar un nuevo nodo al final de la lista
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    # Método para duplicar cada nodo de la lista
    def duplicar_nodos(self):
        actual = self.cabeza
        while actual:
            nuevo_nodo = Nodo(actual.dato)
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
            if nuevo_nodo.siguiente:
                nuevo_nodo.siguiente.anterior = nuevo_nodo
            actual = nuevo_nodo.siguiente

    # Método para imprimir la lista hacia adelante
    def imprimir_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    # Método para imprimir la lista hacia atrás
    def imprimir_atras(self):
        actual = self.cola
        while actual:
            print(actual.dato, end=" ")
            actual = actual.anterior
        print()

    # Método para contar nodos pares e impares en la lista
    def contar_pares_impares(self):
        actual = self.cabeza
        pares = 0
        impares = 0
        while actual:
            if actual.dato % 2 == 0:
                pares += 1
            else:
                impares += 1
            actual = actual.siguiente
        print(f"Nodos pares: {pares}, Nodos impares: {impares}")

    # Método para insertar un nuevo nodo en una posición específica
    def insertar_en_posicion(self, posicion, dato):
        nuevo_nodo = Nodo(dato)
        actual = self.cabeza
        for _ in range(posicion - 1):
            actual = actual.siguiente
        nuevo_nodo.siguiente = actual.siguiente
        nuevo_nodo.anterior = actual
        if actual.siguiente:
            actual.siguiente.anterior = nuevo_nodo
        actual.siguiente = nuevo_nodo

    # Método para eliminar nodos duplicados de la lista
    def eliminar_duplicados(self):
        actual = self.cabeza
        valores_unicos = set()
        while actual:
            if actual.dato in valores_unicos:
                actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
            else:
                valores_unicos.add(actual.dato)
            actual = actual.siguiente

    # Método para invertir la lista
    def invertir_lista(self):
        actual = self.cabeza
        while actual:
            actual.siguiente, actual.anterior = actual.anterior, actual.siguiente
            actual = actual.anterior
        self.cabeza, self.cola = self.cola, self.cabeza

#1 Crear una lista con al menos 4 nodos
lista_1 = ListaDoblementeEnlazada()
lista_1.agregar(1)
lista_1.agregar(2)
lista_1.agregar(3)
lista_1.agregar(4)

# Duplicar cada nodo y mostrar la lista original y duplicada hacia adelante y hacia atrás
print("Lista original:")
lista_1.imprimir_adelante()
lista_1.imprimir_atras()
lista_1.duplicar_nodos()
print("Lista duplicada:")
lista_1.imprimir_adelante()
lista_1.imprimir_atras()

#2 Contar nodos pares e impares
print("\nConteo de nodos pares e impares:")
lista_2 = ListaDoblementeEnlazada()
lista_2.agregar(1)
lista_2.agregar(2)
lista_2.agregar(3)
lista_2.agregar(4)
lista_2.agregar(5)
lista_2.agregar(6)
lista_2.agregar(7)
lista_2.agregar(8)
lista_2.agregar(9)
lista_2.imprimir_adelante()
lista_2.contar_pares_impares()

#3 Insertar un nodo en la posición 3 e imprimir la lista hacia adelante y hacia atrás
print("\nInsertar nodo en posición 3:")
lista_3 = ListaDoblementeEnlazada()
lista_3.agregar(1)
lista_3.agregar(2)
lista_3.agregar(3)
lista_3.agregar(4)
lista_3.agregar(5)
lista_3.imprimir_adelante()
lista_3.insertar_en_posicion(3, 15)
lista_3.imprimir_adelante()

#4 Eliminar nodos duplicados e imprimir la lista hacia adelante y hacia atrás
print("\nEliminar nodos duplicados:")
lista_4 = ListaDoblementeEnlazada()
lista_4.agregar(1)
lista_4.agregar(2)
lista_4.agregar(3)
lista_4.agregar(2)
lista_4.agregar(4)
lista_4.agregar(1)
lista_4.imprimir_adelante()
lista_4.eliminar_duplicados()
lista_4.imprimir_adelante()

#5 Invertir la lista e imprimir hacia adelante y hacia atrás
print("\nInvertir la lista:")
lista_5 = ListaDoblementeEnlazada()
lista_5.agregar(1)
lista_5.agregar(2)
lista_5.agregar(3)
lista_5.agregar(4)
lista_5.agregar(5)
lista_5.agregar(6)
lista_5.imprimir_adelante()
lista_5.invertir_lista()
lista_5.imprimir_adelante()
#6Invertir una cadena utilizando una pila:
def invertir_cadena(cadena):
    pila = []
    for caracter in cadena:
        pila.append(caracter)
    cadena_invertida = ''
    while pila:
        cadena_invertida += pila.pop()
    return cadena_invertida

cadena_original = "Hola mundo"
cadena_invertida = invertir_cadena(cadena_original)
print("Cadena original:", cadena_original)
print("Cadena invertida:", cadena_invertida)
#7Convertir un número decimal a binario utilizando una pila:
def decimal_a_binario(numero):
    pila = []
    while numero > 0:
        pila.append(numero % 2)
        numero //= 2
    binario = ''
    while pila:
        binario += str(pila.pop())
    return binario

numero_decimal = 25
binario = decimal_a_binario(numero_decimal)
print(f"Número decimal {numero_decimal} en binario:", binario)
#8Evaluar una expresión posfija utilizando una pila:
def evaluar_expresion_posfija(expresion):
    pila = []
    operadores = {'+', '-', '*', '/'}
    for token in expresion.split():
        if token not in operadores:
            pila.append(int(token))
        else:
            operando2 = pila.pop()
            operando1 = pila.pop()
            if token == '+':
                pila.append(operando1 + operando2)
            elif token == '-':
                pila.append(operando1 - operando2)
            elif token == '*':
                pila.append(operando1 * operando2)
            elif token == '/':
                pila.append(operando1 / operando2)
    return pila.pop()

expresion_posfija = "3 4 + 2 *"
resultado = evaluar_expresion_posfija(expresion_posfija)
print("Resultado de la expresión posfija:", resultado)
#9Validar operadores anidados utilizando una pila:
def validar_operadores(expresion):
    pila = []
    for caracter in expresion:
        if caracter in "([{":
            pila.append(caracter)
        elif caracter in ")]}":
            if not pila:
                return False
            elif caracter == ")" and pila[-1] != "(":
                return False
            elif caracter == "]" and pila[-1] != "[":
                return False
            elif caracter == "}" and pila[-1] != "{":
                return False
            pila.pop()
    return not pila

expresion_valida = "{[()]}"
expresion_invalida = "{[(])}"
print("Expresión válida:", expresion_valida, validar_operadores(expresion_valida))
print("Expresión válida:", expresion_invalida, validar_operadores(expresion_invalida))

#10 Ordenar una pila de manera ascendente utilizando estructuras adicionales:
def ordenar_pila(pila):
    pila_auxiliar = []
    while pila:
        temp = pila.pop()
        while pila_auxiliar and pila_auxiliar[-1] > temp:
            pila.append(pila_auxiliar.pop())
        pila_auxiliar.append(temp)
    return pila_auxiliar

pila = [3, 1, 4, 1, 5, 9, 2, 6, 5]
pila_ordenada = ordenar_pila(pila)
print("Pila ordenada:", pila_ordenada)

#11Eliminar elementos duplicados de una pila:
def eliminar_duplicados_pila(pila):
    elementos_unicos = set()
    pila_resultado = []
    while pila:
        elemento = pila.pop()
        if elemento not in elementos_unicos:
            elementos_unicos.add(elemento)
            pila_resultado.append(elemento)
    while pila_resultado:
        pila.append(pila_resultado.pop())
    return pila

pila_con_duplicados = [1, 2, 3, 3, 4, 5, 5, 6]
pila_sin_duplicados = eliminar_duplicados_pila(pila_con_duplicados)
print("Pila original:", pila_con_duplicados)
print("Pila sin duplicados:", pila_sin_duplicados)

#12Implementar una calculadora que pueda realizar operaciones básicas utilizando una pila para evaluar expresiones:
def calcular_expresion(expresion):
    pila = []
    operadores = {'+', '-', '*', '/'}
    for token in expresion.split():
        if token not in operadores:
            pila.append(float(token))
        else:
            operando2 = pila.pop()
            operando1 = pila.pop()
            if token == '+':
                pila.append(operando1 + operando2)
            elif token == '-':
                pila.append(operando1 - operando2)
            elif token == '*':
                pila.append(operando1 * operando2)
            elif token == '/':
                pila.append(operando1 / operando2)
    return pila.pop()

expresion_calculadora = "3 4 + 2 *"
resultado_calculadora = calcular_expresion(expresion_calculadora)
print("Resultado de la calculadora:", resultado_calculadora)

#13Comprobar si una palabra o frase es un palíndromo utilizando una pila:
def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    pila = []
    for caracter in texto:
        pila.append(caracter)
    texto_invertido = ''
    while pila:
        texto_invertido += pila.pop()
    return texto == texto_invertido

palabra = "Anita lava la tina"
print("Es palíndromo:", es_palindromo(palabra))

#14Implementar un sistema simple de "deshacer" utilizando dos pilas:
class UndoSystem:
    def __init__(self):
        self.acciones = []
        self.deshaceres = []

    def hacer(self, accion):
        self.acciones.append(accion)

    def deshacer(self):
        if self.acciones:
            accion_deshacer = self.acciones.pop()
            self.deshaceres.append(accion_deshacer)
            print("Deshaciendo:", accion_deshacer)
        else:
            print("No hay acciones para deshacer")

    def rehacer(self):
        if self.deshaceres:
            accion_rehacer = self.deshaceres.pop()
            self.acciones.append(accion_rehacer)
            print("Rehaciendo:", accion_rehacer)
        else:
            print("No hay deshaceres para rehacer")
undo_system = UndoSystem()
undo_system.hacer("Escribir mensaje 1")
undo_system.hacer("Escribir mensaje 2")
undo_system.deshacer()
undo_system.rehacer()



