from typing import TextIO


def contar_lineas(nombre_archivo: str) -> int:
    archivo_abierto = open(nombre_archivo, "r")
    contador : int = 0
    leer_linea = archivo_abierto.readline()
    while leer_linea != "":
        contador += 1
        leer_linea = archivo_abierto.readline()
    archivo_abierto.close()
    return contador

def existe_palabra(nombre_archivo: str, palabra: str) -> bool:
    abrir_archivo : TextIO = open(nombre_archivo, 'r')
    linea : str = abrir_archivo.readline()
    formar_palabra : str = ""
    existe_la_palabra : bool = False
    while linea != "":
        for letra in linea:
            if letra != " " and letra != "\n":
                formar_palabra += letra
            else:
                if formar_palabra == palabra:
                    existe_la_palabra = True
                formar_palabra = ""
        linea = abrir_archivo.readline()
        if formar_palabra == palabra:
            existe_la_palabra = True
    abrir_archivo.close()
    return existe_la_palabra


def cantidad_de_apariciones(nombre_archivo: str, palabra: str) -> int:
    archivo_abierto : TextIO = open(nombre_archivo, 'r')
    leer_linea : str = archivo_abierto.readline()
    armar_palabra : str = ""
    contador : int = 0
    while leer_linea != "":
        for letra in leer_linea:
            if letra != " " and letra != "\n":
                armar_palabra += letra
            else:
                if armar_palabra == palabra:
                    contador += 1
                armar_palabra = ""
        if armar_palabra == palabra:
                    contador += 1
        leer_linea = archivo_abierto.readline()
    archivo_abierto.close()
    return contador

def agrupar_por_longitud(nombre_archivo: str) -> dict[int,int]:
    dicc_res : dict[int,int] = {}
    abrir_archivo : TextIO = open(nombre_archivo, 'r')
    leer_linea : str = abrir_archivo.readline()
    longitud_palabra : int = 0
    while leer_linea != "":
        for letra in leer_linea:
            if letra != " " and letra != "\n":
                longitud_palabra += 1
            else:
                if longitud_palabra > 0:
                    if longitud_palabra not in dicc_res:
                        dicc_res[longitud_palabra] = 1
                    else:
                        dicc_res[longitud_palabra] += 1
                    longitud_palabra = 0
        if longitud_palabra > 0:
            if longitud_palabra not in dicc_res:
                dicc_res[longitud_palabra] = 1
            else:
                dicc_res[longitud_palabra] += 1
            longitud_palabra = 0

        leer_linea = abrir_archivo.readline()
    abrir_archivo.close()
    return dicc_res

def agregar_frase_al_final(nombre_archivo: str, frase: str):
    archivo = open(nombre_archivo, "a")
    archivo.write(frase + "\n")
    archivo.close()

def agregar_frase_al_principio(nombre_archivo: str, frase: str):
    archivo : TextIO = open(nombre_archivo, "r")
    contenido : str = archivo.read()
    archivo.close()

    abrir_archivo : TextIO = open(nombre_archivo,"w")
    abrir_archivo.write(frase + "\n")
    abrir_archivo.write(contenido)
    abrir_archivo.close()
    