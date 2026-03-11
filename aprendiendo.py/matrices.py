# REHACIENDO RESULTADOMATERIA Y RECORDANDO QUE PASA CON LAS CONDICIONES DEL IF EN EL CASO DE LAS LISTAS SEGUN NECESITE RECORRER O NO TODA LA LISTA

# Si no necesito recorrer toda la lista, entonces conviene poner una condicion que de una se vuelva verdadera si ocurre lo que necesito. 
# Si necesito recorrer toda la lista entonces conviene dejar el False al final, digamos recorro toda la lista y si llego al false es porque
# la recorrí toda y evidentemente al final no pasa.

def promedio(notas: list[int]) -> float:
    suma_notas : int = 0
    cant_notas : int = 0
    for nota in notas:
        suma_notas += nota
        cant_notas += 1
    return suma_notas / cant_notas

def resultadoMateria(notas: list[int]) -> int:
    prom : int = promedio(notas)
    for nota in notas:
        if nota < 4 or prom < 4:
            return 3
    if prom <= 7:
        return 2
    else:
        return 1

#REHACIENDO POS SECUENCIA ORDENADA MAS LARGA


def pos_seq_ord_mas_larga(lista: list[int]) -> int:
    longitud_mayor : int = 1
    longitud_actual : int = 1
    inicio_actual : int = 0
    inicio_mayor : int = 0
    for i in range(1,len(lista)):
        if lista[i] >= lista[i-1]:
            longitud_actual += 1
        else:
            if longitud_actual > longitud_mayor:
                longitud_mayor = longitud_actual
                inicio_mayor = inicio_actual
            longitud_actual = 1
            inicio_actual = i # acá medio que lo que me estoy guardando es el indice potencial a ser en el q inicia la subsecuencia mas larga xq
                              # si se entra a este if es porque ocurrio que la longitud de la subsecuen es mas larga q la anterior. O sea
                              # me guardo el indice antes de arrancar y dsp me fijo si la guardo o no como subsecuen mas larga. Al principio parece
                              # que no hay indice pero si lo hay, es el indice 0 que esta guardado porque inicio actual arranca siendo 0 
    if longitud_actual >= longitud_mayor:
                longitud_mayor = longitud_actual
                inicio_mayor = inicio_actual
    return inicio_mayor

def pertenece(s: list[int], elem: int) -> bool:
    for elemento in s:
        if elemento == elem:
            return True
    return False

def pertenece_a_cada_unoV1(matriz: list[list[int]], e: int, res: list[bool]):
    for fila in matriz:
        res.append(pertenece(fila,e))
    return res

# es matriz si la longitud de las filas son mayor a 0 y ademas todas las filas tienen la misma longitud

def es_matriz(matriz: list[list[int]]) -> bool:
    longitud_primera_fila : int = len(matriz[0])
    if longitud_primera_fila == 0:
        return False
    for filas in matriz: 
        if len(filas) != longitud_primera_fila:
            return False
    return True

def es_matriz2(matriz: list[list[int]]) -> bool:
    if len(matriz) == 0 or len(matriz[0]) == 0:
        return False

    longitud = len(matriz[0])
    es_rectangular = True

    for fila in matriz:
        if len(fila) != longitud:
            es_rectangular = False

    return es_rectangular

def ordenadas(filas: list[int]) -> bool:
    for i in range(1,len(filas)):
        if filas[i] <= filas[i-1]:
            return False
    return True

def filas_ordenadas(matriz: list[list[int]], res: list[bool]):
    for filas in matriz:
        res.append(ordenadas(filas))

def columna(matriz: list[list[int]], columna: int) -> list[int]:
    columna_res : list[int] = []
    for fila in matriz:
        columna_res.append(fila[columna])
    return columna_res

        
def columnas_ordenadas(matriz: list[list[int]]) -> list[bool]:
    res : list[bool] = []
    for i in range(len(matriz[0])):
        obtener_columna : list[int] = columna(matriz, i)
        res.append(ordenadas(obtener_columna))
    return res

# [[1,2,3]   [1,4,7]
#  [4,5,6] = [2,5,8]
#  [7,8,9]]  [3,6,9]

def transponer(m: list[list[int]]) -> list[list[int]]:
    res : list[list[int]] = []
    for i in range(len(m[0])):
        obtener_columna : list[int] = columna(m, i)
        res.append(obtener_columna)
    return res

print(transponer([[1,2,3],[4,5,6],[7,8,9]]))

# intentarla volver a hacer
