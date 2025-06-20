import time

def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def fibonacci_iterativo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def medir_tiempo(funcion, n):
    inicio = time.time()
    resultado = funcion(n)
    fin = time.time()
    return resultado, fin - inicio

if __name__ == "__main__":
    n = 42
    resultado1, tiempo1 = medir_tiempo(fibonacci_iterativo, n)
    resultado2, tiempo2 = medir_tiempo(fibonacci_recursivo, n)
    print(f"Suma Iterativa: Resultado={resultado1}, Tiempo={tiempo1:.8f} segundos")
    print(f"Suma Formula: Resultado={resultado2}, Tiempo={tiempo2:.8f} segundos")