  1 import numpy as np
  2 
  3 # Entrada de datos desde la consola para el tamaño del tablero
  4 filas = int(input('Ingrese el número de filas del tablero: '))
  5 columnas = int(input('Ingrese el número de columnas del tablero: '))
  6 
  7 # Crear tablero
  8 ti = np.zeros((filas, columnas))
  9 
 10 # Función para encender una casilla específica
 11 def encender_casilla(i, j):
 12     ti[i, j] = 1
 13 
 14 def update():
 15   tn = np.zeros((filas, columnas))
 16   for i in range (filas):
 17     for j in range (columnas):
 18       #regla de selección
 19       if(ti[i,(j-1)%columnas] == 0 and ti[i, j] == 0 and ti[i, (j+1)%columnas] == 0):
 20         tn[(i+1)%filas, j] = 0 #000 = 0
 21       elif(ti[i,(j-1)%columnas] == 0 and ti[i, j] == 0 and ti[i, (j+1)%columnas] == 1):
 22         tn[(i+1)%filas, j] = 1 #001 = 1
 23       elif(ti[i,(j-1)%columnas] == 0 and ti[i, j] == 1 and ti[i, (j+1)%columnas] == 0):
 24         tn[(i+1)%filas, j] = 1 #010 = 1
 25       elif(ti[i,(j-1)%columnas] == 0 and ti[i, j] == 1 and ti[i, (j+1)%columnas] == 1):
 26         tn[(i+1)%filas, j] = 1 #011 = 1
 27       elif(ti[i,(j-1)%columnas] == 1 and ti[i, j] == 0 and ti[i, (j+1)%columnas] == 0):
 28         tn[(i+1)%filas, j] = 1 #100 = 1
 29       elif(ti[i,(j-1)%columnas] == 1 and ti[i, j] == 0 and ti[i, (j+1)%columnas] == 1):
 30         tn[(i+1)%filas, j] = 0 #101 = 0
 31       elif(ti[i,(j-1)%columnas] == 1 and ti[i, j] == 1 and ti[i, (j+1)%columnas] == 0):
 32         tn[(i+1)%filas, j] = 0 #110 = 0
 33       else:
 34         tn[(i+1)%filas, j] = 0 #111 = 0
 35   #copiamos las celdas vivas de la matriz anterior a la matriz nueva
 36   tn[ti == 1] = 1
 37 
 38   return tn
 39 
 40 # Función para mostrar el tablero
 41 def mostrar_tablero():
 42     for i in range(filas):
 43         for j in range(columnas):
 44             if ti[i, j] == 1:
 45                 print('◉ ', end=' ')
 46             else:
 47                 print('◯ ', end=' ')
 48         print()
 49 
 50 # Entrada de datos desde la consola para encender una casilla específica
 51 i = int(input('Ingrese la coordenada i para encender una casilla: '))-1
 52 j = int(input('Ingrese la coordenada j para encender una casilla: '))-1
 53 encender_casilla(i, j)
 54 
 55 # Iteraciones -> tiempo
 56 iteraciones = int(input('Ingrese el numero de Iteraciones a realizar: '))
 57 for x in range(iteraciones):
 58     print('Iteración:', x + 1)
 59     mostrar_tablero()
 60     ti = update()
 61     print()
 62 

