#create a claas for Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#create a class for linklist its self
class linklist:
    def __init__(self):
        self.head = None
#for return value
    def peek(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
#for inserting value in end of the list

    def append_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head= new_node
            return
        last_node = self.head
        while last_node.next:
            last_node= last_node.next
        last_node.next = new_node
#inserting element in start of list
    def append_start(self,data):
        new_node = Node(data)
        new_node.next=self.head
        self.head = new_node
#inserting element in the given element 
    def insert_in_btw(self,prev_node,data):
        if not prev_node:
            print('previous node is not in list')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next=new_node     
     
linklst = linklist()
linklst.append_end(10)
linklst.append_end(20)
linklst.append_end(40)
linklst.append_start(100)
linklst.insert_in_btw(linklst.head.next.next, 10000)
linklst.peek()
             
