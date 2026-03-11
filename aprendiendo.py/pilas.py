from queue import LifoQueue as Pila, Queue as Cola
import random

def generar_nros_al_azar(cant: int, desde: int, hasta: int) -> Pila[int]:
    i : int = 0
    pila_res : Pila[int] = Pila()
    while i < cant:
        generar_numeros : int = random.randint(desde, hasta)
        pila_res.put(generar_numeros)
        i += 1
    return pila_res

def cant_elementos(p: Pila) -> int:
    pila_aux : Pila = Pila()
    cantidad_elem : int = 0
    while not p.empty():
        cantidad_elem += 1
        elemento_pila = p.get()
        pila_aux.put(elemento_pila)
    while not pila_aux.empty():
        obtener_elem_pila_aux = pila_aux.get()
        p.put(obtener_elem_pila_aux)
    return cantidad_elem

def buscar_el_max(p: Pila) -> int:
    pila_aux : Pila = Pila()
    maximo_res : int = p.get()
    pila_aux.put(maximo_res)
    while not p.empty():
        obtener_elem_pila : int = p.get()
        if obtener_elem_pila > maximo_res:
            maximo_res = obtener_elem_pila
        pila_aux.put(obtener_elem_pila)
    while not pila_aux.empty():
        p.put(pila_aux.get())
    return maximo_res

def buscar_nota_maxima(p: Pila[tuple[str,int]]) -> tuple[str, int]:
    pila_aux : Pila = Pila()
    res : tuple = p.get()
    pila_aux.put(res)
    while not p.empty():
        obtener_tupla : tuple = p.get()
        if obtener_tupla[1] > res[1]:
            res = obtener_tupla
        pila_aux.put(obtener_tupla)
    while not pila_aux.empty():
        p.put(pila_aux.get())
    return res

def esta_bien_balanceada(s: list[str]) -> bool:
    p = Pila()
    for char in s:
        if char == '(':
            p.put(char)
        elif char == ')':
            if p.empty():
                return False
        p.get()
    return p.empty()

def intercalar(p1: Pila, p2: Pila) -> Pila:
    pila_aux = Pila
    pila_res = Pila
    while not p1.empty():
        elem_p2 = p2.get()
        elem_p1 = p1.get()
        pila_aux.put(elem_p2)
        pila_aux.put(elem_p1)
    while not pila_aux.empty():
        pila_res.put(pila_aux.get())
        p1.put(pila_aux.get())
        p2.put(pila_aux.get())
    return pila_res
