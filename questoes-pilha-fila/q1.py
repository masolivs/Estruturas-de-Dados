def processar_fila(fila, sequencia):
    resultado = []
    for char in sequencia:
        if char == '*':
            if fila:
                resultado.append(fila.pop(0))
        else:
            fila.append(char)
    return ''.join(resultado)
def main():
    entrada = input()
    fila = []
    resultado = processar_fila(fila, entrada)
    print(resultado)

if __name__ == "__main__":
    main()
