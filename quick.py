#Quick Sort:
#Outro jeito de dividir e conquistar. Ele escolhe um elemento como pivô e particiona os demais em torno do escolhido, deixando os números menores antes dele e os maiores depois dele.
#Complexidade: Pior Caso =  O(N^2); Melhor Caso: O(N log N)  

def quickSort(alist):
    #Caso Base - lista vazia ou um único elemento
    if len(alist) <=1:
        return alist
    #elementos menores que o pivo vão para a esquerda e os maiores vão para a direita
    esquerda, pivo, direita = reordena(alist)
    esquerda = quickSort(esquerda)
    direita = quickSort(direita)
    esquerda.append(pivo)
    esquerda.extend(direita)
    return esquerda

def reordena(alist):
    #primeiro elem como pivo
    pivo = alist[0]
    #lista vazia p elem maiores e menores
    esquerda = []
    direita = []
    #percorre cada posicao da lista
    for i in range (1,len(alist)):
        if alist[i] < pivo: #vai p esquerda
            esquerda.append(alist[i])
        else: #vai p direita
            direita.append(alist[i])
    return esquerda, pivo, direita