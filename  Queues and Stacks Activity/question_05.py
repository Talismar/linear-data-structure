""" 
5. Dada uma pilha com N elementos, elabore uma fun ̧c ̃ao recursiva que inverta a ordem
   dos elementos da pilha.
"""

class Stack:
    def __init__(self, dim: int):
        self.lenght = dim
        self.top = 0
        self.stack = [None] * dim
    
    def __str__(self):
        ret = [str(i) for i in self.stack]
        
        return f"{ret}"

    def isEmpty(self):
        if self.top == 0:
            return True
        return False

    def isFull(self):
        if self.top == self.dim:
            return True
        return False

    def stackUp(self, value):
        if self.top < self.lenght:
            self.stack[self.top] = value
            self.top += 1
            return value
        
        return "Full Stack"

    def unstack(self):
        if self.top > 0:
            self.top -= 1
            self.stack[self.top] = None
            return self.stack

        else:
            return "Empty Stack"
    
    def showTheTop(self):
        if self.top == 0:
            return "Empyt Stack"

        return self.stack[self.top - 1]

def insert_at_bottom(s: Stack, data):
    if s.isEmpty():
        s.stackUp(data)
    else:
        popped = s.showTheTop()
        s.unstack()
        insert_at_bottom(s, data) # remove all items from the stack
        s.stackUp(popped) # insert the item at the bottom of the stack
 
 
def reverse_stack(s: Stack):
    if not s.isEmpty(): # if the stack element emtpy
        popped = s.showTheTop() # get the top
        s.unstack() # remove the top
        reverse_stack(s) # call reverse_stack again with stacked elements
        insert_at_bottom(s, popped)

stackRoot = Stack(5)
stack01 = Stack(5)
[stack01.stackUp(i) for i in [1,2,3,4,5]]

reverse_stack(stack01)

print("S1: ", stack01)

