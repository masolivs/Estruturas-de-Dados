from collections import deque

def max_janela_deslizante(n, lista, k):
    resultado = []
    janela = deque()

    for i in range(n):

        while janela and janela[0] < i - k + 1:
            janela.popleft()

        while janela and lista[i] >= lista[janela[-1]]:
            janela.pop()

        janela.append(i)

        if i >= k - 1:
            resultado.append(lista[janela[0]])

    return resultado

n = int(input())
lista = list(map(int, input().split()))
k = int(input())

resultado = max_janela_deslizante(n, lista, k)

for valor in resultado:
    print(valor, end=" ")
