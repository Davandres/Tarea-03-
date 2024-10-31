import math

# Tolerancia
tolerancia = 1e-3

# Valor de pi real
pi_real = math.pi

# Inicialización de variables
aproximacion = 0
n = 0
diferencia = abs(4 * aproximacion - pi_real)

# Bucle para calcular el número mínimo de términos
while diferencia >= tolerancia:
    n += 1
    termino = (-1) ** (n + 1) / (2 * n - 1)
    aproximacion += termino
    diferencia = abs(4 * aproximacion - pi_real)

# Resultado
print("Número mínimo de términos necesarios:", n)

