# de hecho conviene hacerlo al reves; siempre que sean distintas la que estoy con las adyacentes conviene seguir recorriendo. Si ese no es el caso;
# entonces entra en un else que te incita a fijarte si son iguales tres en linea

import random

tablero = [['X','O','O'],
           ['X',' ',' '],
           ['X',' ',' ']]


def quien_gana_tateti(tablero: list[list[str]]) -> int:
    for i in range(len(tablero)):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != ' ':
            if tablero[i][0] == 'O':
                return 0
            else:
                return 1
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != ' ':
            if tablero[0][i] == 'O':
                return 0
            else:
                return 1
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
        if tablero[0][0] == 'O':
            return 0
        else:
            return 1
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
        if tablero[0][2] == 'O':
            return 0
        else:
            return 1
    return 2
##############################################################

def lista_estudiantes() -> list[str]:
    lista_res : list[str] = []
    nombre_estudiante : str = input("Ingrese nombre del estudiante: ")
    while nombre_estudiante != "listo" and nombre_estudiante != '':
        lista_res.append(nombre_estudiante)
        nombre_estudiante = input("Ingrese nombre del estudiante: ")
    return lista_res

def sube() -> list[tuple[str, int]]:
    historial : list[tuple[str,int]] = []
    saldo : int = 0
    seleccionar_accion : str = input("Ingrese C para cargar, D para descontar y X para finalizar: ")
    while seleccionar_accion != "X":
        if seleccionar_accion == "C":
            saldo_a_cargar : str = input("Ingrese el saldo a cargar: ")
            saldo += int(saldo_a_cargar)
            historial.append(("C", int(saldo_a_cargar)))
        elif seleccionar_accion == "D":
            saldo_a_cargar = input("Ingrese el saldo a descontar: ")
            saldo -= int(saldo_a_cargar)
            historial.append(("D", int(saldo_a_cargar))) 
        seleccionar_accion = input("Ingrese C para cargar, D para descontar y X para finalizar: ")
    print("El programa ha finalizado")
    print(saldo)
    return historial
#####################################

def siete_y_medio() -> list[int]:
    historial : list[int] = []
    acumular_valores : float = 0
    repartir_cartas : int = random.choice([1,2,3,4,5,6,7,10,11,12])
    historial.append(repartir_cartas)
    if repartir_cartas == 10 or repartir_cartas == 11 or repartir_cartas == 12:
        acumular_valores += 0.5
    else:
        acumular_valores += repartir_cartas
    sacar_o_plantarse : str = input("Seguis sacando o te plantas?: ")
    while sacar_o_plantarse == "sacar":
        repartir_cartas = random.choice([1,2,3,4,5,6,7,10,11,12])
        historial.append(repartir_cartas)
        if repartir_cartas == 10 or repartir_cartas == 11 or repartir_cartas == 12:
            acumular_valores += 0.5
        else:
            acumular_valores += repartir_cartas
        sacar_o_plantarse : str = input("Seguis sacando o te plantas?: ")
    if acumular_valores > 7.5:
        print("Perdiste!")
    else:
        print("Ganaste!")
    return historial

