class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):

        # Case 1: Dono None hain
        if p is None and q is None:
            return True

        # Case 2: Ek None hai aur dusra nahi
        if p is None or q is None:
            return False

        # Case 3: Values different hain
        if p.val != q.val:
            return False

        # Left aur Right subtree compare karo
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# ---------------- Tree 1 ----------------
#
#        1
#      /   \
#     2     3
#

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)


# ---------------- Tree 2 ----------------
#
#        1
#      /   \
#     2     3
#

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)


sol = Solution()

if sol.isSameTree(root1, root2):
    print("Trees are Same")
else:
    print("Trees are NOT Same")