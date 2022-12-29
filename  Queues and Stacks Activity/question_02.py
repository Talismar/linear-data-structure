""" 
2. Coloque os elementos de uma pilha em ordem ascendente usando uma pilha adicional
   e algumas vari ́aveis
"""

class Stack:
    def __init__(self, dim: int):
        self.lenght = dim
        self.top = 0
        self.stack = [None] * dim

    def push(self, value):
        self.stack[self.top] = value
        self.top += 1

    def stackUp(self, value):
        lenght = self.lenght
        tempStack = Stack(lenght)

        if self.top < self.lenght:

            for e, top in zip(range(self.lenght),self.stack):
                if top == None:
                    break

                if top > value:
                    # print("HERE", e, top)
                    # print(self.stack[e:self.stack.index(None)])
                    
                    lenght = len(self.stack[e:])
                    for temp in self.stack[e:self.stack.index(None)]:
                        tempStack.push(temp)
                        self.unstack()
                    
                    break


            self.stack[self.top] = value
            self.top += 1

            for j in tempStack.stack[:tempStack.stack.index(None)]:
                    self.stackUp(j)
                    
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

stackRoot = Stack(5)
stack1 = Stack(5)

for i in [1,2,3,0,2]:
    stack1.stackUp(i)
print(stack1)
