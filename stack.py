class Stack:
    def __init__(self,max):
        self.stack=[]
        self.max=max
        
    def push(self,item):
        if(len(self.stack)==self.max):
            print("Stack Overflow!!\n")
        else:
            self.stack.append(item)
            
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Underflow!!")
            
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Underflow!!")
            
    def is_empty(self):
        return len(self.stack)==0
        
    def view(self):
        return self.stack
        
max=int(input("Enter the maximum size of the stack: "))
stack=Stack(max)
stack.push(10)
stack.push(14)
stack.push(20)
print(stack.view())

stack.pop()
print(stack.view())

stack.push(30)
print(stack.view())

print(stack.peek())

