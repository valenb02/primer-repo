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

            