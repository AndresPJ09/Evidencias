import numpy as np
import matplotlib.pyplot as plt

# Datos de los lenguajes de programación
rankings = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
languages = np.array(['C', 'Java', 'Python', 'C++', 'C#', 'Visual Basic', 'JavaScript', 'PHP', 'Assembly Language', 'SQL'])
ratings = np.array([11.62, 11.17, 10.95, 8.01, 4.83, 4.50, 2.71, 2.58, 2.40, 1.53])
change = np.array([-4.83, -3.93, +1.86, +1.80, -0.42, -0.73, +0.23, +0.68, +1.46, +0.13])

# Función para graficar correlación entre ratings y cambio
def plot_correlation():
    plt.figure(figsize=(10, 6))
    plt.scatter(ratings, change, color='blue')
    
    # Añadir una línea de tendencia (regresión lineal)
    m, b = np.polyfit(ratings, change, 1)
    plt.plot(ratings, m*ratings + b, color='red', linestyle='--')
    
    plt.title('Correlación entre Ratings de Lenguajes de Programación y su Cambio de Ranking (Jul-21)')
    plt.xlabel('Ratings (%)')
    plt.ylabel('Cambio en el Ranking')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('correlation_ratings_change.svg', format='svg')
    plt.show()

# Graficar la correlación
plot_correlation()
