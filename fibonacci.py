def fibonacci(n, contador):
    contador[n] += 1
    if n <= 1:
        return n
    else:
        return fibonacci(n-1, contador) + fibonacci(n-2, contador)

n = int(input())
contador = [0] * (n + 1)
resultado = fibonacci(n, contador)

print(f'fibonacci({n}) = {resultado}.')
for i in range(n + 1):
    print(f'{contador[i]} chamada(s) a fibonacci({i}).')
