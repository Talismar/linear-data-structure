""" 
3. Transfira os elementos da pilha S1 para S2 de forma que os elementos de S2 estejam
   na mesma ordem que estavam na pilha S1
    (a) usando uma pilha adicional.
 ###(b) usando nenhuma pilha adicional, mas apenas algumas variaveis adicionais
"""


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

    def transfer(self, stack1, stack2):
        lenght = stack1.lenght
        tempVariable = ""
        
        for i in range(lenght):
            tempVariable += str(stack1.showTheTop())
            stack1.unstack()
        
        print("Temp:",tempVariable)

        for j in tempVariable[::-1]:
            # stack1.stackUp(tempStack.showTheTop())
            stack2.stackUp(j)
        
        return stack2

stackRoot = Stack(5)
stack1 = Stack(5)
stack2 = Stack(5)

[stack1.stackUp(i) for i in [1,2,3,4,5]]

print("S1: ", stack1)

stackRoot.transfer(stack1, stack2)

print("S2: ", stack2)
