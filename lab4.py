# 1.
def validar_edad(edad):
    # Verifica si la edad es un entero positivo y está dentro del rango válido
    if isinstance(edad, int) and 0 < edad <= 150:
        return True  # La edad es válida
    else:
        return False  # La edad no es válida
edad_usuario = 25
print("La edad del usuario es válida:", validar_edad(edad_usuario))


# 2.
def verificar_tipo_dato(variable, tipo):
    # Comprueba si el tipo de la variable coincide con el tipo especificado
    return isinstance(variable, tipo)
variable = 10
print("La variable es de tipo entero:", verificar_tipo_dato(variable, int))


# 3.
def validar_calificacion(calificacion):
    # Verifica si la calificación está dentro del rango válido
    return 0 <= calificacion <= 100
calificacion = 85
print("La calificación es válida:", validar_calificacion(calificacion))


# 4.
def asegurar_lista_no_vacia(lista):
    # Verifica si la lista no está vacía
    return bool(lista)
mi_lista = [1, 2, 3]
print("La lista no está vacía:", asegurar_lista_no_vacia(mi_lista))


# 5.
def validar_igualdad(objeto1, objeto2):
    # Compara si dos objetos son iguales
    return objeto1 == objeto2

objeto1 = "hola"
objeto2 = "Hola"
print("Los objetos son iguales:", validar_igualdad(objeto1.lower(), objeto2.lower()))


# 6.
def ciclo_while_al_menos_una_vez():
    cont = 0
    while True:  # Se inicia un ciclo infinito
        cont += 1  # Se incrementa el contador en cada iteración
        if cont >= 5:  # Se verifica si se alcanza cierto valor en el contador
            break  # Si se alcanza, se rompe el ciclo
    return cont  # Se devuelve el valor del contador
print("El ciclo se ejecutó al menos una vez y contó hasta:", ciclo_while_al_menos_una_vez())


# 7.
def funcion_retorna_valor_especifico(numero):
    if numero < 0:
        return "Negativo"  # Si el número es negativo, se devuelve "Negativo"
    elif numero == 0:
        return "Cero"  # Si el número es cero, se devuelve "Cero"
    else:
        return "Positivo"  # Si el número es positivo, se devuelve "Positivo"
print("La función retorna un valor específico:", funcion_retorna_valor_especifico(5) == "Positivo")


# 8.
def validar_estado_variable_despues_operacion(numero):
    numero *= 2  # Se multiplica el número por 2
    return numero  # Se devuelve el valor del número después de la operación
numero = 5
numero = validar_estado_variable_despues_operacion(numero)
print("El estado de la variable después de la operación es:", numero)


# 9.
def asegurar_modulo_importado(nombre_modulo):
    try:
        __import__(nombre_modulo)  # Intenta importar el módulo especificado
        return True  # Si se importa correctamente, devuelve True
    except ImportError:
        return False  # Si hay un error al importar, devuelve False
print("El módulo 'random' se ha importado correctamente:", asegurar_modulo_importado("random"))


# 10:
class Nodo:
    def __init__(self, dato):
        self.dato = dato  # Almacena el dato del nodo
        self.siguiente = None  # Apunta al siguiente nodo en la lista


# Clase para la lista enlazada simple
class ListaEnlazada:
    def __init__(self):
        self.head = None  # Inicializa la cabeza de la lista como None

    # Método para insertar un nodo al inicio de la lista
    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)  # Crea un nuevo nodo con el dato proporcionado
        nuevo_nodo.siguiente = self.head  # El nuevo nodo apunta al nodo actual de la cabeza
        self.head = nuevo_nodo  # El nuevo nodo se convierte en la cabeza de la lista

    # Método para buscar un nodo en la lista
    def buscar_nodo(self, dato):
        actual = self.head  # Comienza desde la cabeza de la lista
        while actual:
            if actual.dato == dato:  # Si el dato del nodo actual es igual al dato buscado
                return True  # Se encontró el dato, devuelve True
            actual = actual.siguiente  # Avanza al siguiente nodo en la lista
        return False  # Si no se encuentra el dato, devuelve False

mi_lista = ListaEnlazada()  # Crea una lista enlazada vacía
mi_lista.insertar_al_inicio(10)  # Inserta un nodo con dato 10
mi_lista.insertar_al_inicio(20)  # Inserta un nodo con dato 20
mi_lista.insertar_al_inicio(30)  # Inserta un nodo con dato 30
print("¿El nodo con dato 20 está en la lista?", mi_lista.buscar_nodo(20))  # Busca el nodo con dato 20 en la lista


#11:
def suma_nodos(lista_enlazada):
    suma = 0  # Inicializa la suma en 0
    actual = lista_enlazada.head  # Comienza desde la cabeza de la lista
    while actual:
        suma += actual.dato  # Suma el dato del nodo actual
        actual = actual.siguiente  # Avanza al siguiente nodo en la lista
    return suma  # Devuelve la suma total de los nodos
print("La suma de todos los nodos de la lista es:", suma_nodos(mi_lista))


#12:
def longitud_lista(lista_enlazada):
    longitud = 0  # Inicializa la longitud en 0
    actual = lista_enlazada.head  # Comienza desde la cabeza de la lista
    while actual:
        longitud += 1  # Incrementa la longitud por cada nodo encontrado
        actual = actual.siguiente  # Avanza al siguiente nodo en la lista
    return longitud  # Devuelve la longitud total de la lista
print("La longitud de la lista es:", longitud_lista(mi_lista))


#13:
def concatenar_listas(lista1, lista2):
    if not lista1.head:  # Si la lista1 está vacía
        return lista2  # Retorna lista2 como la lista concatenada
    actual = lista1.head  # Comienza desde la cabeza de la lista1
    while actual.siguiente:  # Mientras haya un siguiente nodo en la lista1
        actual = actual.siguiente  # Avanza al siguiente nodo en la lista1
    actual.siguiente = lista2.head  # Une el final de la lista1 con el inicio de lista2
    return lista1  # Devuelve la lista1 con lista2 concatenada
mi_lista2 = ListaEnlazada()
mi_lista2.insertar_al_inicio(40)
mi_lista2.insertar_al_inicio(50)
concatenada = concatenar_listas(mi_lista, mi_lista2)
actual = concatenada.head
while actual:
    print(actual.dato, end=" ")
    actual = actual.siguiente


#14:
def eliminar_duplicados(lista_enlazada):
    valores = set()  # Crea un conjunto para almacenar valores únicos
    actual = lista_enlazada.head  # Comienza desde la cabeza de la lista
    previo = None  # Mantener un seguimiento del nodo anterior
    while actual:
        if actual.dato in valores:  # Si el dato del nodo actual ya está en el conjunto
            previo.siguiente = actual.siguiente  # Elimina el nodo duplicado conectando el anterior con el siguiente
        else:
            valores.add(actual.dato)  # Agrega el dato del nodo actual al conjunto
            previo = actual  # Actualiza el nodo anterior al nodo actual
        actual = actual.siguiente  # Avanza al siguiente nodo en la lista
mi_lista.insertar_al_inicio(20)
mi_lista.insertar_al_inicio(10)
print("\nLista con duplicados:")
actual = mi_lista.head
while actual:
    print(actual.dato, end=" ")
    actual = actual.siguiente
eliminar_duplicados(mi_lista)
print("\nLista sin duplicados:")
actual = mi_lista.head
while actual:
    print(actual.dato, end=" ")
    actual = actual.siguiente


#15:
def invertir_lista(lista_enlazada):
    previo = None  # Nodo previo
    actual = lista_enlazada.head  # Comienza desde la cabeza de la lista
    siguiente = None  # Nodo siguiente
    while actual:
        siguiente = actual.siguiente  # Guarda el siguiente nodo
        actual.siguiente = previo  # Cambia el puntero del nodo actual al previo
        previo = actual  # Actualiza el nodo previo al nodo actual
        actual = siguiente  # Actualiza el nodo actual al siguiente nodo
    lista_enlazada.head = previo  # La cabeza de la lista es ahora el último nodo

print("\nLista original:")
actual = concatenada.head
while actual:
    print(actual.dato, end=" ")
    actual = actual.siguiente
invertir_lista(concatenada)
print("\nLista invertida:")
actual = concatenada.head
while actual:
    print(actual.dato, end=" ")
    actual = actual.siguiente

