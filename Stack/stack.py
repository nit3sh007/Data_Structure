class Stack:
    #first we create a constructor which inherite all function 
    def __init__(self):
        self.stack=[]
    #check the Stack in empty or not 
    def isEmpty(self):
        return self.stack == [] 
    #push element in Stack
    def push(self,data):
        self.stack.append(data)
     #pop element from Stack
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1] 
        return data
    #peek check the top-most element of stack
    def peek(self):
        return self.stack[-1]
    #check the size of elements 
    def sizeStack(self):
        return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.sizeStack())       
print('popped',stack.pop())
print(stack.sizeStack())
print('peek',stack.peek())
print(stack.isEmpty())
