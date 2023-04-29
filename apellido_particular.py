import multiprocessing
from os import system
import threading
import time
# -*- coding: utf-8 -*-
provincias = {1:"San Jose",2:"Alajuela",3:"Cartago",4:"Heredia",5:"Guanacaste",6:"Puntarenas",7:"Limon",8:"Extranjeros"}

#Funcion que se encarga de seleccionar el modo de ejecucion del codigo 
def seleccionarModo(matriz):
    system("cls")
    print("1. Modo Secuencial\n2. Modo Multiprocesamiento\n3. Ambos\n4. Salir")
    select = int(input("Ingrese la opcion que desea:"))
    op,apellido,prov = select_opcion()
    if select == 4:
        return
    
    if (select == 1):
        metodo_secuencial(matriz,apellido,op,prov)
    elif (select == 2):
        
        metodo_multicore(matriz,apellido,op,prov)
    elif (select == 3):
        metodo_secuencial(matriz,apellido,op,prov)
        metodo_multicore(matriz,apellido,op,prov)

#Funcion que se encarga de seleccionar lo que se quiere buscar en la funcion 
def select_opcion():
    system("cls")
    print("Desea buscar el:\n1.Primer Apellido\n2.Segundo Apellido\n3.Ambos\n4.Ambos con nombre")
    try:
        select = int(input("==> "))
    except:
        print("Formato incorrecto")
        select_opcion()
    print("Ingrese el apellido o Apellidos que desea buscar: ")
    apellido = input("==> ").upper()
    print("Seleccione la provincia donde quiere realizar la busqueda: ")
    for a in provincias:
        print(str(a)+"-"+provincias[a])
    print("9-Todo el pais")
    try:

        prov = int(input("==> "))
    except:
        print("Formato incorrecto")
        select_opcion()
    return select,apellido,prov




#Metodo secuencial 
def metodo_secuencial(matriz,nombre,op,prov):
    print("Metodo secuencia")
    inicio = time.time()
    cont = 0

    for i in matriz:
        
        if ((str(prov) == i[0][0]) or (prov == 9)):
            
            if op == 1:
                apellido2 = str(i[6])
                apellido2 = apellido2.strip()
                if nombre == apellido2:
                    cont = cont+1
            elif op == 2:
                apellido2 = str(i[7])
                apellido2 = apellido2.strip()
                if nombre == apellido2:
                    cont = cont+1
            elif op == 3:
                apellido1 = str(i[6])
                apellido1 = apellido1.strip()
                apellido2 = str(i[7])
                apellido2 = apellido2.strip()
                apellidos = apellido1 +" "+apellido2
                if nombre == apellidos:
                    cont = cont+1
            elif op == 4:
                nombre_local = str(i[5])
                nombre_local = nombre_local.strip()
                apellido1 = str(i[6])
                apellido1 = apellido1.strip()
                apellido2 = str(i[7])
                apellido2 = apellido2.strip()
                nombre_completo = nombre_local + " "+apellido1 +" "+apellido2
                if nombre == nombre_completo:
                    cont = cont+1


    
    fin = time.time()
    system("cls")
    if prov == 9:
        print("Hay "+str(cont)+" personas con el apellido "+nombre+" en todo el pais")
    else:

        print("Hay "+str(cont)+" personas con el apellido "+nombre+" en la provincia de "+provincias[prov])
    print("El codigo duro: "+str(fin-inicio))

    input("Presione Enter para continuar...")








#Metodo multiprocesaminto utilizando hilos 
def metodo_multicore(matriz,nombre,op,prov):
    print("Metodo Multicore")
    inicio = time.time()
    cont = {}
    cont[nombre] = 0
    # número de hilos que se van a utilizar
    num_threads = 3
    def thread_function(section,apellido,op):
        
        for i in section:
            if ((str(prov) == i[0][0]) or (prov == 9)):

                if op == 1:
                    apellido2 = str(i[6])
                    apellido2 = apellido2.strip()
                    if apellido == apellido2:
                        cont[apellido] = cont[apellido]+1
                elif op == 2:
                    apellido2 = str(i[7])
                    apellido2 = apellido2.strip()
                    if apellido == apellido2:
                        cont[apellido] = cont[apellido]+1
                elif op == 3:
                    apellido1 = str(i[6])
                    apellido1 = apellido1.strip()
                    apellido2 = str(i[7])
                    apellido2 = apellido2.strip()
                    apellidos = apellido1 +" "+apellido2
                    if apellido == apellidos:
                        cont[apellido] =cont[apellido]+1
                elif op == 4:
                    nombre_local = str(i[5])
                    nombre_local = nombre_local.strip()
                    apellido1 = str(i[6])
                    apellido1 = apellido1.strip()
                    apellido2 = str(i[7])
                    apellido2 = apellido2.strip()
                    nombre_completo = nombre_local + " "+apellido1 +" "+apellido2
                    if nombre == nombre_completo:
                        cont[apellido] =cont[apellido]+1
        

    # dividir la matriz en secciones
    section_size = len(matriz) // num_threads
    sections = [matriz[i:i+section_size] for i in range(0, len(matriz), section_size)]

    # crear y ejecutar los hilos
    threads = []
    for section in sections:
        thread = threading.Thread(target=thread_function, args=(section,nombre,op))
        thread.start()
        threads.append(thread)

    # esperar a que los hilos terminen
    for thread in threads:
        thread.join()
        
    
    fin = time.time()
    if prov == 9:
        print("Hay "+str(cont[nombre])+" personas con el apellido "+nombre+" en todo el pais")
    else:

        print("Hay "+str(cont[nombre])+" personas con el apellido "+nombre+" en la provincia de "+provincias[prov])
    print("El codigo duro: "+str(fin-inicio))



