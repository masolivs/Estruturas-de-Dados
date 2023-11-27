def academia():
    anilhas = []
    while True:
        anilha = int(input())
        if anilha == 0:
            break
        anilhas.append(anilha)
    anilha_desejada = int(input())
    retiradas = []
    while anilhas[-1] != anilha_desejada:
        retirada = anilhas.pop()
        print("Peso retirado:", retirada)
        retiradas.append(retirada)
    print("Peso retirado:", anilha_desejada)
    retiradas.append(anilha_desejada)
    print("Anilhas retiradas:", len(retiradas))
    print("Peso total movimentado:", sum(retiradas))

academia()
