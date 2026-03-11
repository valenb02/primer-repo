nombre = "valen"
edad = 23
saludo = "Hola " + nombre + f" tenes {edad} años"

""" la moraleja viene siendo q la f con la llavecita adentro te permite convertir la variable q quieras del tipo q sea a texto! y de esa manera es concatenable"""


""" puedo modificar perfectamente una lista despues de haberla definido, por ejemplo si yo enliste el nombre de una persona con su nombre edad y ciudad, y de repente
la persona cambia de edad y ahora tiene 24, entonces puedo modificar lista[1] por 24 y al imprimir la lista ahora en ese lugar dirá 24; en cambio, con la tupla
no está permitida esta funcionalidad"""

lista = ["Valen", 23, "Necochea"]
tupla = ("Valen", 23, "neco")

lista[1] = 24

print(tupla)
print(lista)


# fijate que la idea es la misma que la de las listas, se puede acceder siempre a todos los elementos mediante indices pero en lugar de acceder mediante numeros 
# lo hacemos mediante la clave directa, así, si quiero saber la edad de mamá, en lugar de poner dicc[1], yo, sabiendo que mamá es una clave pregunto directo por la edad
# de mamá con dicc[mama]

diccionario = {'valen' : 23,
                'mama' : 56,
                'maxi' : 35
}

print(diccionario['mama'])











