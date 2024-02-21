'''
Vamos a utilizar la librería sympy para estudiar 
la función se probabilidad.
En este caso vamos a representar un caso en el
que conocemos los parámetro de regresión que se van 
a utilizar en un sistema de clasificación binario
mediante un modelo de regresión logística.
Como ya sabemos del caso de regresión lineal, estos 
parámetros coef_ e intercept_ se obtiene de la optimización
(encontrar mínimo) de una función llamada función de costo
que en el caso de la regresión lineal era la función de 
minimos cuadrados.En este caso la función de costo es mucho 
más compleja por lo que simplemente tenemos que saber que 
 existe y que es el logaritmo de la función logit.
'''
from matplotlib import pyplot as plt

from sympy.plotting import plot3d 
from sympy import *
b0, b1, x = symbols('b0 b1 x')
p = 1.0 / (1.0 + exp(-(b0 + b1 * x)))

r=b0 + b1 * x
#Sustituir b0 por el valor expecificado... -2.823
p = p.subs(b0,-1.823)
# r=r.subs(b0,-1.823)
#Sustituir b0 por el valor expecificado... 0.620
p = p.subs(b1, 0.720)
# r=r.subs(b1,0.720)
print('p= ',p)
# print('y= ',r)
plot(p)

