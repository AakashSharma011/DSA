from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):

        if root is None:
            return []

        q = deque([root])
        ans = []

        leftToRight = True

        while q:

            level_size = len(q)
            temp = []

            while level_size > 0:

                node = q.popleft()

                temp.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                level_size -= 1

            if not leftToRight:
                temp.reverse()

            ans.append(temp)

            leftToRight = not leftToRight

        return ans