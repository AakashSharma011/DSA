from typing import Optional


class Node:
    """
    Represents a single node in a Binary Search Tree (BST) for deletion demonstration.
    """
    def __init__(self, value: int):
        self.data: int = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def insert(root: Optional[Node], value: int) -> Node:
    """
    Insert a value into the BST and return the root.
    """
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert(root.left, value)
    elif value > root.data:
        root.right = insert(root.right, value)
    return root


def get_successor(curr_node: Node) -> Node:
    """
    Find the inorder successor of a node (minimum node in its right subtree).
    """
    temp = curr_node.right
    while temp is not None and temp.left is not None:
        temp = temp.left
    return temp  # type: ignore


def delete_node(root: Optional[Node], value: int) -> Optional[Node]:
    """
    Delete a value from the BST and return the new root node.
    
    Time Complexity: O(log N) average, O(N) worst-case.
    Space Complexity: O(log N) average, O(N) worst-case.
    """
    if root is None:
        return None

    # Recur down the tree
    if value < root.data:
        root.left = delete_node(root.left, value)
    elif value > root.data:
        root.right = delete_node(root.right, value)
    else:
        # Case 1 & 2: Node has 0 or 1 child
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        # Case 3: Node has two children
        # Get the inorder successor (smallest in the right subtree)
        succ = get_successor(root)
        
        # Copy the successor's content to this node
        root.data = succ.data
        
        # Delete the inorder successor
        root.right = delete_node(root.right, succ.data)

    return root


def inorder(root: Optional[Node]) -> None:
    """
    Print the BST elements in-order.
    """
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


if __name__ == '__main__':
    root = None
    elements = [20, 15, 30, 12, 18, 40]
    for el in elements:
        root = insert(root, el)

    print("Initial BST (In-order traversal):")
    inorder(root)
    print("\n")

    print("Deleting node 15...")
    root = delete_node(root, 15)

    print("BST after deletion of 15 (In-order traversal):")
    inorder(root)
    print()
