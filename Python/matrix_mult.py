import time
import csv
import os
import tracemalloc


def leer_csv(filename):
    matriz = []
    with open(filename, mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
            matriz.append([float(val) for val in row])
    return matriz


def multiplicar_matrices(n, A, B):
    C = [[0.0 for _ in range(n)] for _ in range(n)]

    start_time = time.perf_counter()

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    end_time = time.perf_counter()
    return C, end_time - start_time


if __name__ == "__main__":
    secuencia_n = [100, 250, 500, 1000]
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    tiempo_limite = 120.0

    for n in secuencia_n:
        print(f"\n--- Evaluando tamaño n={n} ---")
        ruta_A = os.path.abspath(os.path.join(directorio_actual, "..", "inputs", f"matriz_A_{n}.csv"))
        ruta_B = os.path.abspath(os.path.join(directorio_actual, "..", "inputs", f"matriz_B_{n}.csv"))

        print("Cargando matrices en memoria...")
        A = leer_csv(ruta_A)
        B = leer_csv(ruta_B)

        tiempos = []
        timeout_alcanzado = False

        tracemalloc.start()

        for repeticion in range(5):
            _, tiempo = multiplicar_matrices(n, A, B)
            tiempos.append(tiempo)
            print(f"Repetición {repeticion + 1} - Tiempo Python: {tiempo:.6f} s")

            if tiempo > tiempo_limite:
                print(f"TIMEOUT: La ejecución superó el límite de {tiempo_limite}s.")
                timeout_alcanzado = True
                break

        _, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        pico_mb = peak_memory / (1024 * 1024)
        print(f"Métrica de Memoria (tracemalloc pico): {pico_mb:.2f} MB")

        if timeout_alcanzado:
            print(f"Abortando prueba de tamaños mayores debido a timeout en n={n}.")
            break