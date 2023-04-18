import threading
from collections import Counter
from collections import defaultdict



def get_name_data(matrix):
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
            results[thread_id].append(row[5])

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




def count_occurrences(data, result_dict):
    counts = Counter(data)
    for name, count in counts.items():
        result_dict[name] += count

def find_top_x(data, x):
    result_dict = Counter()
    chunk_size = len(data) // threading.active_count()
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    threads = []
    for chunk in chunks:
        thread = threading.Thread(target=count_occurrences, args=(chunk, result_dict))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return result_dict.most_common(int(x))


def count_occurrences2(data, result_dict):
    counts = defaultdict(int)
    for item in data:
        counts[item] += 1
    for name, count in counts.items():
        result_dict[name] += count


def find_least_x(data, x):
    result_dict = defaultdict(int)
    chunk_size = len(data) // threading.active_count()
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    threads = []
    for chunk in chunks:
        thread = threading.Thread(target=count_occurrences2, args=(chunk, result_dict))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    least_x = sorted(result_dict.items(), key=lambda item: item[1])[:int(x)]
    return least_x



def menos_comunes(nombres, x):
    contador = Counter(nombres)
    menos_comunes = sorted(contador.items(), key=lambda x: x[1])[:int(x)]
    return menos_comunes


def mas_comunes(nombres, x):
    contador = Counter(nombres)
    mas_comunes = sorted(contador.items(), key=lambda x: x[1], reverse=True)[:int(x)]
    return mas_comunes

def buscar_cuartos_campos(matriz):
    cuartos_campos = []
    for fila in matriz:
        if len(fila) >= 4:
            cuarto_campo = fila[5]
            cuartos_campos.append(cuarto_campo)
        else:
            cuartos_campos.append(None)
    return cuartos_campos