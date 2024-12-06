import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Datos en formato de lista
data = [
    ['Python', 1],
    ['Java', 0.4855],
    ['JavaScript', 0.4451],
    ['C++', 0.3749],
    ['TypeScript', 0.2497],
    ['SQL', 0.2258],
    ['C#', 0.2089],
    ['Go', 0.2052],
    ['C', 0.1989],
    ['HTML', 0.1817],
    ['Rust', 0.1506],
    ['Mathematica', 0.1275],
    ['PHP', 0.1196],
    ['Shell', 0.117],
    ['Lua', 0.1041],
    ['SAS', 0.0855]
]

# Extraer datos
languages = np.array([item[0] for item in data])  # Lenguajes
popularity = np.array([item[1] for item in data])  # Popularidad
indices = np.arange(1, len(popularity) + 1)  # Índices 1 a N

# Calcular correlación de Pearson
correlation, p_value = pearsonr(indices, popularity)

# Gráfica de correlación "vs"
plt.figure(figsize=(12, 8))
plt.scatter(indices, popularity, color='orange', edgecolor='black', s=100, alpha=0.8, label='Datos')
plt.plot(indices, np.polyval(np.polyfit(indices, popularity, 1), indices), 
         color='blue', linestyle='--', label='Tendencia (Regresión lineal)')

# Añadir etiquetas de lenguajes
for i, lang in enumerate(languages):
    plt.annotate(lang, (indices[i], popularity[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9)

# Etiquetas y estilo
plt.title('Correlación entre Índice y Popularidad de Lenguajes', fontsize=16)
plt.xlabel('Índice de Popularidad (Posición)', fontsize=12)
plt.ylabel('Popularidad (%)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(np.mean(popularity), color='red', linestyle='--', label='Promedio de Popularidad')
plt.legend()

# Guardar y mostrar gráfica
plt.tight_layout()
plt.savefig('Correlacion_Indice_vs_Popularidad.svg', format='svg')
plt.show()

# Hipótesis
print(f"Hipótesis:\n"
      f"H0: No existe una correlación significativa entre la posición en el índice y el porcentaje de popularidad.\n"
      f"H1: Existe una correlación significativa entre la posición en el índice y el porcentaje de popularidad.\n\n"
      f"Coeficiente de correlación de Pearson: {correlation:.2f}\n"
      f"Valor p: {p_value:.4f}")
