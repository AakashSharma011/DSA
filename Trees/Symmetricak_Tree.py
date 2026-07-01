class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isMirror(self, left, right):

        # Dono None hain
        if left is None and right is None:
            return True

        # Ek None hai
        if left is None or right is None:
            return False

        # Values same nahi hain
        if left.val != right.val:
            return False

        # Mirror check
        return (self.isMirror(left.left, right.right) and
                self.isMirror(left.right, right.left))

    def isSymmetric(self, root):

        if root is None:
            return True

        return self.isMirror(root.left, root.right)


# ---------------- Create Tree ----------------
#
#            1
#          /   \
#         2     2
#        / \   / \
#       3   4 4   3
#

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.left = TreeNode(4)
root.right.right = TreeNode(3)


# ---------------- Check ----------------

sol = Solution()

if sol.isSymmetric(root):
    print("Tree is Symmetric")
else:
    print("Tree is NOT Symmetric")