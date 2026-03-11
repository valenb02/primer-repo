import math

def imprimir_verso():
    print("where the dogs do find her\ngot time, time to wait for tomorrow\nto find her, to find her")

def raizDe2():
    return round(math.sqrt(2), 4)

def factorialDeDos():
    return math.factorial(2)

def perimetro():
    return 2*math.pi

def imprimir_saludo_perso(nombre: str):
    print("Hola", nombre)

def raiz_cuadrada_de(num: float) -> float:
    return math.sqrt(num)

def fahrenheit_a_celsius(temp_far: float) -> float:
    return ((temp_far - 32) * 5) / 9 

def es_multiplo_de(n: int, m: int) -> bool:
    return (n % m == 0)

def es_par(numero: int) -> bool:
    return numero % 2 == 0
######################################
# como lo sacaria normalmente?
# hago 4x3 y como da 12 yo ya se intuitivamente que voy a necesitar dos pizzas porque cada pizza tiene 8 porciones y necesito aumentar 8
# y aumentar 1 pizza que necesito por cada vez que me pregunto si me alcanza. Me va a alcanzar cuando la cantidad de porciones acumuladas
# sean mayores que las q necesito

def cantidad_de_pizzas(comensales: int, min_cant_porc: int) -> int:
    cant_porc_necesito : int = comensales * min_cant_porc 
    cant_porc_q_tengo : int = 8
    cant_pizzas_necesarias : int = 1 
    while cant_porc_necesito > cant_porc_q_tengo: 
        cant_pizzas_necesarias += 1 
        cant_porc_q_tengo += 8
    return cant_pizzas_necesarias 

def es_bisiesto(año: int) -> bool:
    return es_multiplo_de(año, 400) or (es_multiplo_de(año,4) and not es_multiplo_de(año, 100))

def peso_pino(pino_en_m: int) -> int:
    if pino_en_m <= 3:
        return pino_en_m * 300
    else:
        return (pino_en_m - 3) * 200 + 3 * 300
    
#usando min y max:

def peso_pino2(pino_en_m: float) -> float:
    return min(pino_en_m, 3) * 300 + max(pino_en_m - 3, 0) * 200
################################################################
def es_peso_util(peso_en_kg: float) -> bool:
    return 400 <= peso_en_kg <= 1000

# 1 metro = 300kg (antes de los 3m)
# 1 metro = 200kg (dsp de los 3m)

def sirve_pino(pino_en_metros: float) -> bool:
    return 400 <= peso_pino(pino_en_metros) <= 1000


def es_par(num: int) -> bool:
    return num % 2 == 0

def devolver_doble_si_es_par(num: int) -> int:
    if es_par(num):
        return num * 2
    return num

def devolver_valor_si_es_par_sino_el_q_sigue(num: int) -> int:
    if es_par(num):
        return num
    return num + 1

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int) -> int:
    if numero % 9 == 0:
        return numero * 3
    elif numero % 3 == 0:
        return numero * 2
    else:
        return numero

def vacaciones_o_trabajar(sexo: str, edad: int) -> str:
    if edad < 18 or (sexo == 'F' and edad >= 60) or (sexo == 'M' and edad >= 65):
        print("Andá de vacaciones")
    else:
        print("Te toca trabajar")

    