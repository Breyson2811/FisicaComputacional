import numpy as np #importa numpy para algunas operacione matemáticas
import matplotlib.pyplot as plt  #importa matplotlib para las gráficas
from numpy.random import uniform #importa numpy.random para generar los números aleatorios

def evaluaFuncion (x_, amplitud, n_itera):
  cont = 0 #inicializamos cont en cero
  for k in range(n_itera): #itera sobre los elementos del muestreo y realiza el cálculo de la cont
    cont = cont + (x_[k] * (1 + x_[k]**2)**(3/2))
  return cont
#Método que resuelve integrales con el método montecarlo
def montecarlo (funcion, a, b, n_itera):
  amplitud = b - a #calcula la amplitud del rango
  x_ = np.random.uniform(a, b, n_itera) #genera un muestreo aleatorio en el rango definido
  cont = evaluaFuncion(x_, amplitud, n_itera)
  resultado = (amplitud) * cont / n_itera #calcula el resultado final multiplicando la amplitud por la suma y dividiendo por el número de iteraciones
  print('Resultado : ', resultado, '\n')
  grafica(x, funcion, x_) #grafíca

#Gráfica de las funciones montecarlo
def grafica (c, f, muestreo):
  plt.title('ÁREAS POR EL MÉTODO MONTECARLO')
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.plot(c, f)
  plt.hist(muestreo, density=True)
  plt.show()

a = 0
b = 1000000000000
x = np.linspace(0.0001, b)
funcion = x * (1 + x**2)**(3/2)
n_itera = 1000000
montecarlo (funcion, a, b, n_itera)
