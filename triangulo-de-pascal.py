def triangulo(n):
    if n < 0:
        return []

    trigPAS = []
    for i in range(n):
        linha = [1] * (i + 1)
        for j in range(1, i):
            linha[j] = trigPAS[i - 1][j - 1] + trigPAS[i - 1][j]
        trigPAS.append(linha)

    return trigPAS
