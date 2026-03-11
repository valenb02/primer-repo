def hay_repetidos_consecutivos(v: list[int]) -> bool:
    actual : int = v[0]
    hay : bool = False
    for i in range(1,len(v)):
        if actual == v[i]:
            hay = True
        actual = v[i]
    return hay

# flag para recordar algo que pasó:

# [1,0,2,5] = True
# [9,8,1,0,1] = False

def hay_cero_y_luego_positivo(v: list[int]) -> bool:
    aparecio_cero = False
    hay = False
    for num in v:
        if num == 0:
            aparecio_cero = True
        if num > 0 and aparecio_cero:
            hay = True
    return hay

# sin flag:
def hay_cero_y_luego_positivo(v: list[int]) -> bool:
    for i in range(len(v)):
        if v[i] == 0:
            for j in range(i+1, len(v)):
                if v[j] > 0:
                    return True
    return False

# ejercicio tipo parcial con flag:

# [1,2,2,2,3] → True
# [4,4,4] → False

def hay_meseta(lista: list[int]) -> bool:
    meseta : bool = False
    contador : int = 1
    inicio_racha : int = 0
    for i in range(1,len(lista)):
        if lista[i] == lista[i-1]:
            contador += 1
        else:
            if contador >= 3 and inicio_racha > 0:
                meseta = True   # preguntar cual es la diferencia a si hubiese puesto return True aca 
            contador = 1
            inicio_racha = i

    if contador >= 3 and inicio_racha > 0:
        meseta = True
    return meseta






