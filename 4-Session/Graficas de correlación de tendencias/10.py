import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Datos en formato de lista
data_solutions = [
    ['Automatización del Marketing', 16],
    ['Herramientas de análisis para Big Data y sistemas predictivos', 22],
    ['Formación de los empleados', 51],
    ['Cloud', 64],
    ['Ciberseguridad', 66],
    ['Database', 70],
    ['Equipamiento e infraestructura', 81]
]

# Convertir datos a un array de numpy
data_array_solutions = np.array(data_solutions)

# Extraer columnas relevantes
solutions = data_array_solutions[:, 0]  # Soluciones
percentages_solutions = data_array_solutions[:, 1].astype(float)  # Porcentajes

# Hipótesis
# Hipótesis nula (H₀): No existe correlación entre las soluciones tecnológicas (porcentaje no correlacionado).
# Hipótesis alternativa (H₁): Existe correlación entre los porcentajes de adopción de las soluciones.

# Realizar el análisis de correlación (en este caso, calculamos el coeficiente de correlación entre los porcentajes)
# En este caso, dado que tenemos solo un conjunto de datos de porcentajes, simularemos una relación con un nuevo conjunto de datos.
# Por ejemplo, podríamos comparar el porcentaje con un conjunto hipotético relacionado con otro factor (ej. inversión en tecnología).
investments = np.array([15, 20, 50, 60, 65, 72, 80])  # Inversión simulada en tecnología

# Calcular el coeficiente de correlación de Pearson entre los porcentajes y la inversión
corr_coefficient, _ = pearsonr(percentages_solutions, investments)

# Mostrar el resultado del coeficiente de correlación
print(f"Coeficiente de correlación de Pearson: {corr_coefficient:.2f}")

# Crear un gráfico de dispersión (scatter plot) para mostrar la correlación
plt.figure(figsize=(10, 6))
plt.scatter(percentages_solutions, investments, color='b', label='Datos', edgecolors='black')

# Añadir una línea de tendencia (regresión lineal)
m, b = np.polyfit(percentages_solutions, investments, 1)
plt.plot(percentages_solutions, m*percentages_solutions + b, color='r', label='Línea de tendencia')

# Añadir título y etiquetas
plt.title('Correlación entre el Porcentaje de Soluciones y la Inversión en Tecnología', fontsize=16, fontweight='bold')
plt.xlabel('Porcentaje de Soluciones (%)', fontsize=12)
plt.ylabel('Inversión en Tecnología ($)', fontsize=12)
plt.legend()

# Mostrar la cuadrícula
plt.grid(True)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
