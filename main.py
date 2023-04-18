from expiracion import *
from nombres_comunes import *

matriz = []
with open("PADRON_COMPLETO.txt", "r") as archivo:
    for linea in archivo:
        campos = linea.strip().split(",")
        matriz.append(campos)

print("Bienvenido al sistema del padrón electoral \nIngrese la acción que desea llevar a cabo: \na. Búsqueda de una persona a partir de sus datos \nb. Cantidad de votantes por provincia \nc. Cantidad de votantes por cantón \nd. Cantidad de votantes por distritos \ne. Los N cantones con más votantes registrados\nf. Los N distritos con más votantes registrados\ng. Cantidad de personas por tipo de identificación \nh. Personas cuya identificación expira en una fecha suministrada por el usuario \ni. Cantidad de personas con un nombre en particular\nj. Cantidad de personas con un apellido en particular\nk. Los N nombres más comunes \nl. Los N apellidos más comunes \nm. Los N nombres menos comunes \nn. Una ejecución completa de las consultas")

op = input("Ingrese su seleccion: ")

if op == "a":
    print ("x")
elif op == "b":
    print ("x")   
elif op == "c":
    print ("x")
elif op == "d":
    print ("x")
elif op == "e":
    print ("x")
elif op == "f":
    print ("x")
elif op == "g":
    print ("x")
elif op == "h":
    anio = input("Ingrese el año que desea buscar: ") 
    mes = input("Ingrese el mes que desea buscar: ")
    dia = input("Ingrese el día que desea buscar: ")
    fecha = anio + mes + dia
    person = find_matching_data(matriz,fecha)
    print(get_third_data(person))
elif op == "i":
    print ("x")
elif op == "j":
    print ("x")
elif op == "k":
    n = input("Ingrese la cantidad de nombres que desea ver: ")
    print("Los nombres más comunes y la cantidad de veces que aparecen son los siguientes:")
    nombres = get_name_data(matriz)
    top = find_top_x(nombres, n)
    bool = False
    for i in range(len(top)):
        for j in range(len(top[0])):
            print(top[i][j], end=" ")
            if bool == True:
                print() 
            if bool == True:
                bool = False
            elif bool == False:
                bool = True


    primero = top[0][1]
    segundo = top[1][1]
    diferencia = primero-segundo
    print("Y la diferencia entre el primero y segundo es de: " + str(diferencia))

elif op == "l":
    print ("x")
elif op == "m":
    n = input("Ingrese la cantidad de nombres que desea ver: ")
    print("Los nombres menos comunes y la cantidad de veces que aparecen son los siguientes:")
    nombres = get_name_data(matriz)
    least = find_least_x(nombres, n)
    bool = False
    for i in range(len(least)):
        for j in range(len(least[0])):
            print(least[i][j], end=" ")
            if bool == True:
                print() 
            if bool == True:
                bool = False
            elif bool == False:
                bool = True


    primero = least[0][1]
    segundo = least[1][1]
    diferencia = primero-segundo
    print("Y la diferencia entre el primero y segundo es de: " +str(diferencia))
elif op == "n":
    print ("x")





