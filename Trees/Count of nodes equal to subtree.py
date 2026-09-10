# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):

        def dfs(node):
            if not node:
                return 0, 0, 0

            left_sum, left_count, left_ans = dfs(node.left)
            right_sum, right_count, right_ans = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            current_ans = left_ans + right_ans

            if total_sum // total_count == node.val:
                current_ans += 1

            return total_sum, total_count, current_ans

        total_sum, total_count, ans = dfs(root)

        return ans