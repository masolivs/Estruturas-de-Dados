def divisores(n):
    lista_divisores = []

    for i in range(1, n + 1):
        if n % i == 0:
            lista_divisores.append(i)

    return lista_divisores