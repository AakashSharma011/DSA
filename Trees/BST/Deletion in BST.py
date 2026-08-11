class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def get_succesor(root):
        root=root.right
        while root!=None and root.left!=None:
            root=root.left
        return root
    def deleteNode(root,key):
        if root is None:
            return root
        if root.val>key:
            root.left=Solution.deleteNode(root.left,key)
        elif root.val<key:
            root.right=Solution.deleteNode(root.right,key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                succ=Solution.get_succesor(root)
                root.val=succ.val
                root.right=Solution.deleteNode(root.right,succ.val)
        return root
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
print(Solution.deleteNode(root, 3).left.val)  # Output: 2