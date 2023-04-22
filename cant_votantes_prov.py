import threading
import time

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

def imprimir(provinciaLista):
    provincias = {1:"San Jose",2:"Alajuela",3:"Cartago",4:"Heredia",5:"Guanacaste",6:"Puntarenas",7:"Limon",8:"Extranjeros"}
    
    sorted_dict = dict(sorted(provinciaLista.items(), key=lambda x: x[1], reverse=True))

    '''try:
            
        cantidad = int(input("Ingrese la cantidad de Distritos que quiere imprimir: "))
    except:
        print("Formato Incorecto!")'''
    for a in sorted_dict:
        print(provincias[int(a)]+":"+str(sorted_dict[a]))
        
        
def metodo_secuencial(matriz):
    print("Metodo secuencia")
    inicio = time.time()
    provinciaLista = {}
    
    for x in matriz:
        provincia = x[1][0]
        if (provincia) not in provinciaLista:

            provinciaLista[provincia] = 1
        else:
            provinciaLista[provincia] = provinciaLista[provincia] +1
    imprimir(provinciaLista)
    fin = time.time()
    
    print("El codigo duro: "+str(fin-inicio))

def metodo_multicore(matriz):
    print("Metodo Multicore")
    inicio = time.time()
    provinciaLista = {}
    # número de hilos que se van a utilizar
    num_threads = 4
    def thread_function(section):
        
        for x in section:
            provincia = x[1][0]
            if (provincia) not in provinciaLista:

                provinciaLista[provincia] = 1
            else:
                provinciaLista[provincia] = provinciaLista[provincia] +1
        

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
        
    imprimir(provinciaLista)
    fin = time.time()
    print("El codigo duro: "+str(fin-inicio))