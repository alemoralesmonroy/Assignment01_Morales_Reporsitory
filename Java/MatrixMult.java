package Java;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

public class MatrixMult {

    // Lector de CSV básico para matrices cuadradas
    public static double[][] leerCSV(String filename, int n) throws IOException {
        double[][] matriz = new double[n][n];
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            int row = 0;
            while ((line = br.readLine()) != null && row < n) {
                String[] values = line.split(",");
                for (int col = 0; col < n; col++) {
                    matriz[row][col] = Double.parseDouble(values[col]);
                }
                row++;
            }
        }
        return matriz;
    }

    // Algoritmo clásico O(n^3) requerido
    public static double[][] multiplicarMatrices(int n, double[][] A, double[][] B) {
        double[][] C = new double[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                C[i][j] = 0.0;
                for (int k = 0; k < n; k++) {
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }
        return C;
    }

    public static void main(String[] args) {
        int[] secuencia_n = {100, 250, 500, 1000};
        double tiempo_limite = 120.0;

        for (int n : secuencia_n) {
            System.out.println("\n--- Evaluando tamaño n=" + n + " ---");
            Path rutaA = Paths.get("inputs", "matriz_A_" + n + ".csv").toAbsolutePath();
            Path rutaB = Paths.get("inputs", "matriz_B_" + n + ".csv").toAbsolutePath();

            try {
                double[][] A = leerCSV(rutaA.toString(), n);
                double[][] B = leerCSV(rutaB.toString(), n);

                System.out.println("Fase de calentamiento...");
                for (int w = 0; w < 3; w++) {
                    multiplicarMatrices(n, A, B);
                }

                boolean timeoutAlcanzado = false;
                System.out.println("Iniciando benchmark...");

                for (int r = 0; r < 5; r++) {
                    long start = System.nanoTime();
                    multiplicarMatrices(n, A, B);
                    long end = System.nanoTime();

                    double elapsed = (end - start) / 1e9;
                    System.out.printf("Repetición %d - Tiempo Java: %.6f s%n", r + 1, elapsed);

                    if (elapsed > tiempo_limite) {
                        System.out.println("TIMEOUT: La ejecución superó el límite de " + tiempo_limite + "s.");
                        timeoutAlcanzado = true;
                        break;
                    }
                }

                // Forzar recolección de basura y medir memoria del Heap
                Runtime runtime = Runtime.getRuntime();
                runtime.gc();
                long memoriaUsada = runtime.totalMemory() - runtime.freeMemory();
                double picoMB = memoriaUsada / (1024.0 * 1024.0);
                System.out.printf("Métrica de Memoria (Heap gestionado): %.2f MB%n", picoMB);

                if (timeoutAlcanzado) {
                    System.out.println("Abortando prueba de tamaños mayores debido a timeout en n=" + n);
                    break;
                }

            } catch (IOException e) {
                System.err.println("Error leyendo los archivos: " + e.getMessage());
            }
        }
    }
}