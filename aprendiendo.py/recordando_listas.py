# recordemos que en el caso de que necesitemos devolver un booleano luego de recorrer una lista por completo, es necesario que pedir una condicion
# contraria a lo que necesitamos y un False si esa condicion contraria se llegara a cumplir, porque considerando que los return son automaticos, entonces
# en ese caso la funcion devolverá un False de una, y un True si logra terminar el recorrido

# EJEMPLOS:

def pertenece_2(lista: list[int], elem: int) -> bool:
    for elemento in lista:
        if elemento != elem:
            return False
    return True

def todos_multiplos_del_elemento(lista: list[int], num: int) -> bool:
    for elemento in lista:
        if elemento % num != 0:
            return False
    return True

# los for in range son preferibles cuando por alguna razon necesitamos comparar los elementos de una lista entre si, normalmente si estamos buscando
# "el más" o "el menos" de una lista o cuando si o si necesitamos hacer referencia a un indice porque necesitamos, justamente, devolver el indice, o
# porque necesitamos devolver un bool respecto a una condicion que se tiene que dar entre el orden o caracteristica ENTRE ellos

# ejemplo:

def maximo(lista: list[int]) -> int:
    max : int = lista[0]
    for i in range(1, len(lista)):
        if max < lista[i]:
            max = lista[i]
    return max

# esta version está bien pero es menos normal!
def ordenados(lista: list[int]) -> bool:
    actual : int = lista[0]
    for i in range(1,len(lista)):
        if actual <= lista[i]:
            actual = lista[i]
        else:
            return False
    return True
        
# notar que el range va hasta len lista - 1, ya que el "hasta" del range es no inclusivo asi que siempre va en realidad hasta el anteultimo (incluyendolo)
# asi que como yo voy a estar comparando el actual con el que sigue hasta el final, me gustaria encontrar la manera de compara el que estoy con el que sigue
# sin salirme del range, y la forma es hacer len(lista)-1, que logra que, si por ejemplo, la lista fuera [1,2,3,4] len - 1 recorre hasta 3, incluido
# pero hace que la comparacion que está en la condicion incluya el lista[3] >= lista[4]

def ordenados_2(lista: list[int]) -> bool:
    for i in range(len(lista) - 1):
        if lista[i] >= lista[i+1]: #notar que en este caso la condicion es contraria a lo que quiero, yo quiero que en el q estoy sea MENOR al q sigue
            return False #entonces si se cumple esa condicion falsa, corresponde devolver un falso de una
    return True

# recordar entonces que siempre que este trabajando con comparaciones directas entre elementos seguidos hay que tener en cuenta que el recorrido
# paso a paso actual debe ir hasta un numero en especifico y que los demas se pueden formar a partir de ese! En el caso de tener que recorrer toda
# la lista como en el caso de la funcion ordenados siempre se puede formar el ultimo a partir del anteultimo 

# si lista = [1,2,3,4], len = 4(no incluido, no existe), indices = 0,1,2,3
#                       len - 1 = 3(no incluido, pero si existe), indices = 0,1,2,3
#                                   (es como si fuera hasta 2)                    * el 3 se forma a partir del 2, cuando llega a i = 2 en el if
#                                                                                   2 + 1, incluyendo al 3 en la comparación
