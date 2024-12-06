import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Datos en formato de lista
data2 = [
    [1995, 17, 31, 53],
    [2000, 28, 23, 49],
    [2005, 35, 19, 53],
    [2010, 37, 21, 42],
    [2015, 29, 19, 52]
]

# Convertir datos a un array de numpy
data_array2 = np.array(data2)

# Extraer columnas relevantes
years2 = data_array2[:, 0]  # Años
successes = data_array2[:, 1]  # Éxitos
failures = data_array2[:, 2]  # Fracasos
underestimates = data_array2[:, 3]  # Sub-estimados

# Calcular la correlación de Pearson entre éxitos y fracasos
corr_success_fail, p_value_success_fail = pearsonr(successes, failures)

# Calcular la correlación de Pearson entre éxitos y sub-estimados
corr_success_under, p_value_success_under = pearsonr(successes, underestimates)

# Crear gráficos de dispersión (scatter plots) con líneas de mejor ajuste (regresión)
plt.figure(figsize=(14, 6))

# Subgráfico 1: Correlación entre éxitos y fracasos
plt.subplot(1, 2, 1)
plt.scatter(successes, failures, color='red', label='Fracasos vs Éxitos')
plt.plot(np.unique(successes), np.poly1d(np.polyfit(successes, failures, 1))(np.unique(successes)), color='blue', label='Línea de mejor ajuste')
plt.title(f"Correlación entre Éxitos y Fracasos\nCorrelación = {corr_success_fail:.2f}, p-value = {p_value_success_fail:.4f}")
plt.xlabel('Éxitos')
plt.ylabel('Fracasos')
plt.grid(True)
plt.legend()

# Subgráfico 2: Correlación entre éxitos y sub-estimados
plt.subplot(1, 2, 2)
plt.scatter(successes, underestimates, color='green', label='Sub-estimados vs Éxitos')
plt.plot(np.unique(successes), np.poly1d(np.polyfit(successes, underestimates, 1))(np.unique(successes)), color='blue', label='Línea de mejor ajuste')
plt.title(f"Correlación entre Éxitos y Sub-estimados\nCorrelación = {corr_success_under:.2f}, p-value = {p_value_success_under:.4f}")
plt.xlabel('Éxitos')
plt.ylabel('Sub-estimados')
plt.grid(True)
plt.legend()

# Mostrar gráficos
plt.tight_layout()
plt.show()

# Mostrar las hipótesis de correlación
if p_value_success_fail < 0.05:
    print(f"Hipótesis para Éxitos y Fracasos: Existe una correlación significativa entre éxitos y fracasos.")
else:
    print(f"Hipótesis para Éxitos y Fracasos: No existe una correlación significativa entre éxitos y fracasos.")

if p_value_success_under < 0.05:
    print(f"Hipótesis para Éxitos y Sub-estimados: Existe una correlación significativa entre éxitos y sub-estimados.")
else:
    print(f"Hipótesis para Éxitos y Sub-estimados: No existe una correlación significativa entre éxitos y sub-estimados.")
