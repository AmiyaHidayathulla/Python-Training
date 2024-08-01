class Queue:
    def __init__(self,max):
        self.queue= []
        self.max=max
    
    def enqueue(self,item):
        if(len(self.queue)<self.max):
            self.queue.append(item)
        else:
            print("Queue Overflow!!\n")
        
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")
        return None
    
    def is_empty(self):
        return len(self.queue)==0
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None


max=int(input("Enter the size of the queue: "))
queue=Queue(max)
queue.enqueue(5)
queue.enqueue(9)
queue.enqueue(12)

print(queue.dequeue())
print(queue.peek())
