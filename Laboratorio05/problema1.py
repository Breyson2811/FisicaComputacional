def calcular_corriente_total():
    # Solicitar al usuario la cantidad de resistencias
    num_resistencias = int(input("Ingrese la cantidad de resistencias en serie: "))

    # Solicitar al usuario el valor de la fuente de voltaje
    voltaje_fuente = float(input("Ingrese el valor de la fuente de voltaje (en volts): "))

    # Inicializar la suma de las resistencias
    suma_resistencias = 0

    # Solicitar al usuario los valores de cada resistencia y sumarlos
    for i in range(1, num_resistencias + 1):
        resistencia = float(input(f"Ingrese el valor de la resistencia {i} (en ohms): "))
        suma_resistencias += resistencia

    # Calcular la corriente total utilizando la ley de Ohm (I = V / R)
    corriente_total = voltaje_fuente / suma_resistencias

    # Mostrar el resultado
    print(f"La corriente total en el circuito es: {corriente_total} amperios")

# Llamar a la función para calcular la corriente total
calcular_corriente_total()
