from typing import Any

# INTENTA VOLVER A HACER RESULTADOMATERIA E INTENTAR RECORDAR DE MEMORIA SI TE QUEDO CLARO DE QUE PASA SEGUN SI LAS CONDICIONES DENTRO DEL BLOQUE IF
# SON VERDADERAS O FALSAS.

# por ahora digo que siempre y cuando sean verdaderas el bloque continua y si son falsas entonces se terminan ahi. Lo pertinente es preguntarse
# si necesito recorrer toda la lista para afirmar algo o si puedo cortar antes

def pertenece(s: list[Any], elem: Any) -> bool:
    for elemento in s:
        if elemento == elem:
            return True
    return False

def sin_vocales(s: str) -> str:
    res : str = ""
    vocales : str = "aeiou"
    for elem in s:
        if not pertenece(vocales,elem.lower()):
            res += elem
    return res

def reemplaza_vocales(s: str) -> str:
    res : str = ""
    vocales : str = "aeiou"
    for letra in s:
        if not pertenece(vocales, letra.lower()):
            res += letra
        else:
            res += "-"
    return res
#######################################
def da_vuelta_str(palabra: str) -> str:
    palabra_res : str = ""
    for i in range(len(palabra) - 1,-1, -1): # el fin es -1 porque no se incluye nunca; el fin no se incluye nunca
        palabra_res += palabra[i]
    return palabra_res

def eliminar_repetidos(palabra: str) -> str:
    palabra_aux : str = ""
    palabra_res : str = ""
    for letra in palabra:
        if not pertenece(palabra_aux, letra):
            palabra_res += letra
            palabra_aux += letra
    return palabra_res


def promedio(notas: list[int]) -> float:
    suma_notas : int = 0
    cant_notas : int = 0
    for nota in notas:
        suma_notas += nota
        cant_notas += 1
    return suma_notas / cant_notas

def resultadoMateria(notas: list[int]) -> int:
    prom : float = promedio(notas)
    for nota in notas:                              # esta manera me permite recorrer toda la lista primero y si me topo como un numero menor
                                                    # a 4 entonces de una devuelvo 3, pero si puedo salir del for entonces es porque no hay ningun
                                                    # numero menor a 4 en la lista, y eso me divide en los dos casos del if, en los cuales hay promedios
                                                    # entre 4 y 7 y hay promedios mayores a 7
        if nota < 4:
            return 3
    if prom < 4:
        return 3
    elif 4 <= prom < 7:
        return 2
    else:
        return 1


# [5,6,7,1,8] (5.4) = 3
# [5,6,7,5,8] (6.2) = 2  # intentar hacer esta otra vez! mañana u otro dia 
# [6,6,7,8,8] (7.0) = 1

def saldoActual(movimientos: list[tuple[str,int]]) -> int:
    saldo_actual : int = 0
    for tupla in movimientos:
        if tupla[0] == 'I':
            saldo_actual += tupla[1]
        else:
            saldo_actual -= tupla[1]
    return saldo_actual
