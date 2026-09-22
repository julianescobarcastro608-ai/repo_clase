import numpy as np 
from sklearn.svm import SVC

X = np.array([
    [1, 1],
    [2, 1],
    [1, 2],
    [4, 4],
    [5, 4],
    [4, 5],
    [6, 5],
    [5, 6],
    [6, 6],
])

Y =  np.array([0, 0, 0, 1, 1, 1, 1, 1, 1])
modelo_lineal = SVC(kernel='linear')
modelo_lineal.fit(X, Y)

print("--- moodelo con kernel='linear' ---")
print("Vectores de soporte (indices):", modelo_lineal.support_)
print("Vectores de soporte (coordenadas): \n", modelo_lineal.support_vectors_)

X = np.vstack([X, [5, 5]])
Y = np.append(Y, 0)

modelo_lineal_2 = SVC(kernel='linear')
modelo_lineal_2.fit(X, Y)

nuevo_punto = np.array([[5, 5]])
prediccion_lineal = modelo_lineal_2.predict(nuevo_punto)

print("\n modelo LINEAL re entrenado (con punto [5,5] = Clase A) ---")
print("Vectores de soporte (coordenadas):\n", modelo_lineal_2.support_vectors_)
print("Prediccion para [5,5]:", prediccion_lineal[0], "(esperado: 0, Clase A)")
print("Presicion sobre el proposito de dataset de entrenamiento:", modelo_lineal_2.score(X, Y))

modelo_rbf = SVC(kernel='rbf', gamma=2)
modelo_rbf.fit(X, Y)
prediccion_rbf = modelo_rbf.predict(nuevo_punto)

print("\n--- Modelo con Kernel='rbf' ---")
print("Vectores de soporte (coordenadas):\n", modelo_rbf.support_vectors_)
print("Prediccion para [5,5]:", prediccion_rbf[0], "(esperado: 0, Clase A)")
print("Precision sobre el propioo dataset de entyrenamiento:", modelo_rbf.score(X, Y))