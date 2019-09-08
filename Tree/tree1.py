class Node(object):
    def __init__(self,data= None):
        self.data = data
        self.left = None
        self.right = None
#setter  
    def get_value(self):
        return self.data
#getter
    def set_value(self,data):
        self.data = data 

#set left child
    def set_left_child(self,node):
        self.left = node              
#set right child
    def set_right_child(self,node):
        self.right = node

#get left child
    def get_left_child(self):
        return self.left        
#get right child
    def get_right_child(self):
        return self.right

#check left child exits or not using boolnean expression 
    def left_exits(self):
        return self.left != None
#check tright child exits or not using boolean expression           
    def right_exits(self):
        return self.right != None

node0 = Node('apple')
node1 = Node('mango')
node2 = Node('grapes')

print(f"left child exists {node0.left_exits()}")
print(f"right child exists{node0.right_exits()}")

node0.set_left_child(node1)
node0.set_right_child(node2)

print('\n ADDING LEFT CHILD OR RIGHT CHILD \n')

print(f"left{node0.left_exits()}")
print(f"right{node0.right_exits()}")

#adding node to right or left 
# print(f"""
# data {node0.data}
# left:{node0.left.data}
# right:{node0.right.data}
# """)