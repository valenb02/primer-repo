from queue import Queue as Cola
import random

def generar_nros_al_azar(cant: int, desde: int, hasta: int) -> Cola[int]:
    cola_res = Cola()
    for _ in range(cant):
        cola_res.put(random.randint(desde,hasta))
    return cola_res

def cantidad_elementos(c: Cola) -> int:
    cola_aux = Cola()
    cantidad : int = 0
    while not c.empty():
        elem_cola = c.get()
        cantidad += 1
        cola_aux.put(elem_cola)
    while not cola_aux.empty():
        c.put(cola_aux.get())
    return cantidad

def buscar_el_max(c: Cola) -> int:
    max : int = c.get()
    cola_aux = Cola()
    while not c.empty():
        elem_cola : int = c.get()
        if elem_cola > max:
            max = elem_cola
        cola_aux.put(elem_cola)
    while not cola_aux.empty():
        c.put(cola_aux.get())
    return max

def buscar_nota_minima(c: Cola[tuple[str,int]]) -> tuple[str, int]:
    nota_minima : tuple[str,int] = c.get()
    cola_aux = Cola()
    cola_aux.put(nota_minima)
    while not c.empty():
        obtener_elem : tuple[str,int] = c.get()
        if obtener_elem[1] < nota_minima[1]:
            nota_minima = obtener_elem
        cola_aux.put(obtener_elem)
    while not cola_aux.empty():
        c.put(cola_aux.get())
    return nota_minima


def intercalar(c1: Cola, c2: Cola) -> Cola:
    cola_res = Cola()
    cola_aux = Cola()
    while not c1.empty():
        obtener_elem_c1 : int = c1.get()
        obtener_elem_c2 : int = c2.get()
        cola_aux.put(obtener_elem_c1)
        cola_aux.put(obtener_elem_c2)
    while not cola_aux.empty():
        elem_cola_aux = cola_aux.get()
        cola_res.put(elem_cola_aux)
        c1.put(elem_cola_aux)
        c2.put(elem_cola_aux)
    return cola_res

def pacientes_urgentes(c: Cola[int,str,str]) -> int:
    prioridad : int = 0
    cola_aux = Cola()
    while not c.empty():
        tupla : tuple[int, str, str] = c.get()
        if tupla[0] < 4:
            prioridad += 1
        cola_aux.put(tupla)
    while not cola_aux.empty():
        elemento = cola_aux.get()
        c.put(elemento)
    return prioridad


def atencion_a_clientes(c: Cola[tuple[str,int,bool,bool]]) -> Cola[tuple[str,int,bool,bool]]:
    cola_aux = Cola()
    cola_res = Cola()
    cola_normales = Cola()
    cola_prioridades = Cola()
    while not c.empty():
        cuadrupla : tuple[str,int,bool,bool] = c.get()
        if cuadrupla[3]:
            cola_res.put(cuadrupla)
        elif cuadrupla[2]:
            cola_prioridades.put(cuadrupla)
        else:
            cola_normales.put(cuadrupla)
        cola_aux.put(cuadrupla)
    while not cola_prioridades.empty():
        cola_res.put(cola_prioridades.get())
    while not cola_normales.empty():
        cola_res.put(cola_normales.get())
    while not cola_aux.empty():
        c.put(cola_aux.get())
    return cola_res

c = Cola()
c.put(("Valen B", 44049734, False, False)) #4
c.put(("Rodri B", 44049734, True, False)) #3 
c.put(("Caro E", 20826315, False, True))#1
c.put(("Cesar B", 12938373, True, True)) #2

cola_atencion = atencion_a_clientes(c)
while not cola_atencion.empty():
    print(cola_atencion.get())

