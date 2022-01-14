#Binary search tree implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.left=None
        self.right=None


    def insert(self, value):
        if value <= self.data:
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if value == self.data:
            return True
        if value < self.data:
            if self.left==None:
                return  False
            else:
                return self.left.contains(value)
        else:
            if self.right ==None:
                return False
            else:
                return self.right.contains(value)

    def printInOrder(self):
        if self.left != None:
            self.left.printInOrder()

        print(self.data)

        if self.right != None:
            self.right.printInOrder()


bst = Node(7)
bst.insert(2)
bst.insert(8)
bst.insert(12)
bst.insert(1)
print(bst.contains(2))
print(bst.contains(20))
bst.printInOrder()