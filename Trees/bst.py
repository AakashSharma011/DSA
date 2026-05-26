from typing import Optional


class Node:
    """
    Represents a single node in a Binary Search Tree (BST).
    """
    def __init__(self, value: int):
        self.data: int = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def insert(root: Optional[Node], value: int) -> Node:
    """
    Insert a value into the BST and return the root.
    
    Time Complexity: O(log N) average, O(N) worst-case (skewed tree).
    Space Complexity: O(log N) average, O(N) worst-case for recursion stack.
    """
    if root is None:
        return Node(value)
    
    if value < root.data:
        root.left = insert(root.left, value)
    elif value > root.data:
        root.right = insert(root.right, value)
    
    # If value is already present, do nothing (sets do not allow duplicates)
    return root


def search(root: Optional[Node], value: int) -> Optional[Node]:
    """
    Search for a value in the BST and return the matching Node.
    
    Time Complexity: O(log N) average, O(N) worst-case.
    Space Complexity: O(log N) average, O(N) worst-case for recursion stack.
    """
    if root is None or root.data == value:
        return root
    
    if value < root.data:
        return search(root.left, value)
    return search(root.right, value)


def inorder(root: Optional[Node]) -> None:
    """
    In-order traversal (Left, Root, Right) of the tree.
    Prints the values in sorted ascending order.
    """
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


if __name__ == '__main__':
    # Initialize tree
    root = None
    elements = [20, 15, 30, 12, 18, 40]
    print(f"Inserting elements: {elements}")
    for el in elements:
        root = insert(root, el)
        
    print("In-order traversal of the BST:")
    inorder(root)
    print("\n")
    
    # Search tests
    target_found = 18
    target_missing = 25
    
    node_found = search(root, target_found)
    if node_found:
        print(f"Element {target_found} found in BST.")
    else:
        print(f"Element {target_found} not found in BST.")
        
    node_missing = search(root, target_missing)
    if node_missing:
        print(f"Element {target_missing} found in BST.")
    else:
        print(f"Element {target_missing} not found in BST.")
