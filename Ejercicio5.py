def suma_doble_triangular(A, B):
    n = len(A)
    suma = 0
    for i in range(n):
        for j in range(i + 1):  # j va desde 0 hasta i
            suma += A[i] * B[j]
    return suma

# Ejemplos
A = [1, 2, 3]  # Ejemplo de lista A
B = [4, 5, 6]  # Ejemplo de lista B

print("Resultado de suma doble triangular:", suma_doble_triangular(A, B))
