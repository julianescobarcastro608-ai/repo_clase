variables = {
    "desempeno_pobre": 0.1,
    "desempeno_promedio": 0.4,
    "desempeno_excelente": 0.85,
    "antiguedad_corta": 0.2,
    "antiguedad_media": 0.5,
    "antiguedad_larga": 0.6,
}

def motor_bonos(v):
    bono_bajo = max(v["desempeno_pobre"], v["antiguedad_corta"])
    bono_medio = v["desempeno_promedio"]
    bono_alto = min(v["desempeno_excelente"], v["antiguedad_larga"])
    return{
        "Bono Bajo": bono_bajo,
        "Bono Media": bono_medio,
        "Bono Alto": bono_alto,
    }

resultado = motor_bonos(variables)

print("niveles de activacion:")
for nivel, grado in resultado.items():
    print(f"{nivel:10s}: {grado:3f}")

fuerza_regla_a = 0.4
fuerza_regla_b = 0.7
fuerza_final_bono_alto = max(fuerza_regla_a, fuerza_regla_b)

print(f"\nFuerza final agregada para 'bono alto' {fuerza_final_bono_alto}")