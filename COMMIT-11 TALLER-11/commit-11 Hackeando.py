def funcion_escalon(z):
    return 1 if z > 0 else 0 

def perceptron(entradas, pesos, sesgo):
    z = sum(x * w for x, w in zip(entradas, pesos)) + sesgo
    return funcion_escalon(z)

pesos_and = [1, 1]
sesgo_and = -1.5

print("--- Compuerta AND (codigo original) ---")
for entrada in [[1, 1], [1, 0], [0, 1], [0, 0]]:
    salida = perceptron(entrada, pesos_and, sesgo_and)
    print(f"Entrada {entrada} -> Salida: {salida}")

pesos_or = [1, 1]
sesgo_or = -0.5

print("\n--- compuerta OR (pesos y sesgos ajustados manualmente) ---")
for entrada in [[1, 1], [1, 0], [0, 1], [0, 0]]:
    salida = perceptron(entrada, pesos_or, sesgo_or)
    print(f" Entrada {entrada} -> Salida: {salida}")

print(f"\nPesos (w) encontrados: {pesos_or}")
print(f"Sesgo (b) encontrado: {sesgo_or}")