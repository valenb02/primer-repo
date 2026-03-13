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

# [1,2,3,4,5] 5 = 2

def cant_parejas_q_suman(s: list[int], num: int) -> int:
    parejas_que_suman : int = 0
    for i in range(len(s)):
        for j in range(i + 1,len(s)):
            if s[i] + s[j] == num:
                parejas_que_suman += 1
    return parejas_que_suman

def obtener_col(matriz: list[list[int]], col: int) -> list[int]:
    columnas : int = len(matriz[0])
    columna : list[int] = []
    for j in range(columnas):
        for i in range(len(matriz)):
            if j == col:
                columna.append(matriz[i][j])
    return columna

def invertir(columna: list[int]) -> list[int]:
    res : list[int] = []
    for i in range(len(columna) - 1, -1, -1):
        res.append(columna[i])
    return res

# [[1,2,3],           [1,9,8]
#  [4,5,6],   1  2 =  [4,6,5]
#  [7,8,9]]           [7,3,2]

def intercambiar_e_invertir_columnas(matriz: list[list[int]], col1: int, col2:int) -> list[list[int]]:
    columnas_matriz_original : int = len(matriz[0])
    res : list[list[int]] = []
    for j in range(columnas_matriz_original):
        if j != col1 and j != col2:
            res.append(obtener_col(matriz,j))
        elif j == col1:
            res.append(invertir(obtener_col(matriz, col2)))
        else:
            res.append(invertir(obtener_col(matriz,col2)))
    return res


# {"valen": "neco", "caro": "lobe", "maxi": "mdq", "rodri": "neco"}, {"valen": "bsas", "caro": "neco", "maxi": "mdq", "rodri": "neco"} =
#                 {"neco": 1, "lobe": 0,  "mdq": 1} }

def mantuvieron_residencia(censo1: dict[str,str], censo2: dict[str,str]) -> dict[str,int]:
    dicc_res : dict[str,int] = {}
    for localidad in censo1.values():
        dicc_res[localidad] = 0
    for ciudadano in censo2:
        ciudad = censo1[ciudadano]
        if ciudad == censo2[ciudadano]:
            dicc_res[ciudad] += 1
    return dicc_res
