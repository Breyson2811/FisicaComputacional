def calcular_distancia(velocidad_inicial, tiempo, aceleracion):
    return (velocidad_inicial * tiempo) + (0.5 * aceleracion * tiempo ** 2)

def calcular_velocidad_inicial(distancia, tiempo, aceleracion):
    if tiempo > 0:
        return (distancia - (0.5 * aceleracion * tiempo ** 2)) / tiempo
    else:
        print("El valor del tiempo es un valor no válido.")
        return None

def calcular_aceleracion(distancia, velocidad_inicial, tiempo):
    if tiempo > 0:
        return (2 * (distancia - (velocidad_inicial * tiempo))) / (tiempo ** 2)
    else:
        print("El valor del tiempo es un valor no válido.")
        return None
while True:
    option = input("¿Qué desea calcular? 1: Distancia - 2: VelocidadInicial - 3: Aceleracion - 4:Salir\n")
    if option == '4':
        break

    option = int(option)

    if option not in [1, 2, 3]:
        print("Seleccione una opción válida (1 - 2 - 3).")
        continue

    if option == 1:
        velocidad_inicial = float(input("Ingrese el valor de la velocidad inicial (m/s): "))
        tiempo = float(input("Ingrese el valor del tiempo (s): "))
        aceleracion = float(input("Ingrese el valor de la aceleración (m/s^2): "))
        distancia = calcular_distancia(velocidad_inicial, tiempo, aceleracion)
        print("El resultado de la distancia es", distancia, "metros")
    elif option == 2:
        distancia = float(input("Ingrese el valor de la distancia (metros): "))
        tiempo = float(input("Ingrese el valor del tiempo (s): "))
        aceleracion = float(input("Ingrese el valor de la aceleración (m/s^2): "))
        velocidad_inicial = calcular_velocidad_inicial(distancia, tiempo, aceleracion)
        if velocidad_inicial is not None:
            print("El resultado de la velocidad inicial es", velocidad_inicial, "m/s")
    elif option == 3:
        distancia = float(input("Ingrese el valor de la distancia (metros): "))
        velocidad_inicial = float(input("Ingrese el valor de la velocidad inicial (m/s): "))
        tiempo = float(input("Ingrese el valor del tiempo (s): "))
        aceleracion = calcular_aceleracion(distancia, velocidad_inicial, tiempo)
        if aceleracion is not None:
            print("El resultado de la aceleración es", aceleracion, "m/s^2")
