#1Verificar si una palabra es palíndroma utilizando una cola:
from collections import deque

def es_palindroma(palabra):
    cola = deque(palabra)
    while len(cola) > 1:
        if cola.popleft() != cola.pop():
            return False
    return True

palabra = "reconocer"
print("¿Es palíndroma?", es_palindroma(palabra))

#2Sistema de gestión de pedidos utilizando una cola:
from collections import deque

class SistemaGestionPedidos:
    def __init__(self):
        self.cola_pedidos = deque()

    def agregar_pedido(self, pedido):
        self.cola_pedidos.append(pedido)

    def procesar_pedido(self):
        if self.cola_pedidos:
            return self.cola_pedidos.popleft()
        else:
            return "No hay pedidos para procesar"

    def mostrar_estado_cola(self):
        print("Estado actual de la cola de pedidos:")
        for pedido in self.cola_pedidos:
            print(pedido)

# Uso del sistema de gestión de pedidos
sistema_pedidos = SistemaGestionPedidos()
sistema_pedidos.agregar_pedido("Pedido 1")
sistema_pedidos.agregar_pedido("Pedido 2")
sistema_pedidos.agregar_pedido("Pedido 3")
print(sistema_pedidos.procesar_pedido())
print(sistema_pedidos.procesar_pedido())
sistema_pedidos.mostrar_estado_cola()

#3Búsqueda de rutas en un laberinto utilizando BFS y una cola:
from collections import deque

def encontrar_ruta_laberinto(laberinto, inicio, fin):
    if laberinto[inicio[0]][inicio[1]] == 1 or laberinto[fin[0]][fin[1]] == 1:
        return "Inicio o fin en una pared"
    filas = len(laberinto)
    columnas = len(laberinto[0])
    visitado = [[False] * columnas for _ in range(filas)]
    cola = deque([(inicio, 0)])
    visitado[inicio[0]][inicio[1]] = True
    while cola:
        actual, distancia = cola.popleft()
        if actual == fin:
            return distancia
        for vecino in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            fila_vecino = actual[0] + vecino[0]
            columna_vecino = actual[1] + vecino[1]
            if 0 <= fila_vecino < filas and 0 <= columna_vecino < columnas and laberinto[fila_vecino][columna_vecino] == 0 and not visitado[fila_vecino][columna_vecino]:
                visitado[fila_vecino][columna_vecino] = True
                cola.append(((fila_vecino, columna_vecino), distancia + 1))
    return "No hay ruta"

laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
inicio = (0, 0)
fin = (4, 4)
print("Distancia mínima:", encontrar_ruta_laberinto(laberinto, inicio, fin))

#4Sistema de gestión de tareas utilizando una cola:
from collections import deque

class SistemaGestionTareas:
    def __init__(self):
        self.cola_tareas = deque()

    def agregar_tarea(self, tarea):
        self.cola_tareas.append(tarea)

    def marcar_completada(self):
        if self.cola_tareas:
            return self.cola_tareas.popleft()
        else:
            return "No hay tareas pendientes"

    def mostrar_proxima_tarea(self):
        if self.cola_tareas:
            return self.cola_tareas[0]
        else:
            return "No hay tareas pendientes"

# Uso del sistema de gestión de tareas
sistema_tareas = SistemaGestionTareas()
sistema_tareas.agregar_tarea("Tarea 1")
sistema_tareas.agregar_tarea("Tarea 2")
print("Próxima tarea:", sistema_tareas.mostrar_proxima_tarea())
print("Tarea completada:", sistema_tareas.marcar_completada())
print("Próxima tarea:", sistema_tareas.mostrar_proxima_tarea())
###ARBOLES##
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def contar_nodos(arbol):
    if arbol is None:
        return 0
    return 1 + contar_nodos(arbol.izquierda) + contar_nodos(arbol.derecha)

def contar_nodos_hoja(arbol):
    if arbol is None:
        return 0
    if arbol.izquierda is None and arbol.derecha is None:
        return 1
    return contar_nodos_hoja(arbol.izquierda) + contar_nodos_hoja(arbol.derecha)

def contar_nodos_internos(arbol):
    if arbol is None or (arbol.izquierda is None and arbol.derecha is None):
        return 0
    return 1 + contar_nodos_internos(arbol.izquierda) + contar_nodos_internos(arbol.derecha)

def altura_arbol(arbol):
    if arbol is None:
        return 0
    return 1 + max(altura_arbol(arbol.izquierda), altura_arbol(arbol.derecha))

def profundidad_nodo(arbol, valor_nodo, profundidad=0):
    if arbol is None:
        return None
    if arbol.valor == valor_nodo:
        return profundidad
    izquierda = profundidad_nodo(arbol.izquierda, valor_nodo, profundidad + 1)
    derecha = profundidad_nodo(arbol.derecha, valor_nodo, profundidad + 1)
    if izquierda is not None:
        return izquierda
    return derecha

def minimo_valor(arbol):
    if arbol is None:
        return float('inf')
    return min(arbol.valor, min(minimo_valor(arbol.izquierda), minimo_valor(arbol.derecha)))

def maximo_valor(arbol):
    if arbol is None:
        return float('-inf')
    return max(arbol.valor, max(maximo_valor(arbol.izquierda), maximo_valor(arbol.derecha)))

# Ejemplo de uso
# Crear un árbol de ejemplo
arbol_ejemplo = Nodo(10)
arbol_ejemplo.izquierda = Nodo(5)
arbol_ejemplo.derecha = Nodo(15)
arbol_ejemplo.izquierda.izquierda = Nodo(3)
arbol_ejemplo.izquierda.derecha = Nodo(8)
arbol_ejemplo.derecha.derecha = Nodo(20)

#5 Contar nodos en el árbol
print("Cantidad de nodos en el árbol:", contar_nodos(arbol_ejemplo))

#6Contar nodos hoja en el árbol
print("Cantidad de nodos hoja en el árbol:", contar_nodos_hoja(arbol_ejemplo))

#7Contar nodos internos en el árbol
print("Cantidad de nodos internos en el árbol:", contar_nodos_internos(arbol_ejemplo))

#8Calcular altura del árbol
print("Altura del árbol:", altura_arbol(arbol_ejemplo))

#9Calcular profundidad de un nodo en el árbol
valor_nodo = 8
print("Profundidad del nodo con valor", valor_nodo, ":", profundidad_nodo(arbol_ejemplo, valor_nodo))

#10Encontrar el mínimo valor en el árbol
print("Valor mínimo en el árbol:", minimo_valor(arbol_ejemplo))

#11Encontrar el máximo valor en el árbol
print("Valor máximo en el árbol:", maximo_valor(arbol_ejemplo))




