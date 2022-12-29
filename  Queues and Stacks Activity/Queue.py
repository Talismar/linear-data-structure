class Queue:
    def __init__(self, dim):
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