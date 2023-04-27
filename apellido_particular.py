import threading
import time


def seleccionarModo(matriz):
    
    print("1. Modo Secuencial\n2. Modo Multiprocesamiento\n3. Ambos\n4. Salir")
    select = int(input("Ingrese la opcion que desea:"))
    op,apellido = select_apellido()
    if select == 4:
        return
    
    if (select == 1):
        metodo_secuencial(matriz,apellido,op)
    elif (select == 2):
        metodo_multicore(matriz,apellido,op)
    elif (select == 3):
        metodo_secuencial(matriz,apellido,op)
        metodo_multicore(matriz,apellido,op)
def select_apellido():
    print("Desea buscar el:\n1.Primer Apellido\n2.Segundo Apellido\n3. Ambos")
    try:
        select = int(input("==> "))
    except:
        print("Formato incorrecto")
    
    print("Ingrese el apellido o Apellidos que desea buscar: ")
    apellido = input("==> ").upper()
    return select,apellido




        
        

def metodo_secuencial(matriz,apellido,op):
    print("Metodo secuencia")
    inicio = time.time()
    cont = 0

    for i in matriz:
        if op == 1:
            apellido2 = str(i[6])
            apellido2 = "".join(apellido2.split())
            if apellido == apellido2:
                cont = cont+1
        elif op == 2:
            apellido2 = str(i[7])
            apellido2 = "".join(apellido2.split())
            if apellido == apellido2:
                cont = cont+1
        elif op == 3:
            apellido1 = str(i[6])
            apellido1 = "".join(apellido1.split())
            apellido2 = str(i[7])
            apellido2 = "".join(apellido2.split())
            apellidos = apellido1 +" "+apellido2
            if apellido == apellidos:
                cont = cont+1
    
    fin = time.time()
    print("Hay "+str(cont)+" personas con el apellido "+apellido)
    print("El codigo duro: "+str(fin-inicio))










def metodo_multicore(matriz,apellido,op):
    print("Metodo Multicore")
    inicio = time.time()
    cont = {}
    cont[apellido] = 0
    # número de hilos que se van a utilizar
    num_threads = 4
    def thread_function(section,apellido,op):
        
        for i in section:
            if op == 1:
                apellido2 = str(i[6])
                apellido2 = "".join(apellido2.split())
                if apellido == apellido2:
                    cont[apellido] = cont[apellido]+1
            elif op == 2:
                apellido2 = str(i[7])
                apellido2 = "".join(apellido2.split())
                if apellido == apellido2:
                    cont[apellido] = cont[apellido]+1
            elif op == 3:
                apellido1 = str(i[6])
                apellido1 = "".join(apellido1.split())
                apellido2 = str(i[7])
                apellido2 = "".join(apellido2.split())
                apellidos = apellido1 +" "+apellido2
                if apellido == apellidos:
                    cont[apellido] =cont[apellido]+1
        
        

    # dividir la matriz en secciones
    section_size = len(matriz) // num_threads
    sections = [matriz[i:i+section_size] for i in range(0, len(matriz), section_size)]

    # crear y ejecutar los hilos
    threads = []
    for section in sections:
        thread = threading.Thread(target=thread_function, args=(section,apellido,op))
        thread.start()
        threads.append(thread)

    # esperar a que los hilos terminen
    for thread in threads:
        thread.join()
        
    
    fin = time.time()
    print("Hay "+str(cont[apellido])+" personas con el apellido "+apellido)
    print("El codigo duro: "+str(fin-inicio))
