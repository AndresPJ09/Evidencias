import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Datos de preocupaciones
concerns = np.array([
    'User data collection', 
    'Skill shifts in the workforce', 
    'Job displacement', 
    'Existential risks', 
    'User accessibility', 
    'Perpetuating bias', 
    'Other'
])

counts = np.array([161, 155, 150, 136, 135, 118, 6])
percent_cases = np.array([44.4, 42.7, 41.3, 37.5, 37.2, 32.5, 1.7])

# Función para graficar y calcular correlación
def plot_correlation(x, y, title):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x, y=y, color='blue', s=100)
    sns.regplot(x=x, y=y, scatter=False, color='red', line_kws={"linewidth": 2})
    plt.title(title)
    plt.xlabel('Número de Casos')
    plt.ylabel('Porcentaje de Casos')
    plt.grid(True)
    plt.tight_layout()
    
    # Calcular coeficiente de correlación
    correlation = np.corrcoef(x, y)[0, 1]
    print(f'Coeficiente de correlación entre {title}: {correlation:.2f}')
    
    plt.show()

# Graficar la correlación
plot_correlation(counts, percent_cases, 'Relación entre Número de Casos y Porcentaje de Casos')
