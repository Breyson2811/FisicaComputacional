def calcular_velocidad_final(velocidad_inicial, aceleracion, tiempo):
    return velocidad_inicial + (aceleracion * tiempo)

def calcular_velocidad_inicial(velocidad_final, aceleracion, tiempo):
    if tiempo > 0:
        return velocidad_final - (aceleracion * tiempo)
    else:
        print("El valor del tiempo es un valor no válido.")
        return None

def calcular_aceleracion(velocidad_inicial, velocidad_final, tiempo):
    if tiempo > 0:
        return (velocidad_final - velocidad_inicial) / tiempo
    else:
        print("El valor del tiempo es un valor no válido.")
        return None

def calcular_tiempo(velocidad_inicial, velocidad_final, aceleracion):
    if aceleracion != 0:
        return (velocidad_final - velocidad_inicial) / aceleracion
    else:
        print("La aceleración no puede ser cero.")
        return None

while True:
    option = input("¿Qué desea calcular? 1: VelocidadFinal - 2: VelocidadInicial - 3: Aceleracion - 4: Tiempo - 5: Salir\n")
    if option == '5':
        break

    option = int(option)

    if option not in [1, 2, 3, 4]:
        print("Seleccione una opción válida (1 - 2 - 3 - 4).")
        continue

    if option == 1:
        velocidad_inicial = float(input("Ingrese el valor de la velocidad inicial (m/s): "))
        aceleracion = float(input("Ingrese el valor de la aceleración (m/s^2): "))
        tiempo = float(input("Ingrese el valor del tiempo (s): "))
        velocidad_final = calcular_velocidad_final(velocidad_inicial, aceleracion, tiempo)
        print("El resultado de la velocidad final es", velocidad_final, "m/s")
    elif option == 2:
        velocidad_final = float(input("Ingrese el valor de la velocidad final (m/s): "))
        aceleracion = float(input("Ingrese el valor de la aceleración (m/s^2): "))
        tiempo = float(input("Ingrese el valor del tiempo (s): "))
        velocidad_inicial = calcular_velocidad_inicial(velocidad_final, aceleracion, tiempo)
        if velocidad_inicial is not None:
            print("El resultado de la velocidad inicial es", velocidad_inicial, "m/s")
    elif option == 3:
        velocidad_inicial = float(input("Ingrese el valor de la velocidad inicial (m/s): "))
        velocidad_final = float(input("Ingrese el valor de la velocidad final (m/s): "))
        tiempo = float(input("Ingrese el valor del tiempo (s): "))
        aceleracion = calcular_aceleracion(velocidad_inicial, velocidad_final, tiempo)
        if aceleracion is not None:
            print("El resultado de la aceleración es", aceleracion, "m/s^2")
    elif option == 4:
        velocidad_inicial = float(input("Ingrese el valor de la velocidad inicial (m/s): "))
        velocidad_final = float(input("Ingrese el valor de la velocidad final (m/s): "))
        aceleracion = float(input("Ingrese el valor de la aceleración (m/s^2): "))
        tiempo = calcular_tiempo(velocidad_inicial, velocidad_final, aceleracion)
        if tiempo is not None:
            print("El resultado del tiempo es", tiempo, "s")
