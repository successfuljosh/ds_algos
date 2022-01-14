#Depth first search is a way of traversing a tree.
#has 3 major ways:
#-Pre-order:Left Parent Right,, Visits the parents, then children
#-Inorder: Left Parent Right,, Visits the  children, then parents
# - Post-Order: Visit all children first before the parent

class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return 'Node ('+self.value +')'

#recursive method for DFS
def walk(tree):
    if tree is not None:
        print(tree)  #the position of this determines if it is pre-order, inorder or post order travesal
        walk(tree.left)
        walk(tree.right)

#iterative method
def walk2(tree, stack):
    stack.append(tree)
    while len(stack) > 0:
        node =  stack.pop()
        if node is not None:
            print(node)
            stack.append(node.left)
            stack.append(node.right)


mytree = Node('A', Node('B', Node('D'), Node('E')), Node('C', Node('F'), Node('G')))

# walk(mytree)
walk2(mytree,[])