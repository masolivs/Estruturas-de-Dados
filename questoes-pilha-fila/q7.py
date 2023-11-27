class RoupasOrganizer:
    def __init__(self):
        self.gaveta = []
        self.total_roupas = 0
        self.total_tempo = 0

    def organizar_roupas(self, tipo, cor, tempo):
        self.gaveta.insert(0, {"tipo": tipo, "cor": cor})
        self.total_roupas += 1
        self.total_tempo += tempo

    def mostrar_gaveta(self):
        for roupa in self.gaveta:
            print(f'Tipo: {roupa["tipo"]}, Cor: {roupa["cor"]}')

    def mostrar_resultado(self):
        self.mostrar_gaveta()
        print(f'Total de roupas: {self.total_roupas}')
        print(f'Total de tempo: {self.total_tempo}')

def main():
    num_entradas = int(input())
    organizer = RoupasOrganizer()

    for _ in range(num_entradas):
        entrada = input().split()
        tipo, cor, tempo = entrada[0], entrada[1], int(entrada[2])
        organizer.organizar_roupas(tipo, cor, tempo)

    organizer.mostrar_resultado()


if __name__ == "__main__":
    main()
