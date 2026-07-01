class Solution:
    def LCA(self,root,p,q):
        if root is None:
            return None
        if root==p or root==q:
            return root
        left=self.LCA(root.left,p,q)
        right=self.LCA(root.right,p,q)
        if left and right:
            return root
        if left:
            return left
        return right