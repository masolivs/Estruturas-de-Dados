#já está implementada
class ArvoreBinaria(): 
    def __init__(self, dado, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir
#############
def verificaSimetria(raiz):
    def eSimetrica(esq, dir):
        if esq is None and dir is None:
            return True
        if esq is None or dir is None:
            return False

        return (esq.dado == dir.dado) and eSimetrica(esq.esq, dir.dir) and eSimetrica(esq.dir, dir.esq)

    if raiz is None:
        return True

    return eSimetrica(raiz.esq, raiz.dir)