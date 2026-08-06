def sumNumbers(self, root):
        def find(root,sumi):
            if root is None:
                return 0
            sumi = sumi *10 + root.val 
            if root.left is None and root.right is None:
                 return sumi
            return find(root.left, sumi) + find(root.right, sumi)
        
        return find(root,0)