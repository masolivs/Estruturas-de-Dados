#Algoritmo de ordenação e busca. Percorre a lista várias vezes, trocando de ordem quando o elemento anterior é MAIOR que o posterior.
#Complexidade: Pior Caso (O(n^2)); Melhor Caso (O(n)). De espaço: (O(1)).

def bubbleSort(alist):
    for passnum in range(len(alist) -1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1],alist[i]

n = int(input()) #tamanho da lista
alist = []
for i in range(n):
    valor = int(input())
    alist.append(valor)
print("Lista Original:",alist)
bubbleSort(alist)
print('Lista ordenada:',alist)
