""" 
1. Reverta a ordem dos elementos de uma pilha.
    (a) usando duas pilhas adicionais. 
 ###(b) usando uma fila adicional.
    (c) usando uma pilha adicional e algumas vari ́aveis.
"""

class Queen:
    def __init__(self, dim: int):
        self.dim = dim
        self.last = 0
        self.first = 0
        self.fila = [None] * dim 

    def fullQueue(self):
        if None in self.fila:
            return False 
        else: 
            return True

    def insert(self, value):
        if not self.fullQueue():
            if self.last == self.dim:
                self.last = 0
            
            self.fila[self.last] = value
            self.last += 1
            
        else:
            print("Full Queue!!!")

    def remove(self):
        if self.first == self.dim:
            self.first = 0
        
        if self.fila[self.first] != None:
            self.fila[self.first] = None
            self.first += 1
        
        else:
            print("Empty Queue!!!")

    def __str__(self):
        ret = [str(i) for i in self.fila]
        
        return f"{ret}"

class Stack:
    def __init__(self, dim: int):
        self.lenght = dim
        self.top = 0
        self.stack = [None] * dim

    def stackUp(self, value):
        if self.top < self.lenght:
            self.stack[self.top] = value
            self.top += 1
            return "OK " + str(value)
        
        return "Full Stack"

    def unstack(self):
        if self.top > 0:
            self.top -= 1
            self.stack[self.top] = None

        else:
            return "Empty Stack"

    def showTheTop(self):
        if self.top == 0:
            return "Empyt Stack"

        return self.stack[self.top - 1]

    def isEmpty(self):
        if self.top > 0:
            return True
        return False

    def isFull(self):
        if self.top == self.dim:
            return True
        return False
    
    def bottomInsertion(self):
        pass

    def __str__(self):
        ret = [str(i) for i in self.stack]
        
        return f"{ret}"

    def reverse(self, stack1):
        lenght = stack1.lenght
        queen = Queen(lenght)
        
        for i in [1,2,3,4,5]:
            queen.insert(stack1.showTheTop())
            stack1.unstack()
        print(queen)

stackRoot = Stack(5)
stack1 = Stack(5)

[stack1.stackUp(i) for i in [1,2,3,4,5]]
print(stack1)
stackRoot.reverse(stack1)