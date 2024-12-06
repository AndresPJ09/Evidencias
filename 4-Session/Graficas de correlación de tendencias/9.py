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

# Datos adicionales de inversión
investments = [10, 15, 30, 50, 55, 60, 80]  # Inversión en miles de dólares

# Calcular el coeficiente de correlación de Pearson entre porcentajes y la inversión
corr_coefficient, _ = pearsonr(percentages_solutions, investments)

# Mostrar el resultado del coeficiente de correlación
print(f"Coeficiente de correlación de Pearson: {corr_coefficient:.2f}")

# Graficar los datos
plt.figure(figsize=(10, 6))

# Crear gráfico de dispersión
plt.scatter(percentages_solutions, investments, color='blue', label='Datos')

# Añadir una línea de tendencia
m, b = np.polyfit(percentages_solutions, investments, 1)
plt.plot(percentages_solutions, m*percentages_solutions + b, color='red', label='Línea de tendencia')

# Títulos y etiquetas
plt.title('Correlación entre Adopción de Soluciones Tecnológicas y la Inversión', fontsize=16)
plt.xlabel('Porcentaje de Adopción (%)', fontsize=12)
plt.ylabel('Inversión en Tecnología ($ en miles)', fontsize=12)
plt.legend()
plt.grid(True)

# Mostrar gráfico
plt.tight_layout()
plt.show()
