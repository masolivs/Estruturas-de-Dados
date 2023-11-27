#FIFO: First In, First Out
#Complexidade: O(1) nas três operações

class Node: #implementar a classe nó primeiro
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0
        
    def push(self,elem): #inserir
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node
        if self.first is None:
            self.first = node
        self._size += 1 
        
    
    def pop(self): #remover elemento do topo da pilha
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            self._size = self._size - 1
            return elem
        raise IndexError("A fila está vazia")
        
    
    def peek(self): #retorna o topo sem remover
        if self._size > 0:
            elem = self.first.data
            return elem
        raise IndexError("A fila está vazia")
        
    
    def __len__(self):
        return self._size
        
    def __repr__(self):
        if self._size > 0:
            r = ''
            pointer = self.first
            while pointer:
                r = r + str(pointer).data + "\n"
                pointer = pointer.next
            return r
        return "Fila Vazia"
       
    def __str__(self):
        return self.__repr__()


