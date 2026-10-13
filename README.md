# Big Data - Assignment 1: Matrix Multiplication Benchmark

**Author:** Alejandro Morales Monroy  
**Course:** Big Data (Data Science and Engineering)

## Project Overview
This repository contains the source code and reproducibility materials for Assignment 1. It benchmarks the classic $O(n^3)$ dense matrix multiplication algorithm across three languages: Python (interpreted), Java (JIT compiled), and C (AOT compiled). 

## Environment Details
- **OS:** Windows
- **CPU:** Intel Core i7-10400F
- **RAM:** 16 GB
- **Languages & Compilers:**
  - Python 3.x
  - Java JDK 21
  - C Compiler: MSVC (`cl.exe`)

## Dependencies
- Python: `numpy` (used exclusively for correctness validation).
  ```bash
  pip install numpy
  
## Repository Structure
- `generador_matrices.py`: Python script that generates the square matrices with random 64-bit float values and saves them as CSV files. It uses fixed seeds (42 and 43) to guarantee the reproducibility of the inputs.
- `validacion_correccion.py`: Script that uses `numpy` as a baseline reference to mathematically validate the custom $O(n^3)$ algorithm, applying strict absolute and relative tolerances ($10^{-9}$) to account for floating-point arithmetic.
- `analisis_resultados.py`: Python script to compute statistical metrics (median and interquartile range) from the raw benchmark execution data.
- `/inputs`: Directory containing the generated CSV matrix files used across all three languages.
- `/Python`: Directory containing `matrix_mult.py`, the Python implementation of the benchmark, including time tracking and peak memory profiling (`tracemalloc`).
- `/Java`: Directory containing `MatrixMult.java`, which includes the algorithm implementation, JIT warm-up iterations, and `Runtime` heap memory profiling.
- `/C`: Directory containing `matrix_mult.c`, the C implementation using native Windows APIs (`QueryPerformanceCounter` for precise timing and `psapi.h` for Peak Working Set memory profiling).

## Build and Run Instructions
### 1. Data generation
Generate the input matrices first (sizes 100, 250, 500, 1000):
```bash
python generador_matrices.py
```

### 2. Python execution
Run the mathematical validation from the root directory first:
```bash
python validacion_correccion.py
```
Then, execute the benchmark:
```bash
cd Python
python matrix_mult.py
```

### 3. Java execution
Compile and run using JDK 21:
```bash
cd Java
javac MatrixMult.java
java MatrixMult
```

### 4. C execution
Compile using Microsoft Visual C++(MSVC) with the maximum speed optimization flag(`/02`):
```bash
cd C
cl.exe /02 matrix_mult.c
.\matrix_mult.exe
```