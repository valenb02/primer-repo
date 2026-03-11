from queue import Queue as Cola


def max_cantidades_consecutivos(v: list[int]) -> dict[int, int]:
    res = {}
    for num in v:
        if num not in res:
            res[num] = 1

    actual = v[0]
    cant_apariciones_conse = 1

    for i in range(1, len(v)):
        if v[i] == actual:
            cant_apariciones_conse += 1
        else:
            if cant_apariciones_conse > res[actual]:
                res[actual] = cant_apariciones_conse
            actual = v[i]
            cant_apariciones_conse = 1

    if cant_apariciones_conse > res[actual]:
        res[actual] = cant_apariciones_conse

    return res

def es_primo(num: int) -> bool:
    if num < 2:
        return False
    i : int = 2
    while i < num:
        if num % i == 0: #no necesito recorrer toda la lista, asi la condicion es exactamente lo que quiero
            return False # y un falso DIRECTO si no se cumple
        i += 1
    return True

def max_cantidad_primos(A: list[list[int]]) -> int:
    mayor_cant_primos : int = 0
    contador_de_primos : int = 0
    columnas : int = len((A[0]))
    for j in range(columnas):
        for i in range(len(A)):
            if es_primo(A[i][j]):
                contador_de_primos += 1
        if contador_de_primos > mayor_cant_primos:
            mayor_cant_primos = contador_de_primos
        contador_de_primos = 0
    return mayor_cant_primos

def tuplas_positivas_y_negativas(c: Cola[tuple[int,int]]):
    cola_tuplas_negativas : Cola[tuple[int, int]] = Cola()
    cola_res : Cola[tuple[int, int]] = Cola()
    while not c.empty():
        tupla : tuple[int,int] = c.get()
        producto : int = tupla[0] * tupla[1]
        if producto > 0:
            cola_res.put(tupla)
        else:
            if producto != 0:
                cola_tuplas_negativas.put(tupla)
    while not cola_tuplas_negativas.empty():
        cola_res.put(cola_tuplas_negativas.get())
    while not cola_res.empty():
        c.put(cola_res.get())
