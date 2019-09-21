                                        #insert or Search
class Node:
    def __init__(self,data):
        self.data = data
        self.leftChild= None
        self.rightChild = None

class BST():
        def __init__(self):
            self.root= None

        def insert(self,data=None):
            #check Root node is none
            if self.root is None:
                self.root = Node(data)
            else:
                #insert data if not value in root 
                self.insertIn(data,self.root)    

        def insertIn(self,data,cur_node):
            #check entered value is less then root node(data) 
            #if entered value is less then root node then value assign as left of root node
            if data < cur_node.data:
                #again check left child nodeis none oe not
                if cur_node.leftChild is None:
                    #set left child as node
                    cur_node.leftChild = Node(data)
                    #set left node as current node 
                    cur_node.leftChild.parent = cur_node
                else:
                    #else set current node as left child
                    self.insertIn(data,cur_node.leftChild)
            #check entered value is less then root node(data) 
            #if entered value is greater then root node then value assign as right of root node
  
            if data > cur_node.data:
                #check right child node is empty or not 
                if cur_node.rightChild is None:
                    cur_node.rightChild = Node(data)
                    #if empty then assign right node as parent
                    cur_node.rightChild.parent = cur_node
                else:
                    #if right node is not empty then assign rightnode as child node
                    self.insertIn(data,cur_node.rightChild)
            else:
                #if dublicate value is preset in given tree
                print('value is already present in Tree')        

        def search(self,data):
            if self.root:
                is_find = self._search(data,self.root)
                #if value availabe in Tree then retunn True otherwise False
                if is_find:
                    return True
                return False
            else:
                return None

        def _search(self,data,cur_node):
            #check data is less then current node(root) in left child node
            if data < cur_node.data and cur_node.leftChild:           
                return self._search(data,cur_node.leftChild)
            #check data is less then current node(root) in left child node
            elif data > cur_node.data and cur_node.rightChild:
                return self._search(data,cur_node.rightChild) 
            if data ==cur_node.data:
                return True
                    

bst = BST()
bst.insert(10)
bst.insert(1)
bst.insert(11)
print(bst.search(0))
