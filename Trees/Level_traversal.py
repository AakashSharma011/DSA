from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def levelOrder(root):
    if root is None:
        return []

    q = deque([root])
    ans = []

    while q:

        level_size = len(q)
        temp = []

        while level_size > 0:

            node = q.popleft()

            temp.append(node.data)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

            level_size -= 1

        ans.append(temp)

    return ans
root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(levelOrder(root))