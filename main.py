from expiracion import *
from nombres_comunes import *
import datetime
import cant_votantes
import apellido_particular
matriz = []
with open("PADRON_COMPLETO.txt", "r") as archivo:
    for linea in archivo:
        campos = linea.strip().split(",")
        matriz.append(campos)
op = str
while op!="0":
    
    print("Bienvenido al sistema del padrón electoral \nIngrese la acción que desea llevar a cabo: \na. Búsqueda de una persona a partir de sus datos \nb. Cantidad de votantes por provincia \nc. Cantidad de votantes por cantón \nd. Cantidad de votantes por distritos \ne. Los N cantones con más votantes registrados\nf. Los N distritos con más votantes registrados\ng. Cantidad de personas por tipo de identificación \nh. Personas cuya identificación expira en una fecha suministrada por el usuario \ni. Cantidad de personas con un nombre en particular\nj. Cantidad de personas con un apellido en particular\nk. Los N nombres más comunes \nl. Los N apellidos más comunes \nm. Los N nombres menos comunes \nn. Una ejecución completa de las consultas")
    op = input("Ingrese su seleccion: ")

    if op == "a":
        print ("x")
    elif op == "b":
        cant_votantes.seleccionarModo(matriz,0)
    elif op == "c":
        cant_votantes.seleccionarModo(matriz,3)
    elif op == "d":
        cant_votantes.seleccionarModo(matriz,4)
    elif op == "e":
        cant_votantes.seleccionarModo(matriz,2)
    elif op == "f":
        cant_votantes.seleccionarModo(matriz,1)
    elif op == "g":
        print ("x")
    elif op == "h":



        anio = input("Ingrese el año que desea buscar: ") 
        mes = input("Ingrese el mes que desea buscar: ")
        dia = input("Ingrese el día que desea buscar: ")
        op2 = input("Ingrese 1 si desea hacelo secuencial o 2 si desea hacerlo paralelo")
        fecha = anio + mes + dia
        inicio = datetime.datetime.now()
        if op2 == "1":
         mn = (buscar_persona(matriz,fecha))
         encontrar_terceros_datos(mn)
         final = datetime.datetime.now()
         tiempo = final-inicio
         print("El tiempo de ejecucion fue de: "+str(tiempo))
        elif op2 == "2":
            person = find_matching_data(matriz,fecha)
            final = datetime.datetime.now()
            print(get_third_data(person))
            tiempo = final-inicio
            print("El tiempo de ejecucion fue de: "+str(tiempo))








    elif op == "i":
        print ("x")
    elif op == "j":
        apellido_particular.seleccionarModo(matriz)
    elif op == "k":
        n = input("Ingrese la cantidad de nombres que desea ver: ")
        print("Los nombres más comunes y la cantidad de veces que aparecen son los siguientes:")
        op2 = input("Ingrese 1 si quiere que sea secuencial o 2 si quiere que sea paralelo: ")
        inicio = datetime.datetime.now()
        nombres = buscar_cuartos_campos(matriz)
        if op2 == "1":
            top = mas_comunes(nombres, n)
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
            final = datetime.datetime.now()
            primero = top[0][1]
            segundo = top[1][1]
            diferencia = primero-segundo
            print("Y la diferencia entre el primero y segundo es de: " + str(diferencia))
            tiempo = final-inicio
            print("El tiempo de ejecucion fue de: "+str(tiempo))
        elif op2 == "2":
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
            final = datetime.datetime.now()
            primero = top[0][1]
            segundo = top[1][1]
            diferencia = primero-segundo
            print("Y la diferencia entre el primero y segundo es de: " + str(diferencia))
            tiempo = final-inicio
            print("El tiempo de ejecucion fue de: "+str(tiempo))

    elif op == "l":
        print ("x")
    elif op == "m":
        n = input("Ingrese la cantidad de nombres que desea ver: ")
        op2 = input("Ingrese 1 si quiere que sea secuencial o 2 si quiere que sea paralelo: ")
        print("Los nombres menos comunes y la cantidad de veces que aparecen son los siguientes:")
        inicio = datetime.datetime.now()
        nombres = buscar_cuartos_campos(matriz)
        if op2 == "1":
            least = menos_comunes(nombres,n)
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
            final = datetime.datetime.now()
            primero = least[0][1]
            segundo = least[1][1]
            diferencia = primero-segundo
            print("Y la diferencia entre el primero y segundo es de: " +str(diferencia))
            tiempo = final-inicio
            print("El tiempo de ejecucion fue de: "+str(tiempo))
        elif op2 == "2":
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
            final = datetime.datetime.now()
            primero = least[0][1]
            segundo = least[1][1]
            diferencia = primero-segundo
            print("Y la diferencia entre el primero y segundo es de: " +str(diferencia))
            tiempo = final-inicio
            print("El tiempo de ejecucion fue de: "+str(tiempo))
    elif op == "n":
        print ("x")
    




