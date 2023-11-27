def numero_para_mes(numero):
    meses = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Marco",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }

    return meses.get(numero, "Mês inválido")

m = int(input())

nome_mes = numero_para_mes(m)

print(nome_mes)