def calcular_corriente_total():
    # Solicitar al usuario el valor de la primera fuente de voltaje
    v1 = float(input("Ingrese el valor de la primera fuente de voltaje (en volts): "))

    # Solicitar al usuario el valor de la segunda fuente de voltaje
    v2 = float(input("Ingrese el valor de la segunda fuente de voltaje (en volts): "))

    # Solicitar al usuario el valor de la resistencia en kohms
    resistencia = float(input("Ingrese el valor de la resistencia (en kohms): "))

    # Calcular el voltaje total sumando las fuentes
    voltaje_total = v1 + v2

    # Convertir la resistencia a ohms
    resistencia_ohms = resistencia

    # Calcular la corriente total utilizando la ley de Ohm (I = V / R)
    corriente_total = voltaje_total / resistencia_ohms

    # Mostrar el resultado
    print(f"El voltaje total del circuito es: {voltaje_total} volts")
    print(f"La corriente total aportada por las dos fuentes es: {corriente_total} amperios")

# Llamar a la función para calcular la corriente total
calcular_corriente_total()
