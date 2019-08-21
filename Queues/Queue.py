class Queue:
    def __init__(self):
        # create a empty array
        self.queue= [] 
        #check wether the Queue is Empty or not
    def isEmpty(self):
        return self.queue == []
        #add element is queue
    def enqueue(self,data):
        self.queue.append(data)
        #delete element from queue 
    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data
        
    def peek(self):
        return self.queue[0]
    def lenQ(self):
        return len(self.queue)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(4)
print('Delete',queue.dequeue())
print("len",queue.lenQ())
print('peek',queue.peek())