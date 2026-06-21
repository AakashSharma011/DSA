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


def find_floor(root: Node | None, value: int) -> int:
    """
    Finds the Floor of a given value in a Binary Search Tree (BST).
    Floor is the largest element in the BST that is less than or equal to the given value.
    If no such value exists, returns -1.
    
    Time Complexity: O(H) where H is the height of the BST (O(log N) average, O(N) worst case).
    Space Complexity: O(1) iterative lookup.
    """
    floor_val = -1
    while root is not None:
        if root.data == value:
            return root.data
        if root.data > value:
            root = root.left
        else:
            floor_val = root.data
            root = root.right
    return floor_val


if __name__ == '__main__':
    # Constructing a sample BST
    #         10
    #        /  \
    #       5    15
    #      / \
    #     2   6
    root = None
    elements = [10, 5, 15, 2, 6]
    for el in elements:
        root = insert(root, el)

    print("Inorder traversal of the constructed BST:")
    inorder(root)
    print("\n")

    test_value = 14
    floor_res = find_floor(root, test_value)
    print(f"Floor of {test_value} is: {floor_res}")

    test_value_2 = 1
    floor_res_2 = find_floor(root, test_value_2)
    print(f"Floor of {test_value_2} is: {floor_res_2}")