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
#####################################
from typing import TextIO

def parsear_linea(linea: str) -> list[str]:
    campos = []
    actual = ""
    for c in linea:
        if c == ",":
            campos.append(actual)
            actual = ""
        elif c != "\n":
            actual += c
    campos.append(actual)
    return campos


def diccionario_lu_y_notas(diccionario: dict[str, list], linea_convertida_a_lista: list):
    LU: str = linea_convertida_a_lista[0]
    nota: float = float(linea_convertida_a_lista[3])

    if LU not in diccionario:
        diccionario[LU] = [nota]
    else:
        diccionario[LU].append(nota)


def promedio_estudiante(LU: str, diccio: dict[str, list]) -> float:
    suma: float = 0
    cant_notas: int = 0

    for nota in diccio[LU]:
        suma += nota
        cant_notas += 1

    return suma / cant_notas

def calcular_promedio_por_estudiante(nombre_archivo_notas: str, nombre_archivo_promedios: str):
    abrir_archivo_notas: TextIO = open(nombre_archivo_notas, "r")
    diccionario: dict[str, list] = {}
    leer_linea: str = abrir_archivo_notas.readline()
    while leer_linea != "":
        convertir_str_a_lista: list[str] = parsear_linea(leer_linea)
        diccionario_lu_y_notas(diccionario, convertir_str_a_lista)
        leer_linea = abrir_archivo_notas.readline()
    abrir_archivo_promedios: TextIO = open(nombre_archivo_promedios, "w")
    for LU in diccionario:
        prom = promedio_estudiante(LU, diccionario)
        abrir_archivo_promedios.write(LU + "," + str(prom) + "\n")

    abrir_archivo_notas.close()
    abrir_archivo_promedios.close()

    