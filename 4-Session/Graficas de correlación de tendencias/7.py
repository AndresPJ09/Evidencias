import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Datos en formato de lista
data1 = [
    [2017, 1, 2],
    [2018, 1, 3],
    [2019, 2, 4],
    [2020, 3, 5],
    [2021, 5, 8],
    [2022, 7, 10],
    [2023, 10, 15],
    [2024, 15, 30],
    [2025, 25, 45]
]

# Convertir datos a un array de numpy
data_array1 = np.array(data1)

# Extraer columnas relevantes
years1 = data_array1[:, 0]  # Años
low_values = data_array1[:, 1]  # Valores bajos
high_values = data_array1[:, 2]  # Valores altos

# Crear un gráfico de dispersión para comparar los valores bajos vs altos
plt.figure(figsize=(10, 6))
plt.scatter(low_values, high_values, color='purple', edgecolor='black', s=100, alpha=0.7)
plt.title('Correlación entre Valores Bajos y Altos (2017-2025)', fontsize=14)
plt.xlabel('Valores Bajos ($Billions)', fontsize=12)
plt.ylabel('Valores Altos ($Billions)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Calcular la correlación de Pearson
correlation, p_value = pearsonr(low_values, high_values)

# Añadir línea de tendencia
plt.plot(np.unique(low_values), np.poly1d(np.polyfit(low_values, high_values, 1))(np.unique(low_values)), color='red', label='Línea de Tendencia')

# Mostrar el gráfico
plt.legend()
plt.tight_layout()

# Guardar gráfico en formato SVG
plt.savefig('Correlacion_Valores_Bajos_Altos.svg', format='svg')

plt.show()

# Mostrar los resultados de la correlación
print(f"Coeficiente de correlación (r): {correlation:.2f}")
print(f"Valor p: {p_value:.4f}")
