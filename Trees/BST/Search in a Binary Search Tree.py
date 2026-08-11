class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def searchBST(self, root, val):
        if root is None:
            return None
            
        if root.val == val:
            return root
        elif root.val>val:
            return self.searchBST(root.left,val)
        elif root.val<val:
            return self.searchBST(root.right,val)

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)   
print(Solution().searchBST(root, 2).val)  # Output: 2