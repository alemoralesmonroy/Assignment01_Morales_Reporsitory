import csv
import random
import os


def generar_matriz_csv(n, filename, seed):
    # El protocolo exige usar una semilla conocida para la reproducibilidad
    random.seed(seed)

    # Crea la carpeta 'inputs' si no existe
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        for _ in range(n):
            # Usamos floats de 64 bits con valores entre 0.0 y 10.0
            row = [random.uniform(0.0, 10.0) for _ in range(n)]
            writer.writerow(row)

    print(f"Generada matriz de {n}x{n} en: {filename} (Semilla: {seed})")


if __name__ == "__main__":
    # Secuencia declarada de tamaños
    secuencia_n = [100, 250, 500, 1000]

    for n in secuencia_n:
        print(f"Generando matrices de {n}x{n}...")
        generar_matriz_csv(n, f"inputs/matriz_A_{n}.csv", seed=42)
        generar_matriz_csv(n, f"inputs/matriz_B_{n}.csv", seed=43)

    print("\n¡Generación de toda la secuencia completada!")