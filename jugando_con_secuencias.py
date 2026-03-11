def pertenece(lista: list[int], e: int) -> bool:
    for i in range(len(lista)):
        if lista[i] == e:
            return True
    return False

def pertenece2(lista: list[int], e: int) -> bool:
    i : int = 0
    while i < len(lista):
        if lista[i] != e:
            return True
        i += 1
    return False

def pertenece3(lista: list[int], elem: int) -> bool:
    encontrado : bool = False
    for i in range(len(lista)):
        if lista[i] == elem:
            encontrado = True
    return encontrado

def divide_a_todos(s: list[int], elem: int) -> bool:
    for i in range(len(s)):
        if s[i] % elem != 0:
            return False
    return True

def suma_total(s: list[int]) -> int:
    res : int = 0
    for i in range(len(s)):
        res += s[i]
    return res

# [4,3,5,2,1]
def maximo(s: list[int]) -> int:
    res : int = s[0]
    for i in range(1,len(s)):
        if s[i] > res:
            res = s[i]
    return res

def minimo(s: list[int]) -> int:
    res: int = s[0]
    for i in range(1, len(s)):
        if s[i] <= res:
            res = s[i]
    return res

def ordenados(s: list[int]) -> bool:
    for i in range(len(s) - 1):
        if s[i]  >= s[i + 1]:  # la condicion es negativa a lo que queremos
            return False    # asi, el return es falso tambien, porque en ese caso falso devuelve falso
    return True

def ordenados2(s:list[int]) -> bool:
    for i in range(1,len(s)):
        if s[i-1] >= s[i]:
            return False
    return True

# la onda aca es que cuando buscamos minimos o maximos de una lista (o en general algo que sea "el mas" o "el menos" de una lista), conviene asumir
# que el primero es el mas o el menos y dejarlo guardado en una variable, luego recorrer la lista de manera que este comparando el actual
# siempre con el que me quedó guardado como "el que más" o "el que menos", la lista a partir de allí se recorrera sola dentro de la comparacipon
# porque el bucle "for" ya hará el trabajo de ir uno a uno. En el primer de los casos el posicion uno guardada en res
# queda representada por el i - 1 y si se encuentra uno "mas" o "menos" que ese segun lo que se necesite, entonces se guarda, el proceso se repite
# hasta el final y el que quede guardado es la respuesta que estoy buscando

def pos_maximo(s: list[int]) -> int:
    if len(s) == 0:
        return -1
    else:
        res : int = 0
        for i in range(1,len(s)):
            if s[i] >= s[res]:
                res = i
        return res

def pos_minimo(s: list[int]) -> int:
    if len(s) == 0:
        return -1
    else:
        res : int = s[0]
        for i in range(1, len(s)):
            if s[i] <= s[res]:
                res = i 
    return res

def long_mayorASiete(lista_palabras: list[str]) -> bool:
    for palabra in lista_palabras:
        if len(palabra) > 7:
            return True
    return False

# valen

def es_palindroma(palabra: str) -> bool:
    for i in range(len(palabra) // 2):
        if palabra[i] != palabra[len(palabra) - i - 1]:
            return False
    return True

# si accedo hasta i + k entonces el rango deberia ser range(len - k)
def iguales_consecutivos(s: list[int]) -> bool:
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] == s[i + 2]:
            return True
    return False

def vocales_distintas(palabra: str) -> bool:
    vocales : list[str] = ['a','e','i','o','u','A','E','I','O','U']
    num_vocales_encontradas : int = 0
    vocales_encontradas : str = ""
    for letra in palabra:
        if pertenece(vocales, letra) and not pertenece(vocales_encontradas, letra):
            num_vocales_encontradas += 1
            vocales_encontradas += letra
    if num_vocales_encontradas >= 3:
        return True
    return False

def vocales_distintas2(palabra: str) -> bool:
    vocales = "aeiou"
    encontradas = ""
    
    for letra in palabra.lower():
        if letra in vocales and letra not in encontradas: # o bien pertenece..
            encontradas += letra
    
    return len(encontradas) >= 3


# intentar volver a hacerla para que me quede claro que lo que estoy haciendo es utilizar "guardar algo" que primero asumo como que es la respuesta
# correcta y con el reemplazo y el guardado de lo anterior cuando veo que se rompe algo es que funciona para todo lo que sigue
def pos_seq_ord_mas_larga(lista: list[int]) -> int:
    longi_actual = 1
    indice_actual = 0
    longi_mayor_hasta_ahora = 1
    indice_mayor_hasta_ahora = 0
    for i in range(1, len(lista)):
        if lista[i] > lista[i-1]:
            longi_actual += 1    
        else:
            if longi_actual > longi_mayor_hasta_ahora:
                longi_mayor_hasta_ahora = longi_actual
                indice_mayor_hasta_ahora = indice_actual
            indice_actual = i  
            longi_actual = 1
    if longi_actual > longi_mayor_hasta_ahora:
        indice_mayor_hasta_ahora = indice_actual
        longi_mayor_hasta_ahora = longi_actual
    return indice_mayor_hasta_ahora

#                sigo..
#             longi actual: 1
#             if lista[2] < lista[3]:
#                sigo..
#             longi actual: 2
#               no es... 
#             longi mas larga hasta ahora = 2 (la actual)
#             longi actual = 1 
#             toca guardar el indice para que sea donde inicia la secuencia mas larga
#             indice donde inicia la secu mas larga: 1 Lo guardamos automaticamente en el momento en el que se rompe la condicion de 
#               el q estoy es mas grande q el q le sigue.
# arranco la comparacion de vuelta pero desde lista[3], comparando lista[3] con el q le sigue
#             if lista[3] < lista[4]:
#                sigo
#             if lista[4] < lista[5]
#                sigo
#             if lista[5] < lista[6]
#                sigo 
#             if lista[6] < lista[7]
#                 no es..
#             toca guardar el indice para que ahora sea donde inicia la secuencia mas larga SI ES QUE la longitud de esta seq es mas grande
#             que la longitud de la anterior secuencia guardada. Si pasa este filtro entonces:
#             longi mas larga hasta ahora: 4 (la actual)
#             longi actual = 1
#             toca guardar el indice para q sea donde inicia la secu mas larga(7)

# [57,2383,812,246] = 5

def cant_dig_impares(s: list[int]) -> int:
    contador_de_impares : int = 0
    for i in range(len(s)):
        num_convertido_a_str : str = str(s[i])
        for j in range(len(num_convertido_a_str)):
            if int(num_convertido_a_str[j]) % 2 != 0:
                contador_de_impares += 1
    return contador_de_impares

# mas simple usando for directos:

def cant_dig_impares2(s: list[int]) -> int:
    contador : int = 0
    for numero in s:   # los numeros no son iterables!
        for digito in str(numero): # esto si se puede porque los strings si son iterables, el for nada mas indica que se debe ir elemento a elemento
                                   # en lo que se le pase, y se puede utilizar siempre y cuando lo que se le pase sea iterable. Conviene usar for
                                   # in range cuando es necesario hacer referencia a algun tipo de indice porque hay que comparar entre cosas
                                   # de la lista y el for cuando solo hay que ir uno a uno hasta que termine y nada más.
            if int(digito) % 2 != 0:
                contador += 1
    return contador

# [131,25,6,1] = 

def cant_dig_impares3(lista: list[int]) -> int:
    contador_impares : int = 0
    for numero in lista:
        for digito in str(numero):
            if int(digito) % 2 != 0:
                contador_impares += 1
            digito = int(digito) // 10
    return contador_impares
#######################################################################################################################
def cerosEnPosPares(s: list[int]):
    for i in range(len(s)):
        if i % 2 == 0:
            s[i] = 0
# por qué no me pide un else?? digamos por que continua si yo no le dije q hacer en el caso en el q la pos no sea par?
# porque en python el else no es necesario, es opcional, cuando la condicion es falsa python simplemente saltea el bloque del if y sigue
# normal con la iteracion del for;, nada mas se necesita el else si es que necesitamos que haga otra cosa en caso contrario

################################
def cerosEnPosPares2(s:list[int]) -> list[int]:
    lista_res : list[int] = []
    for i in range(len(s)):
        if i % 2 != 0:
            lista_res.append(s[i])
        else:
            lista_res.append(0)
    return lista_res

def cerosEnPosPares3(s: list[int]) -> list[int]:
    lista_aux : list[int] = s.copy()
    for i in range(len(s)):
        if i % 2 == 0:
            lista_aux[i] = 0
    return lista_aux
