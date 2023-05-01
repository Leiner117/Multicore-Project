import threading


def get_third_data(matrix):
    # Get the number of available threads
    num_threads = threading.active_count()

    # Divide the matrix into n equal parts
    chunk_size = len(matrix) // num_threads
    if chunk_size == 0:
        
        return ("Dato no encontrado")
    else:
        chunks = [matrix[i:i+chunk_size] for i in range(0, len(matrix), chunk_size)]

    # If there's a smaller fragment, add it to the last chunk
    if len(chunks[-1]) < chunk_size and len(chunks) > 1:
        chunks[-2].extend(chunks[-1])
        chunks.pop()

    # Create a list to store the results
    results = [[] for _ in range(num_threads)]

    # Define a function to process each chunk
    def process_chunk(chunk, results, thread_id):
        for row in chunk:
            print(row[5]," ",row[6]," ",row[7],"\n")
            #results[thread_id].append(row[5])
            #results[thread_id].append(row[6])
            #results[thread_id].append(row[7])

    # Create and start a thread for each chunk
    threads = []
    for i, chunk in enumerate(chunks):
        t = threading.Thread(target=process_chunk, args=(chunk, results, i))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Concatenate the results and return them
    return [result for sublist in results for result in sublist]




def find_matching_data(matrix, target):
    # Get the number of available threads
    num_threads = threading.active_count()

    # Divide the matrix into n equal parts
    chunk_size = len(matrix) // num_threads
    chunks = [matrix[i:i+chunk_size] for i in range(0, len(matrix), chunk_size)]

    # If there's a smaller fragment, add it to the last chunk
    if len(chunks[-1]) < chunk_size and len(chunks) > 1:
        chunks[-2].extend(chunks[-1])
        chunks.pop()

    # Create a list to store the results
    results = [[] for _ in range(num_threads)]

    # Define a function to process each chunk
    def process_chunk(chunk, results, thread_id):
        for row in chunk:
            if target in row:
                results[thread_id].append(row)

    # Create and start a thread for each chunk
    threads = []
    for i, chunk in enumerate(chunks):
        t = threading.Thread(target=process_chunk, args=(chunk, results, i))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Concatenate the results and return them
    return [result for sublist in results for result in sublist]


def encontrar_terceros_datos(matriz):
    terceros_datos = []
    for fila in matriz:
        # Comprobamos si la fila tiene al menos tres elementos
        if len(fila) < 3:
            terceros_datos.append(None)
        else:
            print(fila[5]," ",fila[6]," ",fila[7],"\n")
            #terceros_datos.append(fila[2])
    return terceros_datos


def buscar_persona(matriz, exp):
    mn = []
    for i in range(len(matriz)):
        if exp in matriz[i]:
            mn.append(matriz[i])
    return mn
