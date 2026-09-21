import numpy as np 
from sklearn.neighbors import KNeighborsClassifier

X_entrenamiento = np.array([
    [20, 30],
    [40, 50],
    [35, 45]
])

Y_entrenamiento = np.array([0, 1, 1])
nombres = ["A", "B", "C"]
nuevo_cliente = np.array([[30, 40]])

print("Distancias Eucludianas:")
for nombre, punto in zip(nombres, X_entrenamiento):
    distancia = np.sqrt(np.sum((nuevo_cliente[0] - punto) **2))
    print(f"Hasta{nombre} ({int(punto[0])}, {int(punto[1])}): {distancia:.3f}")

modelo_k1 = KNeighborsClassifier(n_neighbors=1)
modelo_k1.fit(X_entrenamiento, Y_entrenamiento)
prediccion_k1 = modelo_k1.predict(nuevo_cliente)
print(f"\nK = 1 -> Clase predicha: {prediccion_k1[0]}" f"({'COMPRA' if prediccion_k1[0] == 1 else 'NO COMPRA'})")

modelo_k3 = KNeighborsClassifier(n_neighbors=3)
modelo_k3.fit(X_entrenamiento, Y_entrenamiento)
prediccion_k3 = modelo_k3.predict(nuevo_cliente)
print(f"K = 3 -> Clase predicha: {prediccion_k3[0]}" f"({'COMPRA' if prediccion_k3[0] == 1 else 'NO COMPRA'})")

if prediccion_k1[0] == prediccion_k3[0]:
    print("\n No hubo cambio en la decision de pasar de K=1 a K=3.")
else:
    print("\n Si hubo cambio en la decision de passar de K=1 a K=3")