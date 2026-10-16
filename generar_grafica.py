import matplotlib.pyplot as plt

sizes = [100, 250, 500, 1000]

time_java = [0.002033, 0.022276, 0.177629, 5.516295]
time_c = [0.005313, 0.060567, 0.644889, 8.630204]
time_python = [0.500207, 7.810342, 63.253833, 120.0]

plt.figure(figsize=(10, 6))

plt.plot(sizes, time_java, marker='o', linestyle='-', color='#0073e6', linewidth=2, label='Java (JIT)')
plt.plot(sizes, time_c, marker='s', linestyle='-', color='#e60000', linewidth=2, label='C (AOT - /O2)')
plt.plot(sizes, time_python, marker='^', linestyle='--', color='#2ca02c', linewidth=2, label='Python (Interpreted)')

plt.annotate('TIMEOUT (>120s)', xy=(1000, 120), xytext=(800, 110),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6),
             fontsize=10, color='black', weight='bold')

plt.title('Execution Time vs. Matrix Size (O(n³))', fontsize=14, pad=15)
plt.xlabel('Matrix Size (n x n)', fontsize=12)
plt.ylabel('Median Execution Time (Seconds)', fontsize=12)
plt.xticks(sizes)
plt.yscale('linear')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=11)

plt.tight_layout()
plt.savefig('performance_plot.png', dpi=300)
print("Gráfica guardada como performance_plot.png")