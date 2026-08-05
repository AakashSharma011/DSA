root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
targetSum = 22
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def find(root,sumi):
            if not root:
                return False
            sumi +=root.val
            if not root.left and not root.right:
                return sumi == targetSum
            return find(root.left,sumi) or find(root.right,sumi)
        return find(root,0)

print(Solution().hasPathSum(root, targetSum))