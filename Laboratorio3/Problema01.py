def Unidades():
  print('NOTA\nConsiderar para el ingreso de datos :')
  print('Elongación, x: en metros (m)')
  print('Amplitud, A : en metros (m)')
  print('Frecuencia, f : en Hertz (Hz)')
  print('Periodo, T : en segundos (s)')
  print('Frecuencia angular, w : en radianes por segundo (rad/s)')
  print('Tiempo, t : en segundos(s)')
  print('Velocidad, v : metros por segundo al cuadrado (m/s²)')
  print('Masa, m : en kilogramos (Kg)\n')

def verificarNegativo(x):   
   if (x<0):
    x1 = float(input('El valor ingresado no puede ser negativo, vuelva a ingresar otro valor : '))
    return x1
   else: 
    return x

def MAS():
  A = float (input('Ingrese la amplitud en metros : '))
  ti = float (input('Ingrese el tiempo inicial en segundos : '))
  ti = verificarNegativo(ti)
  tf = float (input('Ingrese el tiempo final en segundos : '))
  tf = verificarNegativo(tf)
  w = float (input('Ingrese la frecuencia  angular en rad/s : '))
  phi = float(input('Ingrese la fase en grados: '))
  velocidad_max = w * A
  aceleracion_max = pow(w, 2) * A
  print('----RESULTADOS---\n')
  print('La velocidad máxima es : ', round(velocidad_max, 2), ' m/s')
  print('La aceleración máxima es : ', round(aceleracion_max, 2), ' m/s²\n')

#main
print('----MOVIMIENTO ARMÓNICO SIMPLE---\n')
Unidades()
continuar = 1
while continuar == 1:
  MAS()
  continuar = int(input('Ingrese 1 si desea continuar, caso contrario ingrese cualquier otro valor\n'))
