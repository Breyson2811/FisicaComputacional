def calcular_aceleracion(masa1, masa2, g):
    aceleracion = (masa1 - masa2)/(masa1+masa2)*g
    return aceleracion

def calcular_tension(masa1, masa2, g):
    tension = (2*masa1 - masa2)/(masa1+masa2)*g
    return tension

gravedad = 9.8
continuar = 1
while continuar == 1: 
    print(" \t\t Máquina de Atwood")
    masa1 = float(input("Ingrese el valor de la masa del cuerpo1 (KG): "))
    masa2 = float(input("Ingrese el valor de la masa del cuerpo2 (KG): "))

    if masa1 > masa2:
        aceleracion = calcular_aceleracion(masa1,masa2,gravedad)
        tension = calcular_tension(masa1,masa2,gravedad)
        print("El resultado de la aceleración es", aceleracion, "m/s^2")
        print("El resultado de la Tensión es", tension, "N")
    elif masa2>masa1:
        aceleracion = calcular_aceleracion(masa2,masa1,gravedad)
        tension = calcular_tension(masa2,masa1,gravedad)
        print("El resultado de la aceleración es", aceleracion, "m/s^2")
        print("El resultado de la Tensión es", tension, "N")
    else:
        print("El resultado de la aceleración es 0", "m/s^2")
        tension = masa1 * gravedad
        print("El resultado de la Tensión es", tension, "N")
    
    continuar = float(input("Ingrese (1) si quiere volver a calcular, Ingrese cualquier digito si desea salir:  "))
