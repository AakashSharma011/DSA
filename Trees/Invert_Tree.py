class Solution:
    def invert(self,root):
        if root is None:
            return None
        
        root.left,root.right=root.right,root.left
        self.invert(root.left)
        self.invert(root.right)
        return root