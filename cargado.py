<<<<<<< HEAD
def cargar_archivo(nombre_archivo):
    matriz = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            campos = linea.strip().split(",")
            matriz.append(campos)
    return matriz

=======
def cargar_archivo(nombre_archivo):
    matriz = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            campos = linea.strip().split(",")
            matriz.append(campos)
    return matriz

>>>>>>> f32a626f4b376edaf5eee7f5ebbc16f76b1926a6
print(cargar_archivo("PADRON_COMPLETO.txt"))