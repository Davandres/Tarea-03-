import cmath
import math

def calcular_raices(a, b, c):
    # Calcular el discriminante
    discriminante = b ** 2 - 4 * a * c
    
    # Caso de raíces complejas
    if discriminante < 0:
        real = -b / (2 * a)
        imaginario = cmath.sqrt(discriminante) / (2 * a)
        x1 = real + imaginario
        x2 = real - imaginario
    else:
        # Raíces reales
        raiz = math.sqrt(discriminante)
        if b >= 0:
            x1 = -2 * c / (b + raiz)
            x2 = (-b - raiz) / (2 * a)
        else:
            x1 = (-b + raiz) / (2 * a)
            x2 = -2 * c / (b - raiz)
    
    return x1, x2

# Ejemplo
a = 1
b = -3
c = 2
x1, x2 = calcular_raices(a, b, c)
print("Raíz x1:", x1)
print("Raíz x2:", x2)
