from os import system
import threading
import time


def seleccionarModo(matriz):
    system("cls")
    print("1. Modo Secuencial\n2. Modo Multiprocesamiento\n3. Ambos\n4. Salir")
    select = int(input("Ingrese la opcion que desea:"))
    if select == 4:
        return
    
    if (select == 1):
        metodo_secuencial(matriz)
    elif (select == 2):
        metodo_multicore(matriz)
    elif (select == 3):
        metodo_secuencial(matriz)
        metodo_multicore(matriz)


def imprimir(dic):
    for i in dic:
        print("Tipo "+str(i)+":"+str(dic[i]))

def metodo_secuencial(matriz):
    print("Metodo secuencia")
    inicio = time.time()
    cedulas = {1:0,2:0,3:0}
    for i in matriz:
        if int(i[0][0]) in range(1,7):
            cedulas[1] = cedulas[1]+1
        elif int(i[0][0]) == 8:
            cedulas[2] = cedulas[2]+1
        elif int(i[0][0]) == 9:
            cedulas[3] = cedulas[3]+1
    fin = time.time()
    system("cls")
    imprimir(cedulas)
    print("El codigo duro: "+str(fin-inicio))
    input("Presione Enter para continuar...")

    


def metodo_multicore(matriz):
    print("Metodo Multicore")
    inicio = time.time()
    cedulas = {1:0,2:0,3:0}
    # número de hilos que se van a utilizar
    num_threads = 4
    def thread_function(section):
        for i in section:
            if int(i[0][0]) in range(1,7):
                cedulas[1] = cedulas[1]+1
            elif int(i[0][0]) == 8:
                cedulas[2] = cedulas[2]+1
            elif int(i[0][0]) == 9:
                cedulas[3] = cedulas[3]+1
        

    # dividir la matriz en secciones
    section_size = len(matriz) // num_threads
    sections = [matriz[i:i+section_size] for i in range(0, len(matriz), section_size)]

    # crear y ejecutar los hilos
    threads = []
    for section in sections:
        thread = threading.Thread(target=thread_function, args=(section,))
        thread.start()
        threads.append(thread)

    # esperar a que los hilos terminen
    for thread in threads:
        thread.join()
        
    imprimir(cedulas)
    fin = time.time()
    print("El codigo duro: "+str(fin-inicio))
    input("Presione Enter para continuar...")
