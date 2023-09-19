def calcular_distancia(velocidad, tiempo):
    return velocidad * tiempo

def calcular_velocidad(distancia, tiempo):
    if tiempo > 0:
        return distancia / tiempo
    else:
        print("El valor del tiempo es un valor no válido.")
        return None

def calcular_tiempo(distancia, velocidad):
    if velocidad > 0:
        return distancia / velocidad
    else:
        print("El valor de la velocidad es un valor no válido.")
        return None

while True:
    option = input("¿Qué desea calcular? 1: Distancia - 2: Velocidad - 3: Tiempo - 4: Salir\n")
    if option == '4':
        break

    option = int(option)

    if option not in [1, 2, 3]:
        print("Seleccione una opción válida (1 - 2 - 3).")
        continue

    if option == 1:
        velocidad_m_s = float(input("Ingrese el valor de la velocidad (m/s): "))
        tiempo_s = float(input("Ingrese el valor del tiempo (s): "))
        distancia_m = calcular_distancia(velocidad_m_s, tiempo_s)
        print("El resultado de la distancia es", distancia_m, "metros")
    elif option == 2:
        distancia_m = float(input("Ingrese el valor de la distancia (metros): "))
        tiempo_s = float(input("Ingrese el valor del tiempo (s): "))
        velocidad_m_s = calcular_velocidad(distancia_m, tiempo_s)
        if velocidad_m_s is not None:
            print("El resultado de la velocidad es", velocidad_m_s, "m/s")
    elif option == 3:
        distancia_m = float(input("Ingrese el valor de la distancia (metros): "))
        velocidad_m_s = float(input("Ingrese el valor de la velocidad (m/s): "))
        tiempo_s = calcular_tiempo(distancia_m, velocidad_m_s)
        if tiempo_s is not None:
            print("El resultado del tiempo es", tiempo_s, "segundos")
