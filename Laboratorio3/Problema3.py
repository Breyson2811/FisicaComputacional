import math
def Unidades():
  print('NOTA\nConsiderar para el ingreso de datos :')
  print('Frecuencia angular, w : en radianes por segundo (rad/s)')
  print('Tiempo, t : en segundos(s)')
  print('Carga, Q : en culombios (µ)')
  print('Inductancia, L : en henrios (H)')
  print('Capacitancia, C : en faradios (F)')
  print('Resistencia, R : en ohmios (Ω)\n')

def verificarNegativo(x):   
   if (x<0):
    x1 = float(input('El valor ingresado no puede ser negativo, vuelva a ingresar otro valor : '))
    return x1
   else: 
    return x
   
def circuitoLC():
  L = float(input('Ingrese la inductancia L en henrios: '))
  C = float(input('Ingrese la capacitancia C en faradios : '))
  Qi = float(input('Ingrese la Carga inicial en culombios: '))
  t = float(input('Ingrese el tiempo en segundos : '))
  t = verificarNegativo(t)
  phi = float(input('Ingrese la fase en grados : '))

  w = 1 / math.sqrt(L * C)
  Carga = Qi * math.sin(math.radians((w * t) + phi))
  print('La carga en el tiempo', t, 'segundos es:', round(Carga,2), ' µ')

def circuitoLCR():
  L = float(input('Ingrese la inductancia L en henrios: '))
  C = float(input('Ingrese la capacitancia C en faradios : '))
  R = float(input('Ingrese la resistencia R en ohmios : '))
  Qi = float(input('Ingrese la Carga inicial en culombios: '))
  t = float(input('Ingrese el tiempo en segundos : '))
  t = verificarNegativo(t)
  phi = float(input('Ingrese la fase en grados : '))

  gamma = R / (2 * L)
  w = 1 / math.sqrt(L * C)
  Carga = (Qi * math.exp(-gamma * t) * math.sin(math.radians(w * t + phi)))
  print('La carga en el tiempo', t, 'segundos es:', round(Carga,2), ' µ')
  
#main
Unidades()
continuar = 1
while continuar == 1:
  print('1: Circuito LC\n2: Circuito LCR\n')
  option = int(input('Elige una opción : '))
  if (option == 1):
    print('----CIRCUITO LC---\n')
    Unidades()
    circuitoLC()
  if (option == 2):
    print('----CIRCUITO LCR---\n')
    Unidades()
    circuitoLCR()
  else:
    print('Ingrese una opción correcta ')
  continuar = int(input('Ingrese 1 si desea continuar, caso contrario ingrese cualquier otro valor\n'))
