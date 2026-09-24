import numpy as np

def sigmoide(z):
    return 1 / (1 + np.exp(-z))

X =  np.array([[0.5, 0.8, 0.2]])

W1 = np.array([
    [0.4],
    [0.6],
    [-0.2],
])
b1 = 0.1  

Z1 = np.dot(X, W1) + b1
A1 = sigmoide(Z1)  
print("--- 1 solo un cliente---")
print("Z1 (Valor puro antes de la sigmoide):\n", Z1)
print("A1 (probabilidad despues de la sigmoide):\n", A1)

X_lote = np.array([
    [0.5, 0.8, 0.2],
    [0.1, 0.9, 0.9],
])

Z1_lote = np.dot(X_lote, W1) + b1
A1_lote = sigmoide(Z1_lote)

print("\n--- 3 y 4. Dos clientes en lote (batch) ---")
print("Z1 (valores puros para ambos clientes):\n", Z1_lote)
print("A1 (probabilidades para ambos clientes):\n", A1_lote)