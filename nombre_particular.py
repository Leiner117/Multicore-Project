from os import system
import threading
import time


def seleccionarModo(matriz):
    system("cls")
    print("1. Modo Secuencial\n2. Modo Multiprocesamiento\n3. Ambos\n4. Salir")
    select = int(input("Ingrese la opcion que desea:"))
    nombre = select_nombre()
    if select == 4:
        return
    
    if (select == 1):
        metodo_secuencial(matriz,nombre)
    elif (select == 2):
        metodo_multicore(matriz,nombre)
    elif (select == 3):
        metodo_secuencial(matriz,nombre)
        metodo_multicore(matriz,nombre)
def select_nombre():
    system("cls")
    print("Ingrese el Nombre que desea buscar(Solo de uno): ")
    nombre = input("==> ").upper()
    return nombre




        
        

def metodo_secuencial(matriz,nombre):
    print("Metodo secuencia")
    inicio = time.time()
    cont = 0
  
    for i in matriz:
        nombres2 = str(i[5])
        nombres2 = nombres2.split()
        primer_nombre = nombres2[0]
        if nombre == primer_nombre:
            cont = cont+1
        if len(nombres2) == 2:
            segundo_nombre = nombres2[1]
        
            if nombre == segundo_nombre:
                cont = cont+1
    
    fin = time.time()
    print("Hay "+str(cont)+" personas con el nombre "+nombre)
    print("El codigo duro: "+str(fin-inicio))
    input("Presione Enter para continuar...")
def metodo_multicore(matriz,nombre):
    print("Metodo Multicore")
    inicio = time.time()
    cont = {}
    cont[nombre] = 0
    # número de hilos que se van a utilizar
    num_threads = 4

    def thread_function(section,nombre):
        
        for i in section:
            nombres2 = str(i[5])
            nombres2 = nombres2.split()
            primer_nombre = nombres2[0]
            
            if nombre == primer_nombre:
                cont[nombre] = cont[nombre]+1
            if len(nombres2) == 2:
                segundo_nombre = nombres2[1]
                if nombre == segundo_nombre:
                    cont[nombre] = cont[nombre]+1
        
        

    # dividir la matriz en secciones
    section_size = len(matriz) // num_threads
    sections = [matriz[i:i+section_size] for i in range(0, len(matriz), section_size)]

    # crear y ejecutar los hilos
    threads = []
    for section in sections:
        thread = threading.Thread(target=thread_function, args=(section,nombre))
        thread.start()
        threads.append(thread)

    # esperar a que los hilos terminen
    for thread in threads:
        thread.join()
        
    
    fin = time.time()
    print("Hay "+str(cont[nombre])+" personas con el apellido "+nombre)
    print("El codigo duro: "+str(fin-inicio))
    input("Presione Enter para continuar...")
