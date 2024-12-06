import numpy as np
import matplotlib.pyplot as plt

# Datos originales
scores_sep_2024 = np.array([1286.59, 1029.49, 807.76, 644.36, 410.24, 149.43, 133.72, 128.79, 123.05, 103.35])
scores_aug_2024 = scores_sep_2024 + np.array([28.11, 2.63, -7.41, 6.97, -10.74, -3.28, -2.25, -1.04, 0.04, -1.44])
scores_sep_2023 = scores_sep_2024 + np.array([45.72, -82.00, -94.45, 23.61, -29.18, -14.26, 12.83, -10.20, -13.67, -25.85])

# Función para graficar correlación con línea de tendencia
def plot_comparison(x, y, xlabel, ylabel, title, color):
    # Ajuste lineal (línea de tendencia)
    coeffs = np.polyfit(x, y, 1)  # Pendiente y término independiente
    trend_line = np.poly1d(coeffs)  # Función de la línea de tendencia
    y_fit = trend_line(x)  # Valores ajustados
    
    # Graficar
    plt.scatter(x, y, color=color, label='Datos')
    plt.plot(x, y_fit, color='black', linestyle='--', label='Línea de tendencia')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid()

# Calcular correlaciones
corr_sep_aug = np.corrcoef(scores_sep_2024, scores_aug_2024)[0, 1]
corr_sep_sep23 = np.corrcoef(scores_sep_2024, scores_sep_2023)[0, 1]
corr_aug_sep23 = np.corrcoef(scores_aug_2024, scores_sep_2023)[0, 1]

# Graficar las comparaciones
plt.figure(figsize=(15, 5))

# Gráfico Sep 2024 vs Aug 2024
plt.subplot(1, 3, 1)
plot_comparison(
    scores_sep_2024, scores_aug_2024, 
    'Scores Sep 2024', 'Scores Aug 2024', 
    f'Sep 2024 vs Aug 2024 (r = {corr_sep_aug:.2f})', 'green'
)

# Gráfico Sep 2024 vs Sep 2023
plt.subplot(1, 3, 2)
plot_comparison(
    scores_sep_2024, scores_sep_2023, 
    'Scores Sep 2024', 'Scores Sep 2023', 
    f'Sep 2024 vs Sep 2023 (r = {corr_sep_sep23:.2f})', 'blue'
)

# Gráfico Aug 2024 vs Sep 2023
plt.subplot(1, 3, 3)
plot_comparison(
    scores_aug_2024, scores_sep_2023, 
    'Scores Aug 2024', 'Scores Sep 2023', 
    f'Aug 2024 vs Sep 2023 (r = {corr_aug_sep23:.2f})', 'red'
)

# Mostrar todas las gráficas juntas
plt.tight_layout()
plt.show()

# Imprimir las correlaciones
print(f"Correlación entre Sep 2024 y Aug 2024: {corr_sep_aug:.2f}")
print(f"Correlación entre Sep 2024 y Sep 2023: {corr_sep_sep23:.2f}")
print(f"Correlación entre Aug 2024 y Sep 2023: {corr_aug_sep23:.2f}")
