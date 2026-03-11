def uno_al_diez():
    v: int = 1
    while v < 11:
        print(v)
        v += 1

def entre_diez_y_cuarenta():
    v: int = 10
    while v <= 40:
        print(v)
        v += 2

def eco():
    v: int = 1
    while v < 11:
        print('eco')
        v += 1

def cuenta_regresiva(num: int):
    v : int = num
    while v > 0:
        print(v)
        v -= 1
    print("Despegue!")

def viaje_en_el_tiempo(partida: int, llegada: int):
    p: int = partida
    while p > llegada:
        p -= 1
        print("Viajó un año al pasado, estamos en el año ", p)

def viaje_en_el_tiempo2(partida: int):
    p : int = partida
    while p - 20 >= -384:
        p -= 20
        print("Viajó 20 años al pasado, hola aristóteles! está en el año ", p)

