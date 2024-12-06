import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Datos en formato de lista
data = [
    [1, 1, '', 'Python', '20.17%', '+6.01%'],
    [2, 3, 'change', 'C++', '10.75%', '+0.09%'],
    [3, 4, 'change', 'Java', '9.45%', '-0.04%'],
    [4, 2, 'change', 'C', '8.89%', '-2.38%'],
    [5, 5, '', 'C#', '6.08%', '-1.22%'],
    [6, 6, '', 'JavaScript', '3.92%', '+0.62%'],
    [7, 7, '', 'Visual Basic', '2.70%', '+0.48%'],
    [8, 12, 'change', 'Go', '2.35%', '+1.16%'],
    [9, 10, 'change', 'SQL', '1.94%', '+0.50%'],
    [10, 11, 'change', 'Fortran', '1.78%', '+0.49%'],
    [11, 15, 'change', 'Delphi/Object Pascal', '1.77%', '+0.75%'],
    [12, 13, 'change', 'MATLAB', '1.47%', '+0.28%'],
    [13, 8, 'change', 'PHP', '1.46%', '-0.09%'],
    [14, 17, 'change', 'Rust', '1.32%', '+0.35%'],
    [15, 18, 'change', 'R', '1.20%', '+0.23%'],
    [16, 19, 'change', 'Ruby', '1.13%', '+0.18%'],
    [17, 14, 'change', 'Scratch', '1.11%', '+0.03%'],
    [18, 20, 'change', 'Kotlin', '1.10%', '+0.20%'],
    [19, 21, 'change', 'COBOL', '1.09%', '+0.22%'],
    [20, 16, 'change', 'Swift', '1.08%', '+0.09%']
]

# Convertir datos a un array de numpy
data_array = np.array(data)

# Extraer columnas relevantes
programming_languages = data_array[:, 3]  # Lenguajes de programación
ratings_str = data_array[:, 4]  # Ratings en formato de cadena
change_rating_str = data_array[:, 5]  # Cambio en rating en formato de cadena

# Convertir ratings y cambios a float
ratings = np.array([float(r.strip('%')) for r in ratings_str])
change_ratings = np.array([float(c.strip('%')) if c else 0 for c in change_rating_str])

# Calcular correlación de Pearson
correlation, p_value = pearsonr(ratings, change_ratings)

# Hipótesis
hipothesis = """
Hipótesis:
H0: No existe correlación significativa entre los ratings y el cambio en los ratings.
H1: Existe una correlación significativa entre los ratings y el cambio en los ratings.
"""

# Mostrar hipótesis
print(hipothesis)
print(f"Coeficiente de correlación (r): {correlation:.2f}")
print(f"Valor p: {p_value:.4f}")

# Graficar la correlación
plt.figure(figsize=(10, 6))
plt.scatter(ratings, change_ratings, color='purple', edgecolor='black', s=100, alpha=0.7)
plt.title('Correlación entre Ratings y Cambio en Ratings', fontsize=14)
plt.xlabel('Ratings (%)', fontsize=12)
plt.ylabel('Cambio en Ratings (%)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)  # Línea en y=0
plt.axvline(np.mean(ratings), color='blue', linestyle='--', linewidth=0.8, label='Promedio Ratings')  # Línea promedio ratings
plt.legend()

# Guardar el gráfico como SVG
plt.tight_layout()
plt.savefig('correlacion_ratings.svg', format='svg')
plt.show()
