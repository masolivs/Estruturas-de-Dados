def fila_eterna(fila, avancos):
    for _ in range(avancos):
        pessoa_chamada = fila.pop(0)
        fila.append(pessoa_chamada)
    
    pessoa_frente = fila[0]
    pessoa_fim = fila[-1]

    return pessoa_frente, pessoa_fim

nomes = input().split()
avancos = int(input())

pessoa_frente, pessoa_fim = fila_eterna(nomes, avancos)
print(f'Pessoa da frente: {pessoa_frente}')
print(f'Pessoa do fim: {pessoa_fim}')
