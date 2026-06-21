class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def insert(root,value):
    if (root == None):
        return Node(value)
    if(root.data==value):
        return root
    if(root.data>value):
        root.left=insert(root.left,value)
    else:
        root.right=insert(root.right,value)
    return root

def Search(root,value):
    if (root == None):
        print("Element Not Found")
        return 
    if(root.data==value):
        print("Element Found")
        return
    if(root.data>value):
        Search(root.left,value)
    else:
        Search(root.right,value)
    


def Inorder(root):
    if (root!=None):
        Inorder(root.left)
        print(root.data,end=" ")
        Inorder(root.right)


root=insert(None,20)
root=insert(root,15)
root=insert(root,30)
root=insert(root,12)
root=insert(root,18)
root=insert(root,40)
Inorder(root)    
print("\n")
Search(root,18)
print("\n")
Search(root,25)