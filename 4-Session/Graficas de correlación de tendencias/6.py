import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Datos en formato de lista
data = [
    ['Python', 100],
    ['Java', 70],
    ['Spring', 60],
    ['AWS', 50],
    ['Kubernetes', 40],
    ['Angular', 35],
    ['Docker', 35],
    ['JavaScript', 30],
    ['Spark', 25],
    ['Machine Learning', 25],
    ['React', 20],
    ['Go', 15],
    ['Microservices', 10],
    ['Blockchain', 10]
]

# Convertir datos a un array de numpy
data_array = np.array(data)

# Extraer columnas relevantes
search_terms = data_array[:, 0]  # Términos de búsqueda
frequencies = data_array[:, 1].astype(int)  # Frecuencias

# Crear un índice de posición de los términos
positions = np.arange(len(frequencies))

# Calcular la correlación de Pearson
correlation, p_value = pearsonr(positions, frequencies)

# Graficar la correlación
plt.figure(figsize=(10, 6))
plt.scatter(positions, frequencies, color='orange', edgecolor='black', s=100, alpha=0.7)
plt.title('Correlación entre la Posición de los Términos de Búsqueda y su Frecuencia', fontsize=14)
plt.xlabel('Posición en la lista (índice)', fontsize=12)
plt.ylabel('Frecuencia de Búsqueda', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Añadir la línea de tendencia
plt.plot(positions, np.poly1d(np.polyfit(positions, frequencies, 1))(positions), color='red', linestyle='-', label='Línea de Tendencia')

# Mostrar el gráfico
plt.legend()
plt.tight_layout()

# Guardar gráfico en formato SVG
plt.savefig('Posicion_vs_Frecuencia_Correlacion.svg', format='svg')

plt.show()

# Mostrar los resultados de la correlación
print(f"Coeficiente de correlación (r): {correlation:.2f}")
print(f"Valor p: {p_value:.4f}")
