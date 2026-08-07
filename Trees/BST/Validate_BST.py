class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        def valid(node,low,high):
            if not node:
                return True
            if node.val<=low or node.val>=high:
                return False
            return(valid(node.left,low,node.val)and valid(node.right,node.val,high))
        return valid(root,float('-inf'),float('inf'))

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

solution = Solution()
print(solution.isValidBST(root))