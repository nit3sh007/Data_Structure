class Node:
    def __init__(self,data):
        self.data= data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node   
    def print_n(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

n = LinkedList()
n.append(10)
n.append(20) 
n.print_n()               
