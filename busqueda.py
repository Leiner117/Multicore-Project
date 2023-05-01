import threading
import time

def seleccionarModo(matriz):
    
    print("1. Modo Secuencial\n2. Modo Multiprocesamiento\n3. Ambos\n4. Salir")
    select = int(input("Ingrese la opcion que desea:"))
    busqueda = select_busqueda()
    if select == 4:
        return
    
    if (select == 1):
        metodo_secuencial(matriz,busqueda)
    elif (select == 2):
        metodo_multicore(matriz, busqueda)
    elif (select == 3):
        metodo_secuencial(matriz,busqueda)
        metodo_multicore(matriz,busqueda)
    
def select_busqueda(): 
    print("De el dato de la persona que desea buscar")
    busqueda = input("==> ").upper()
    return busqueda

def metodo_secuencial(matriz,busqueda):
    print("Metodo secuencia")
    inicio = time.time()

    for i in matriz:
        for elemento in i:
            if busqueda.lower() in str(elemento).lower():
                print(i)
                break
    
    fin = time.time()
    print("El codigo duro: "+str(fin-inicio))

def metodo_multicore(matriz, busqueda):
    print("Metodo Multicore")
    inicio = time.time()
    # número de hilos que se van a utilizar
    num_threads = 4

    def thread_function(section,busqueda):
        for i in section:
            for elemento in i:
                if busqueda.lower() in str(elemento).lower():
                    print(i)
                    break
        
        

    # dividir la matriz en secciones
    section_size = len(matriz) // num_threads
    sections = [matriz[i:i+section_size] for i in range(0, len(matriz), section_size)]

    # crear y ejecutar los hilos
    threads = []
    for section in sections:
        thread = threading.Thread(target=thread_function, args=(section, busqueda))
        thread.start()
        threads.append(thread)

    # esperar a que los hilos terminen
    for thread in threads:
        thread.join()
        
    
    fin = time.time()
    print("El codigo duro: "+str(fin-inicio))