class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:        
    def __init__(self):
        self.head = None
        
    def printllist(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur ==self.head:
              break            

    def add_start(self,data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head
        if not self.head:
            new_node.next=new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            self.head = new_node

    def add_end(self,data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head      

     def delete(self,key):
        if self.head.data ==key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next                 
  

cllist = CircularLinkedList()
cllist.add_end('!')
cllist.add_end('T')
cllist.add_end(3)
cllist.add_end('s')
cllist.add_end('H')
cllist.add_start('N')
cllist.delete('H')
cllist.printllist()
