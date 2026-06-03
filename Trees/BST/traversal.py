from typing import Optional


class Node:
    """
    Represents a single node in a Binary Tree for traversal demonstration.
    """
    def __init__(self, value: int):
        self.data: int = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def preorder(root: Optional[Node]) -> None:
    """
    Pre-order traversal: Root -> Left -> Right
    
    Time Complexity: O(N)
    Space Complexity: O(H) where H is the height of the tree (for recursion stack).
    """
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root: Optional[Node]) -> None:
    """
    Post-order traversal: Left -> Right -> Root
    
    Time Complexity: O(N)
    Space Complexity: O(H) where H is the height of the tree.
    """
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


def inorder(root: Optional[Node]) -> None:
    """
    In-order traversal: Left -> Root -> Right
    
    Time Complexity: O(N)
    Space Complexity: O(H) where H is the height of the tree.
    """
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


if __name__ == '__main__':
    # Constructing a perfect binary tree of height 3:
    #        1
    #       / \
    #      2   3
    #     / \ / \
    #    4  5 6  7
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Pre-order Traversal (Root -> Left -> Right):")
    preorder(root)
    print("\n")

    print("In-order Traversal (Left -> Root -> Right):")
    inorder(root)
    print("\n")

    print("Post-order Traversal (Left -> Right -> Root):")
    postorder(root)
    print()
