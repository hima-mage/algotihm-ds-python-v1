class Node(object): 
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
      


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
    
    def insert(self, data): 
        if not self.root : 
            self.root = Node(data)
    # O(logn) - if the tree is balanced -> can be reduce to O(N)
    def insertNode(self, data, node): 
        if data < node.data:   # leftChild
            if node.leftChild: 
                self.insertNode(data, node.leftChild) # recursive
            else :
                node.leftChild = Node(data) # insert it into leftnode
        else :  # rightChild
            if node.rightChild: 
                self.insertNode(data, node.rightChild) # recursive
            else: 
                node.rightChild = Node(data) # insert it into  righnode

    def getMinValue(self) : 
        if self.root: 
            return self.getMin(self.root)

    def getMin(self , node): 
        if node.leftChild: 
            return self.getMin(node.leftChild)
        return node.data

    def getMaxValue(self) : 
        if self.root: 
            return self.getMax(self.root)

    def getMax(self , node): 
        if node.rightChild: 
            return self.getMax(node.rightChild)
        return node.data












