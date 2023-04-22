import multiprocessing
import threading
import time

#Seleccionar el modo de ejecucion del programa
def seleccionarModo(matriz):
    print("1. Modo Secuencial\n2. Modo Multiprocesamiento\n3. Ambos\n4. Salir")
    select = int(input("Ingrese la opcion que desea:"))
    if (select == 1):
        metodo_secuencial(matriz)
    elif (select == 2):
        metodo_multicore(matriz)
    elif (select == 3):
        metodo_secuencial(matriz)
        metodo_multicore(matriz)
    
#Funcion que se encarga de imprimir la cantidad de Distritos que se desea
def imprimir(distritosLista):
    i = 0
    sorted_dict = dict(sorted(distritosLista.items(), key=lambda x: x[1], reverse=True))
    '''try:
            
        cantidad = int(input("Ingrese la cantidad de Distritos que quiere imprimir: "))
    except:
        print("Formato Incorecto!")'''
    for a in sorted_dict:
        print(str(a)+":"+str(sorted_dict[a]))
        i = i+1
        if (i == 3):
            break

#Metodo secuncial:
#Se recorre la matriz
#Se verifica si el distrito se encuentra en el diccionario
#Si se encuentra se suma 1 al valor del distrito
#Sino se agrega en el diccionario
def metodo_secuencial(matriz):
    print("Metodo secuencia")
    inicio = time.time()
    distritosLista = {}
    for x in matriz:
        if (x[1]) not in distritosLista:

            distritosLista[x[1]] = 1
        else:
            distritosLista[x[1]] = distritosLista[x[1]] +1
    imprimir(distritosLista)
    fin = time.time()
    print("El codigo duro: "+str(fin-inicio))
#Metodo multicore
#Crea hilos que se encargan de ejecutar la funcion al mismo tiempo
def metodo_multicore(matriz):
    print("Metodo Multicore")
    inicio = time.time()
    distritosLista = {}
    dic = {}

   
    
    # número de hilos que se van a utilizar
    num_threads = 4

    # función que cada hilo ejecutará
    def thread_function(section):
        for x in section:
            if (x[1]) not in distritosLista:

                distritosLista[x[1]] = 1
            else:
                distritosLista[x[1]] = distritosLista[x[1]] +1

        

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
        

    
    
    imprimir(distritosLista)
    fin = time.time()
    print("El codigo duro: "+str(fin-inicio))



    
        
