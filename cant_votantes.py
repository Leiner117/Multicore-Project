from os import system
import threading
import time
#Codigo unifica las consultas b,c,f ya que el codigo de las 3 es muy parecido
#Se opto por crear un mismo codigo que realice las 3 consultas 
#Al pasar por parametro un valor en la variable llamada op
#El codigo detecta la consulta que quirer realizar
#0:B
#1: F
#2: e
#3:c
#4: d


#Seleccionar el modo de ejecucion del programa
def seleccionarModo(matriz,op):
    system("cls")
    opciones = {2:"Cantones",1:"Distritos",}
    print("1. Modo Secuencial\n2. Modo Multiprocesamiento\n3. Ambos\n4. Salir")
    select = int(input("Ingrese la opcion que desea:"))
    cantidad = 0
    if select == 4:
        return
    if  (op == 1 or op == 2):
        cantidad = int(input("Ingrese la cantidad de "+opciones[op]+" que quiere imprimir:" ))
    if (select == 1):
        metodo_secuencial(matriz,op,cantidad)
    elif (select == 2):
        metodo_multicore(matriz,op,cantidad)
    elif (select == 3):
        metodo_secuencial(matriz,op,cantidad)
        metodo_multicore(matriz,op,cantidad)
    
        
        
    
#Funcion que se encarga de imprimir la cantidad de Distritos que se desea
def imprimir(lista,op,cantidad):
    provincias = {1:"San Jose",2:"Alajuela",3:"Cartago",4:"Heredia",5:"Guanacaste",6:"Puntarenas",7:"Limon",8:"Extranjeros"}
    
    sorted_dict = dict(sorted(lista.items(), key=lambda x: x[1], reverse=True))
    i = 0
    for a in sorted_dict:
        if op == 0:
            print(provincias[int(a)]+":"+str(sorted_dict[a]))
            
        else:
            print(str(a)+":"+str(sorted_dict[a]))
            i = i+1
            if (i == cantidad):
                break
            
#Metodo secuncial:
#Se recorre la matriz
#Se verifica si el distrito se encuentra en el diccionario
#Si se encuentra se suma 1 al valor del distrito
#Sino se agrega en el diccionario
def metodo_secuencial(matriz,op,cantidad):
    print("Metodo secuencia")
    inicio = time.time()
    dic = {}
    valor = 0
    for x in matriz:
        
        if op == 1 or op==4:
            valor = x[1]
        elif op == 3 or op == 2:
            valor = x[1][0:3]
        elif op == 0:
            valor = x[1][0]
        
        if valor not in dic:

            dic[valor] = 1
        else:
            dic[valor] = dic[valor] +1
    imprimir(dic,op,cantidad)
    fin = time.time()
    
    print("El codigo duro: "+str(fin-inicio))



#Metodo multicore
#Crea hilos que se encargan de ejecutar la funcion al mismo tiempo
def metodo_multicore(matriz,op,cantidad):
    print("Metodo Multicore")
    inicio = time.time()
    dic = {}
    # número de hilos que se van a utilizar
    num_threads = 3
    def thread_function(section):
        
        for x in section:
            if op == 1 or op == 4:
                valor = x[1]
            elif op == 3 or op == 2:
                valor = x[1][0:3]
            elif op == 0:
                valor = x[1][0]
            if valor not in dic:

                dic[valor] = 1
            else:
                dic[valor] = dic[valor] +1
        

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
        
    imprimir(dic,op,cantidad)
    fin = time.time()
    print("El codigo duro: "+str(fin-inicio))
    input("Presione Enter para continuar...")