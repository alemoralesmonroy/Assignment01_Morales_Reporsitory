import numpy as np


# Nuestro algoritmo a validar
def multiplicar_matrices_nuestro(n, A, B):
    C = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def validar_correccion():
    n = 10
    print(f"Iniciando pruebas de corrección con n={n}...\n")

    # 1. Prueba con Matriz de Ceros
    A_zeros = np.zeros((n, n)).tolist()
    B_rand = np.random.uniform(0.0, 10.0, (n, n)).tolist()
    C_zeros_nuestro = multiplicar_matrices_nuestro(n, A_zeros, B_rand)
    C_zeros_ref = np.matmul(A_zeros, B_rand)

    es_correcto_ceros = np.allclose(C_zeros_nuestro, C_zeros_ref, rtol=1e-9, atol=1e-9)
    print(f"Prueba matriz de ceros: {'PASADA' if es_correcto_ceros else 'FALLADA'}")

    # 2. Prueba con Matriz Identidad
    A_identidad = np.eye(n).tolist()
    C_identidad_nuestro = multiplicar_matrices_nuestro(n, A_identidad, B_rand)
    C_identidad_ref = np.matmul(A_identidad, B_rand)

    es_correcto_ident = np.allclose(C_identidad_nuestro, C_identidad_ref, rtol=1e-9, atol=1e-9)
    print(f"Prueba matriz identidad: {'PASADA' if es_correcto_ident else 'FALLADA'}")

    # 3. Prueba con Matrices Aleatorias
    A_rand = np.random.uniform(0.0, 10.0, (n, n)).tolist()
    C_rand_nuestro = multiplicar_matrices_nuestro(n, A_rand, B_rand)
    C_rand_ref = np.matmul(A_rand, B_rand)

    es_correcto_rand = np.allclose(C_rand_nuestro, C_rand_ref, rtol=1e-9, atol=1e-9)
    print(f"Prueba matrices aleatorias: {'PASADA' if es_correcto_rand else 'FALLADA'}")


if __name__ == "__main__":
    validar_correccion()