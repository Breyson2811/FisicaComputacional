def calcular_corriente_individual(voltaje_fuente, resistencias):
    # Paso 1: Calcular corrientes individuales
    corrientes_individuales = [voltaje_fuente / resistencia for resistencia in resistencias]

    # Paso 2: Calcular corriente total sumando las corrientes individuales
    corriente_total = sum(corrientes_individuales)

    return corrientes_individuales, corriente_total

def calcular_corriente_total(resistencias):
    # Paso 1: Calcular la resistencia total en paralelo
    resistencia_total = 1 / sum(1 / resistencia for resistencia in resistencias)

    # Paso 2: Calcular la corriente total utilizando la ley de Ohm
    corriente_total = voltaje_fuente / resistencia_total

    return resistencia_total, corriente_total

# Solicitar al usuario el valor de la fuente de voltaje
voltaje_fuente = float(input("Ingrese el valor de la fuente de voltaje (en volts): "))

# Solicitar al usuario la cantidad de resistencias en paralelo y sus valores
num_resistencias = int(input("Ingrese la cantidad de resistencias en paralelo: "))
resistencias_paralelo = [float(input(f"Ingrese el valor de la resistencia {i} (en ohms): ")) for i in range(1, num_resistencias + 1)]

# Calcular corriente total y resistencia total utilizando ambos métodos
corrientes_individuales, corriente_total_metodo1 = calcular_corriente_individual(voltaje_fuente, resistencias_paralelo)
resistencia_total_metodo2, corriente_total_metodo2 = calcular_corriente_total(resistencias_paralelo)

# Mostrar resultados
print("Resultados del 1er Método (Calculando corrientes individuales):")
for i, corriente_individual in enumerate(corrientes_individuales, 1):
    print(f"Corriente en la rama {i}: {corriente_individual} amperios")

print(f"Corriente total en el circuito: {corriente_total_metodo1} amperios")

print("\nResultados del 2do Método (Calculando resistencia total):")
print(f"Resistencia total en paralelo: {resistencia_total_metodo2} ohms")
print(f"Corriente total en el circuito: {corriente_total_metodo2} amperios")
