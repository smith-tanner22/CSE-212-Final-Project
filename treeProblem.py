class Node: #defines the structure of the node
    def __init__(self, data):
        self.data = data #the data in the node
        self.right = None #right side
        self.left = None #left side

    def insert(self, data): #this will help us put all the numbers in the right order
        if self.data:
            if data < self.data: #if its less than
                if self.left is None: #reach the end
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data: #if its greater than
                if self.right is None: #reach the end
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTheTree(self): #this will print the tree(Obviously)
        if self.left:
            self.left.printTheTree()
        print(self.data),
        if self.right:
            self.right.printTheTree()
            
    def preOrder(self, root):
        # START CODING HERE:
        # this is our pre order traversal
        # the order goes from root, to left, to right
        pass

    def postOrder(self, root):
        # START CODING HERE:
        # this is our post order traversal
        # the order goes from left, to right, to root
        pass

root = Node(10) #this is our root number
root.insert(24)
root.insert(67)
root.insert(19)
root.insert(6)
root.insert(31)
root.insert(25)

print(root.preOrder(root))
# Expected output:
# [10, 6, 24, 19, 67, 31, 25]
print(root.postOrder(root))
# Expected output:
# [6, 19, 25, 31, 67, 24, 10]
