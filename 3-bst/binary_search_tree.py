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
        else:
            self.insertNode(data, self.root)


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

    def traverse(self):
        if self.root: 
            self.traverseInOrder(self.root)
    
    def traverseInOrder(self, node): 
        if node.leftChild: 
            self.traverseInOrder(node.leftChild)

        print("%s" %node.data)
    
        if node.rightChild: 
            self.traverseInOrder(node.rightChild)
      


bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(6)
print(bst)
print(bst.getMinValue())
print(bst.getMaxValue())




