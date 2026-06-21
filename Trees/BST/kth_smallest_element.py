class Node:
    def __init__(self, value: int):
        self.data = value
        self.left = None
        self.right = None


def insert(root: Node | None, value: int) -> Node:
    """
    Inserts a value into the BST and returns the root of the modified tree.
    """
    if root is None:
        return Node(value)
    if root.data == value:
        return root
    if root.data > value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def inorder(root: Node | None) -> None:
    """
    Performs inorder traversal of the BST.
    """
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


class KthSmallest:
    def __init__(self):
        self.count = 0

    def kth(self, root, k):
        if root is None:
            return -1
        
        left = self.kth(root.left, k)
        if left != -1:
            return left
            
        self.count += 1
        if self.count == k:
            return root.data
            
        return self.kth(root.right, k)


if __name__ == "__main__":
    root=insert(None,20)
    root=insert(root,15)
    root=insert(root,30)
    root=insert(root,12)
    root=insert(root,18)
    root=insert(root,40)
    inorder(root)    
    print("\n")
    finder = KthSmallest()
    print(finder.kth(root, 3))