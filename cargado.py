def cargar_archivo(nombre_archivo):
    matriz = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            campos = linea.strip().split(",")
            matriz.append(campos)
    return matriz

print(cargar_archivo("PADRON_COMPLETO.txt"))