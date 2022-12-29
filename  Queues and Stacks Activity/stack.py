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
        stack2 = Stack(lenght)
        
        for i in [1,2,3,4,5]:
            stack2.stackUp(stack1.showTheTop())
            stack1.unstack()
        print(stack2)

stackRoot = Stack(5)
stack1 = Stack(5)

[stack1.stackUp(i) for i in [1,2,3,4,5]]
print(stack1)
stackRoot.reverse(stack1)
