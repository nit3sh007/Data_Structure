class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None 

    def add_last(self,data):
        if self.head is None:
            new_node  = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node    
            new_node.prev = cur
            new_node.next = None        

    def add_start(self,data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node

        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node = None    

    def remove(self,key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                if not cur.next:
                    cur  = None
                    self.head = None
                    return

                else:
                     nxt = cur.next
                     cur.next = None
                     nxt.prev = None
                     cur = None
                     self.head = nxt
                     return
            elif cur.data == key:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None 
                    cur = None
                    return        


    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

llist = DoublyLinkedList()
# llist.add_last(1)
# llist.add_last(2)
# llist.add_last(3)
llist.add_last(5)
llist.add_start("n")
llist.remove(3)
llist.print_list()