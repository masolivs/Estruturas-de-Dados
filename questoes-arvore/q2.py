class ArvoreBinaria():
    def __init__(self, dado, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

def constituiArvoreBinariaDeBusca(raiz):
    def eArvoreDeBuscaValida(node, min_valor=float('-inf'), max_valor=float('inf')):
        if node is None:
            return True

        if not (min_valor < node.dado < max_valor):
            return False

        return (eArvoreDeBuscaValida(node.esq, min_valor, node.dado) and
                eArvoreDeBuscaValida(node.dir, node.dado, max_valor))

    return eArvoreDeBuscaValida(raiz)