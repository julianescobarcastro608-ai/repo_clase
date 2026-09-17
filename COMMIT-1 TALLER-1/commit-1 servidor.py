servidor_estado = {
    "cpu_uso": 85,
    "memoria_libre": 20,
    "ping_respuesta": 150,
    "temperatura": 75,
    "ventilador": True
}

def diagnosticar_servicio(hechos):
    if hechos["temperatura"] > 80 and not hechos["ventilador"]:
        return "CRITICO: temperatura muy alta y ventilador apagado"
    elif hechos["cpu_uso"] > 90 and hechos["memoria_libre"] < 15:
        return "CRITICO: uso excesivo de cpu y poca memoria disponible"
    elif hechos["cpu_uso"] >80 or hechos["ping_respuesta"] > 100:
        return "ADVERTENCIA: el servidor presenta un rendimiento elevado o respuesta lenta"
    elif hechos["cpu_uso"] <= 80 and hechos["memoria_libre"] >20:
        return "NORMAL: el servidor funciona correctamente"
    else:
        return "EN REVISION: no se puede determinar un estado especifico"

diagnostico = diagnosticar_servicio(servidor_estado)

print("Diagnostico del servicio:")
print(diagnostico)

print("\n cambiando valores para probar otra regla")
servidor_estado["temperatura"] = 90
servidor_estado["ventilador"] = False

diagnostico = diagnosticar_servicio(servidor_estado)
print(diagnostico)