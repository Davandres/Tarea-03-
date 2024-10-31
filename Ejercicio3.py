import math

# Tolerancia
tolerancia = 1e-3

# Valor de pi real
pi_real = math.pi

# Inicialización de variables
aproximacion_1 = 0
aproximacion_2 = 0
n = 0
pi_aprox = 0
diferencia = abs(pi_aprox - pi_real)

# Bucle para calcular el número mínimo de términos
while diferencia >= tolerancia:
    n += 1
    
    # Cálculo de los términos individuales
    termino_1 = ((-1) ** (n + 1)) * (1 / 5) ** (2 * n - 1) / (2 * n - 1)
    termino_2 = ((-1) ** (n + 1)) * (1 / 239) ** (2 * n - 1) / (2 * n - 1)
    
    # Sumar los términos a las aproximaciones respectivas
    aproximacion_1 += termino_1
    aproximacion_2 += termino_2
    
    # Cálculo de la aproximación de pi
    pi_aprox = 4 * (4 * aproximacion_1 - aproximacion_2)
    
    # Calcular la diferencia con el valor real de pi
    diferencia = abs(pi_aprox - pi_real)

# Resultado
print("Número mínimo de términos necesarios:", n)
