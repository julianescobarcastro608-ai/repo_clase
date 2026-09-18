def membresia_triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)

conjuntos = {
    "Novato": (0, 0, 5),
    "Intermedio": (2, 5, 8),
    "Experto": (5, 10, 20),
}

conductores = [3, 6, 12]

for ano in conductores:
    print(f"\nconductor con años de experiencia:")

    grados = {}
    for categoria, (a, b, c) in conjuntos.items():
        grado = membresia_triangular(ano, a, b, c)
        grados[categoria] = grado
        print(f"{categoria:10s}: {grado:.3f}")

    categoria_mejor = max(grados, key=grados.get)
    print(f" --> Categoria Dominante: {categoria_mejor}"
          f"(grado ={grados[categoria_mejor]:.3f})")
    