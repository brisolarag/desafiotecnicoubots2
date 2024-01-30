import sys

'''
Para uso:
<numero de elementos>
<espaco separado elementos>
<elementos a ser inseridos>
Exit
'''


lines = []

for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line.split('\n')[0])

nol = lines[0]
treeInput = [int(x) for x in lines[1].split(' ')]
toIns = lines[2]


        

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1  

        
class AVLTree:
    def __init__(self):
        self.root = None

    # Insertion operation - Add your code here
    def insert(self,data):   
        self.root=insertnew(self.root,data)
    # Traversals
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(f"{node.data}(BF={getBalance(node)})", end=" ")
            self.inorder(node.right)
    
    def postorder(self, node):
        if node is not None:
            print(f"{node.data}(BF={getBalance(node)})", end=" ")
            self.postorder(node.left)
            self.postorder(node.right)
            
    def print_balance(self):
        self.inorder(self.root)
        print("")
        self.postorder(self.root)

def insertnew(root,data):
    if root is None:
        return Node(data)
    if root.data<data:
        root.right=insertnew(root.right,data)
    if root.data>data:
        root.left=insertnew(root.left,data)
    root.height=1+max(getheight(root.left),getheight(root.right))
   
#   caso: left left
    if getBalance(root)>1 and data<root.left.data:
        return rotateright(root)
    
#   caso: right right
    if getBalance(root)<-1 and data>root.right.data: 
        return rotateleft(root)
    
#   caso: left right 
    if getBalance(root)>1 and root.left.data<data:
        root.left=rotateleft(root.left)
        return rotateright(root)
    
#   caso: right left 
    if getBalance(root)<-1 and root.right.data>data:
        root.right=rotateright(root.right)
        return rotateleft(root)
    return root
def getheight(root):
    if root is None:
        return 0
    return root.height
def getBalance(root):
    if root is None:
        return 0
    return (getheight(root.left)-getheight(root.right))

def rotateleft(root):
    y=root.right
    T2=y.left
    # rotation
    y.left=root
    root.right=T2
    
    root.height=1+max(getheight(root.left),getheight(root.right))
    y.height=1+max(getheight(y.left),getheight(y.right))
    return y

def rotateright(root):
    y=root.left
    T3=y.right
    # rotation
    y.right=root
    root.left=T3
    root.height=1+max(getheight(root.left),getheight(root.right))
    y.height=1+max(getheight(y.left),getheight(y.right))
    return y
tree = AVLTree()

for x in treeInput:
    tree.insert(x)
tree.insert(int(toIns))
tree.print_balance()

'''
Para uso:
<numero de elementos>
<espaco separado elementos>
<elementos a ser inseridos>
Exit
'''