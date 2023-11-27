class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None 

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]
        else:
            return None  

    def size(self):
        return len(self.items)
