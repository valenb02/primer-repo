ingreso_mensual = 1000

# lo que yo quiero es que si tu ingreso es mayor o igual a 2000 entonces que diga que estas bien en cualquier parte del mundo,
# que si es mayor o igual a 1200 entonces diga que solo estas bien en argentina y que si es estrictamente menor entonces que sos
# pobre en cualquier parte del mundo. Basicamente que si tu sueldo está entre 1200 y 2000 estas bien en terminos argentinos;
# que si es mayor a 2000 entonces estas bien en cualquier lugar y si es menor a 1200 entonce sos pobre

# fijate que esto, en el caso en el que el ingreso mensual sea mayor o igual a 2000 va a salir del bucle y va a ejecutar
# tanto el segundo if como el else, pero en realidad eso no hace falta porque las proposiciones que yo hago en el codigo
# son disjuntas y podemos aprovechar mejor el espacio con un if elif else y poniendo en otro orden las cosas que propongo, teniendo
# en cuenta que python se queda con la primer info que guardó si esta es verdadera, y el elif indica que algo es exclusivo si es que
# se llega ahi habiendo ya un True antes  y termina la ejecucion

'''if ingreso_mensual >= 2000:
    print("estás bien económicamente en cualquier parte del mundo")
if 1200 <= ingreso_mensual < 2000:
    print("estas bien en argentina")
else:
    print("sos pobre")''' # el else está separado al segundo if y es exclusivo solo para él; en cambio para el primero
                          # siempre está funcionando, digamos siempre desemboca al else por mas de que la condicion sea false

'''if ingreso_mensual >= 2000:
    print("estás bien económicamente en todo el mundo")
elif ingreso_mensual >= 1200:
    print("estás bien económicamente solo en arg")
else:
    print("sos pobre")'''


# esta funcion tiene rangos bien definidos entonces no ocurren problemas con los switches entre los elif 

edad = 23

if edad >= 60:
    print("estás en adultez tardía")
elif 30 <= edad < 60:
    print("estás en la adultez media")
elif 18 <= edad < 30:
    print("sos adulto jóven")
else:
    print("sos menor de edad")

# esta funcion no tiene rangos bien definidos entonces vamos a poner los elif de manera que, teniendo en cuenta que se van
# a ejecutar todos (sin necesidad de ENTRAR al bucle) termine por ejecutarse el primero que cumpla la condicion. Esta funcion
# aprovecha la manera en la que python ejecuta por orden y sigue buscando en el codigo hasta encontrar algo que sea True.
# En esta funcion los casos son disjuntos y se va a ejecutar sólo exclusivamente aquel que cumpla lo que queremos.

# Esta versión es preferible porque no hay solapamientos complejos! los rangos de la otra son redundantes.

if edad >= 60:
    print("adultez tardía")
elif edad >= 30:
    print("adultez media")
elif edad >= 18:
    print("adultez joven")
else:
    print("menor de edad")


# EJEMPLO DEL INGRESO MENSUAL (con complejidades):

ingreso_mensual = 1000
gastos_mensuales = 1

# para la clase alta: 1000
# para la clase media: 400
# para la clase baja: else

if ingreso_mensual >= 2000:
    if ingreso_mensual - gastos_mensuales > 1000:
        print("estás manejando bien tu dinero")
    else:
        print("vas a tener que manejar mejor tu dinero")
elif ingreso_mensual >= 1200:
    if ingreso_mensual - gastos_mensuales > 400:
        print("estás manejando bien tu dinero")
    else:
        print("vas a tener que controlar mejor tus gastos")
else:
    print("estás por debajo del índice de pobreza")

# quedamos en que una buena practica para mi es, en vez de pensarlo de una como una funcion de una, porque se me complica separar los parametros
# y darme cuenta de qué hacer con ellos, primero pensarlos como algo separado, tipo crear los parametros como variables y fijarme dentro
# de qué los pondria.

'''def cantidad_de_pizzas(comensales: int, min_cant_porc: int) -> int:
    cant_porc_necesarias : int = comensales * min_cant_porc
    porciones : int = 8
    pizzas_necesarias : int = 1
    while porciones <= cant_porc_necesarias:
        pizzas_necesarias += 1
        porciones += 8
    return pizzas_necesarias'''

# ESTE DE ARRIBA LO HICE PARA VER SI OTRO DIA DISTINTO ME ACORDABA DE COMO SE RESOLVIA

###########################################################################################

# ¿Me acuerdo de como hacer pos seq ordenada mas larga?
# Hay que hacer una funcion que a la cual vos le metas una lista y te devuelva el indice del elemento en el cual comienza la secuencia ordenada + larga
# por ejemplo : [4,3,1,2,3,1] = 2
#               [1,2,1,2,3] = 2
#               [5,2,1,2,1,2,3] = 4

def pos_seq_mas_larga2(lista: list[int]) -> int:
    long_mayor : int = 1
    long_actual : int = 1
    inicio_actual : int = 0
    inicio_pos_seq_mas_larga : int = 0
    for i in range(1,len(lista)):
        if lista[i] < lista[i - 1]:
            long_actual += 1
        else:
            if long_actual < long_mayor:
                long_mayor = long_actual
                inicio_pos_seq_mas_larga = inicio_actual
            long_actual = 1
            inicio_actual = i # la onda de este guardado no es para que el proximo inicio sea desde ahi porque de eso ya se encarga el for
                              # sino que es para tener recordado, para la proxima vuelta, CUÁNDO es que se rompió la seq anterior, porque 
                              # en ese momento es cuando inicia la proxima, que si pasa el filtro de que la longitud es mayor a la que estaba
                              # guardada antes entonces podre actualizar la mas larga a la actual, que inicia exactamente en "i"
    if long_actual < long_mayor:
        long_mayor = long_actual
        inicio_pos_seq_mas_larga = inicio_actual
    return inicio_pos_seq_mas_larga
            
# o sea sí, me guardo el indice "i" ni bien arranco la secuencia, antes de fijarme si es mas larga o no que la anterior, digamos la guardo en todos
# los casos, y si luego de haberse roto el orden de la secuencia quedamos en que la longitud es mas larga que la actual puedo elegir en ese caso
# guardarme el indice en donde inicio esa secuen (que es el indice actual donde estamos llevando la cuenta de la mas larga) como el inicio de la mas
# larga, e utilizar inicio actual para el inicio de la proxima, independientemente de si esa sera la mas larga o no 

