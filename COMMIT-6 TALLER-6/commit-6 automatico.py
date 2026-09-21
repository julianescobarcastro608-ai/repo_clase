import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text

X = np.array([
    [22, 5, 3],
    [25, 4, 2],
    [19, 6, 1],
    [30, 3, 2],
    [45, 1, 0],
    [50, 0, 0],
    [60, 1, 0], 
    [35, 0, 1],
    [23, 5, 0],
    [55, 2, 1],
])

Y = np.array([1, 1, 1, 1, 0, 0, 0, 0, 1, 0])
nombres_columnas = ["Edad", "Hooras_Online", "Compras_previas"]
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X, Y)

reglas = export_text(modelo, feature_names=nombres_columnas)
print("Base de conocimiento generada por el arbol de decision:\n")
print(reglas)

precision = modelo.score(X, Y)
print(f"Presicion sobre el set de entrenamiento: {precision:.2%}")