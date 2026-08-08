class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        inorder_map={}
        for index,value in enumerate(inorder):
            inorder_map[value]=index
        self.post_idx= len(postorder)-1

        def build(low,high):
            if low>high:
                return None

            root_val=postorder[self.post_idx]
            self.post_idx -=1

            root=TreeNode(root_val)
            mid=inorder_map[root_val]
            root.right=build(mid+1,high)
            root.left=build(low,mid-1)
            return root
        return build(0,len(inorder)-1)

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
solution = Solution()
root = solution.buildTree(inorder, postorder)
