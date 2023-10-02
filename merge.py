def merge_sort(arr):
    if len(arr) <= 1:
        return
    
    #dividir p ordenar!

    meio = len(arr) // 2
    esquerda_arr = arr[:meio]
    direita_arr = arr[meio:]

#recurssão!

    merge_sort(esquerda_arr) 
    merge_sort(direita_arr)

    i = 0 #idx esquerda
    j = 0 #idx direita 
    k = 0 #idx mesclada

#mesclagem 

    while i < len(esquerda_arr) and j < len(direita_arr):
        if esquerda_arr[i] < direita_arr[j]:
            arr[k] = esquerda_arr[i]
            i += 1
        else:
            arr[k] = direita_arr[j]
            j += 1
        k += 1

    while i < len(esquerda_arr):
        arr[k] = esquerda_arr[i]
        i += 1
        k += 1

    while j < len(direita_arr):
        arr[k] = direita_arr[j]
        j += 1
        k += 1

entrada = input()
numeros = [int(numero) for numero in entrada.split()]
merge_sort(numeros)
print(numeros)
