def lesma_mais_veloz(l, velocidades):
    # Inicializa as velocidades máximas para cada classe como zero
    max_classe1 = 0
    max_classe2 = 0
    max_classe3 = 0

    for velocidade in velocidades:
        if velocidade < 10 and velocidade > max_classe1:
            max_classe1 = velocidade
        elif 10 <= velocidade < 20 and velocidade > max_classe2:
            max_classe2 = velocidade
        elif velocidade >= 20 and velocidade > max_classe3:
            max_classe3 = velocidade

    return max_classe1, max_classe2, max_classe3

l = int(input())
velocidades = [int(input()) for _ in range(l)]

resultado = lesma_mais_veloz(l, velocidades)

print(resultado[0], end = " ")
print(resultado[1], end = " ")
print(resultado[2], end = " ")