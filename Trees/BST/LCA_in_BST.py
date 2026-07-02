class Solution:
    def __init__(self):
        self.ans=None

    def LCA(self,root,p,q):
        if root is None:
            return None
        if root.data>p and root.data>q:
            return self.LCA(root.left,p,q)
        elif root.data<p and root.data<q:
            return self.LCA(root.right,p,q)
        else:
            self.ans=root
            return self.ans
