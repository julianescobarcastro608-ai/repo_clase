hechos = {
    "monto": 6000,
    "pais_extranjero": True
}

reglas = [
    {"id": "R1",
    "condiciones": {"monto": (">", 5000)},
    "conclusion": {"transaccion_inusual": True}},

    {"id": "R2",
    "condiciones": {"transaccion_inusual": True, "Pais_extranjero": True},
    "conclusion": {"bloquear_tarjeta": True}},

    {"id": "R3",
    "condiciones": {"bloquear_tarjeta": True},
    "conclusion": {"notificar_cliente"}},

    {"id": "R4",
    "condiciones": {"bloquear_tarjeta": True},
    "conclusion": {"alerta_equipo_segurida": True}},
]

def condicion_cumplida(hechos, clave, valor_esperado):
    valor_actual = hechos.get(clave)

    if isinstance(valor_esperado, tuple):
        operador, valor_comparar = valor_esperado
        if valor_actual is None:
            return False
        if operador == ">":
            return valor_actual > valor_comparar
        elif operador == "<":
            return valor_actual < valor_comparar
        elif operador == ">=":
            return valor_actual >= valor_comparar
        elif operador == "<=":
            return valor_actual <= valor_comparar
        elif operador == "==":
            return valor_actual == valor_comparar
        else:
            raise ValueError(f"Operador no soportado: {operador}")
    else:
        return valor_actual == valor_esperado

nuevos_hechos = True
while nuevos_hechos:
    nuevos_hechos = False
    for regla in reglas:
        condiciones_cumplidas = all(
            condicion_cumplida(hechos, k, v) for k, v in regla["condiciones"].items()
        )

        if condiciones_cumplidas:
            for clave, valor in regla["conclusion"].items():
                if clave not in hechos:
                    hechos[clave] = valor
                    nuevos_hechos = True 
                    print(f"disparando {regla['id']} -> Nuevo Hecho: {clave}={valor}")

print("\nMemoria final:", hechos)