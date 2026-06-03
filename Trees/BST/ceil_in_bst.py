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


def find_ceil(root: Node | None, value: int) -> int:
    """
    Finds the Ceil of a given value in a Binary Search Tree (BST).
    Ceil is the smallest element in the BST that is greater than or equal to the given value.
    If no such value exists, returns -1.
    
    Time Complexity: O(H) where H is the height of the BST (O(log N) average, O(N) worst case).
    Space Complexity: O(1) iterative lookup.
    """
    ceil_val = -1
    while root is not None:
        if root.data == value:
            return root.data
        if root.data < value:
            root = root.right
        else:
            ceil_val = root.data
            root = root.left
    return ceil_val


if __name__ == '__main__':
    # Constructing a sample BST
    #         10
    #        /  \
    #       5    13
    #      / \   /  \
    #     3   6 11  14
    #    /   \
    #   2     9
    #    \
    #     4
    root = None
    elements = [10, 5, 13, 3, 6, 2, 13, 4, 9, 11, 14]
    for el in elements:
        root = insert(root, el)

    print("Inorder traversal of the constructed BST:")
    inorder(root)
    print("\n")

    test_value = 8
    ceil_res = find_ceil(root, test_value)
    print(f"Ceil of {test_value} is: {ceil_res}")

    test_value_2 = 15
    ceil_res_2 = find_ceil(root, test_value_2)
    print(f"Ceil of {test_value_2} is: {ceil_res_2}")
