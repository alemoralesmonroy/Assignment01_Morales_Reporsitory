#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include <psapi.h>

double** leer_csv(const char* filename, int n) {
    double** matriz = (double**)malloc(n * sizeof(double*));
    for (int i = 0; i < n; i++) {
        matriz[i] = (double*)malloc(n * sizeof(double));
    }
    FILE* file = fopen(filename, "r");
    if (!file) return NULL;

    char line[8192];
    int row = 0;
    while (fgets(line, sizeof(line), file) && row < n) {
        char* token = strtok(line, ",");
        int col = 0;
        while (token && col < n) {
            matriz[row][col] = atof(token);
            token = strtok(NULL, ",");
            col++;
        }
        row++;
    }
    fclose(file);
    return matriz;
}

void multiplicar_matrices(int n, double** A, double** B, double** C_mat) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            C_mat[i][j] = 0.0;
            for (int k = 0; k < n; k++) {
                C_mat[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

void liberar_matriz(double** matriz, int n) {
    for (int i = 0; i < n; i++) free(matriz[i]);
    free(matriz);
}

int main() {
    int secuencia_n[] = {100, 250, 500, 1000};
    int num_sizes = 4;
    double tiempo_limite = 120.0;
    
    LARGE_INTEGER frequency, start, end;
    QueryPerformanceFrequency(&frequency);

    for (int s = 0; s < num_sizes; s++) {
        int n = secuencia_n[s];
        printf("\n--- Evaluando tamano n=%d ---\n", n);
        
        char ruta_A[256], ruta_B[256];
        sprintf(ruta_A, "../inputs/matriz_A_%d.csv", n);
        sprintf(ruta_B, "../inputs/matriz_B_%d.csv", n);

        double** A = leer_csv(ruta_A, n);
        double** B = leer_csv(ruta_B, n);
        if (!A || !B) {
            printf("Error leyendo CSV.\n");
            return 1;
        }

        double** C_mat = (double**)malloc(n * sizeof(double*));
        for (int i = 0; i < n; i++) C_mat[i] = (double*)malloc(n * sizeof(double));

        int timeout_alcanzado = 0;
        printf("Iniciando benchmark (5 repeticiones)...\n");
        
        for (int r = 0; r < 5; r++) {
            QueryPerformanceCounter(&start);
            multiplicar_matrices(n, A, B, C_mat);
            QueryPerformanceCounter(&end);
            
            double elapsed = (double)(end.QuadPart - start.QuadPart) / frequency.QuadPart;
            printf("Repeticion %d - Tiempo C: %.6f s\n", r + 1, elapsed);
            
            if (elapsed > tiempo_limite) {
                printf("TIMEOUT: La ejecucion supero el limite de %.1fs.\n", tiempo_limite);
                timeout_alcanzado = 1;
                break;
            }
        }

        PROCESS_MEMORY_COUNTERS pmc;
        if (GetProcessMemoryInfo(GetCurrentProcess(), &pmc, sizeof(pmc))) {
            double pico_mb = pmc.PeakWorkingSetSize / (1024.0 * 1024.0);
            printf("Metrica de Memoria (Peak Working Set): %.2f MB\n", pico_mb);
        }

        liberar_matriz(A, n);
        liberar_matriz(B, n);
        liberar_matriz(C_mat, n);

        if (timeout_alcanzado) {
            printf("Abortando prueba de tamanos mayores debido a timeout en n=%d\n", n);
            break;
        }
    }
    return 0;
}