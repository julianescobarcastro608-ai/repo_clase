import numpy as np 

def centroide(x, curva):
    x = np.array(x, dtype=float)
    curva = np.array(curva, dtype=float)

    if np.sum(curva) == 0:
        raise ValueError("La suma de la curva de membresia es 0:" "no se puede calcular el centriode")

    return np.sum(x * curva) / np.sum(curva)

x_validacion = [10, 20, 30, 40]
mu_validacion = [0.2, 0.8, 0.8, 0]

resultado_validacion = centroide(x_validacion, mu_validacion)
print(f"Validacion(debe coincidir con el papel): {resultado_validacion:.4f}")

x_frenado = np.linspace(0, 100, 100)

media = 70
sigma = 10
curva_frenado = np.exp(-0.5 * ((x_frenado - media) / sigma) ** 2)

fuerza_frenado = centroide(x_frenado, curva_frenado)
print(f"Fuerza de frenado exacta calculada: {fuerza_frenado:.4f} N")