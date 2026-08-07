class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def recoverTree(self,root):
        self.prev=None
        self.first=None
        self.second=None

        def Inorder(node):
            if not node:
                return
            Inorder(node.left)
            if self.prev and node.val < self.prev.val:
                if not self.first:
                    self.first=self.prev
                self.second=node
            self.prev=node
            Inorder(node.right)
        Inorder(root)
        self.first.val,self.second.val=self.second.val,self.first.val

root = TreeNode(1)
root.left = TreeNode(3)
root.left.right = TreeNode(2)
solution = Solution()   
print(solution.recoverTree(root))

# Check inorder traversal
def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val, end=' ')
    inorder(node.right)

inorder(root)