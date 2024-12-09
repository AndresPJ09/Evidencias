import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Crear el dataframe con los datos proporcionados
data = {
    "Rank": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "DBMS": ["Oracle", "MySQL", "Microsoft SQL Server", "PostgreSQL", "MongoDB", "Redis", "Snowflake", "Elasticsearch", "IBM Db2", "SQLite"],
    "Database Model": ["Relational", "Relational", "Relational", "Relational", "Document", "Key-value", "Relational", "Search engine", "Relational", "Relational"],
    "Score Sep 2024": [1286.59, 1029.49, 807.76, 644.36, 410.24, 149.43, 133.72, 128.79, 123.05, 103.35],
    "Aug 2024": [28.11, 2.63, -7.41, 6.97, -10.74, -3.28, -2.25, -1.04, 0.04, -1.44],
    "Sep 2023": [45.72, -82.00, -94.45, 23.61, -29.18, -14.26, 12.83, -10.20, -13.67, -25.85]
}

df = pd.DataFrame(data)

# Correlación entre las columnas numéricas
correlation_matrix = df[["Score Sep 2024", "Aug 2024", "Sep 2023"]].corr()

# Visualización de la matriz de correlación
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("Matriz de Correlación")
plt.show()

# Definir X y y para aplicar la regresión lineal
X = df[["Aug 2024", "Sep 2023"]]  # Variables predictoras
y = df["Score Sep 2024"]  # Variable dependiente

# Crear el modelo de regresión lineal
model = LinearRegression()
model.fit(X, y)

# Realizar las predicciones
y_pred = model.predict(X)

# Evaluar el modelo
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

# Visualizar los resultados de la regresión
plt.figure(figsize=(8, 6))
plt.scatter(y, y_pred, color='blue', label='Datos reales vs Predicciones')
plt.plot([min(y), max(y)], [min(y), max(y)], color='red', linestyle='--', label='Linea de ajuste')
plt.xlabel("Valores reales (Score Sep 2024)")
plt.ylabel("Predicciones")
plt.title("Regresión Lineal: Score Sep 2024 vs Aug 2024 & Sep 2023")
plt.legend()
plt.show()

# Mostrar los coeficientes del modelo y el desempeño
coef = model.coef_
intercept = model.intercept_

coef, intercept, mse, r2
