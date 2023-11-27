def frequencia(mensagem):
    if not mensagem:
        return ""
    contagem = {}
    for caractere in mensagem:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1

    caractere_mais_frequente = max(contagem, key=contagem.get)

    return caractere_mais_frequente