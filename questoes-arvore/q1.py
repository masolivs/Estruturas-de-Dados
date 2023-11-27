class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        self.raiz = self._inserir(self.raiz, valor)

    def _inserir(self, no, valor):
        if no is None:
            return No(valor)

        if valor < no.valor:
            no.esquerda = self._inserir(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._inserir(no.direita, valor)

        return no

    def infixa(self):
        return self._infixa(self.raiz)

    def _infixa(self, no):
        if no is not None:
            return self._infixa(no.esquerda) + [no.valor] + self._infixa(no.direita)
        else:
            return []

    def prefixa(self):
        return self._prefixa(self.raiz)

    def _prefixa(self, no):
        if no is not None:
            return [no.valor] + self._prefixa(no.esquerda) + self._prefixa(no.direita)
        else:
            return []

    def posfixa(self):
        return self._posfixa(self.raiz)

    def _posfixa(self, no):
        if no is not None:
            return self._posfixa(no.esquerda) + self._posfixa(no.direita) + [no.valor]
        else:
            return []

# Função principal
def processar_comandos():
    arvore = ArvoreBinariaBusca()

    while True:
        comando = input().strip()

        if comando == 'quack':
            break
        elif comando.isnumeric():
            arvore.inserir(int(comando))
        elif comando == 'in':
            print(" ".join(map(str, arvore.infixa())))
        elif comando == 'pre':
            print(" ".join(map(str, arvore.prefixa())))
        elif comando == 'pos':
            print(" ".join(map(str, arvore.posfixa())))

if __name__ == "__main__":
    processar_comandos()
