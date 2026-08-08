# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        inorder_map={}
        for index,value in enumerate(inorder):
            inorder_map[value]=index
        self.pre_idx=0

        def build(low,high):
            if low>high:
                return None

            root_val=preorder[self.pre_idx]
            self.pre_idx +=1

            root=TreeNode(root_val)
            mid=inorder_map[root_val]
            root.left=build(low,mid-1)
            root.right=build(mid+1,high)
            return root
        return build(0,len(inorder)-1)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
print("Preorder:", preorder)
print("Inorder:", inorder)
solution = Solution()
root = solution.buildTree(preorder, inorder)
