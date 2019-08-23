''' isEmpty, addFront,deleteFront,addRear,deleteRear,lenght,'''

class Dqueue:
    def __init__(self):
        self.data=[]
    def isEmpty(self):
        return self.data == []
    def addFront(self,data):
        self.data.append(data)
    def addRear(self,data):    
        self.data.insert(0,data)
    def removeFront(self):
        return self.data.pop()
    def removeRear(self,data):
        return self.data.pop(0)
    def size(self):
        return len(self.data)
d = Dqueue()
d.addFront(1)
d.addFront(10)
d.addFront(20)
d.addFront('nitesh')
d.removeFront()
d.addRear(100)
print(d.isEmpty())
print('size',d.size())  
d.addFront('front') 
print('size',d.size())  
d.addRear(200)
print(d.size())
