#critério: LIFO: Last In, First Out
#Ou seja, só é possível inserir um novo elemento no final da pilha e só é possível remover um elemento do final da pilha.
#Semelhante a uma lista encadeada
#IMPORTANTE: inserir, remover e observar o topo da pilha. Todas apresentam complexidade de O(1)

class Node: #implementar a classe nó primeiro
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
        self._size = 0
    def push(self,elem): #inserir
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size +=1
    
    def pop(self): #remover elemento do topo da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node
        raise IndexError("Pilha Vazia")
    
    def peek(self): #retorna o topo sem remover
        if self._size > 0:
            return self.top.data
        raise IndexError("Pilha Vazia")
    
    def __len__(self):
        return self._size
    def __repr__(self):
        r = ""
        pointer = self.top
        while (pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r
    def __str__(self):
        return self.__repr__()



