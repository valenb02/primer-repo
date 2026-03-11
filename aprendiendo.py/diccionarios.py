from queue import LifoQueue as Pila

def calcular_promedio_por_estudiante(notas: list[tuple[str,float]]) -> dict[str, float]:
    dicc_res : dict[str,tuple[float,int]] = {}
    for i in range(len(notas)):
        if notas[i][0] not in dicc_res:
            dicc_res[notas[i][0]] = (notas[i][1], 1)
        else:
            suma_notas, cant = dicc_res[notas[i][0]] 
            suma_notas += notas[i][1]
            cant += 1
            dicc_res[notas[i][0]] = (suma_notas, cant)
    for clave in dicc_res:
        suma_notas, cant = dicc_res[clave]
        dicc_res[clave] = suma_notas / cant
    return dicc_res

#notas = [("valen", 0.4), ("elias", 3), ("caro", 2), ("valen", 5), ("caro", 6), ("elias", 10)]
#print(calcular_promedio_por_estudiante(notas))

def calc_prom_por_estudiante2(lista_notas: list[tuple[str,float]]) -> dict[str,float]:
    diccio : dict[str,float] = {}
    suma_notas : float = 0
    cant_notas : int = 0
    for i in range(len(lista_notas)):
        diccio[lista_notas[i][0]] = 0
    for nombre in diccio:
        for j in range(len(lista_notas)):
            if nombre == lista_notas[j][0]:
                suma_notas += lista_notas[j][1]
                cant_notas += 1
        diccio[nombre] = suma_notas / cant_notas
        suma_notas = 0
        cant_notas = 0
    return diccio
##############################################################


pila : Pila[str] = Pila()
pila.put("twitter")
pila.put("instagram")
pila.put("gmail")

pila_2 : Pila[str] = Pila()
pila_2.put("facebook")
pila_2.put("instagram")
pila_2.put("banco galicia")


historiales : dict[str,Pila[str]] = {"valen": pila, "caro": pila_2}

def visitar_sitio(historiales: dict[str,Pila[str]], usuario: str, sitio: str):
    if usuario in historiales:
        historiales[usuario].put(sitio)
    else:
        nueva_pila = Pila()
        nueva_pila.put(sitio)
        historiales[usuario] = nueva_pila

# Seguir mañana con diccionarios :) intentar rehacer el de historiales, hacer los que quedan + el de examen que era el q te daban dos diccionarios
# como censos attacheados a una clave que era el nombre o algo así; lo podes buscar
            
def calcular_prom_x_estudiante(notas: list[tuple[str,float]]) -> dict[str,float]:
    diccionario : dict[str,float] = {}
    suma_notas : float = 0
    cant_notas : int = 0
    for tupla in notas:
        if tupla[0] not in diccionario:
            diccionario[tupla[0]] = 0
    for nombre in diccionario:
        for nota in notas:
            if nota[0] == nombre:
                suma_notas += nota[1]
                cant_notas += 1
        diccionario[nombre] = suma_notas / cant_notas
        suma_notas = 0
        cant_notas = 0
    return diccionario

# la rehice para recordar; esta vez puedo notar que puedo acceder a los diccionarios de una mediante los nombres y lo mas normal es actualizar 
# la variable a valores nuevos, en el caso de esta versión de arriba es el 0 al promedio, y en la otra es la tupla de suma y cantidad al promedio
# que se saca a partir de esas variables

