def tabela_dispersao(tamanho_tabela, chaves):
    tabela = [[] for _ in range(tamanho_tabela)]
    
    for chave in chaves:
        indice = chave % tamanho_tabela
        tabela[indice].append(chave)
    
    return tabela

tamanho_tabela, num_chaves = map(int, input().split())
chaves = list(map(int, input().split()))

tabela = tabela_dispersao(tamanho_tabela, chaves)

for i, coluna in enumerate(tabela):
    print(f"{i} - ", end="")
    if coluna:
        for j, chave in enumerate(coluna):
            if j == len(coluna) - 1:
                print(chave)
            else:
                print(f"{chave} -> ", end="")
    else:
        print("[x]")
