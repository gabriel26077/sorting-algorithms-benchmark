import time

def measure_time(algorithm, array):
    start = time.time()
    algorithm(array)
    end = time.time()
    return end - start
