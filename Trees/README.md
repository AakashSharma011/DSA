# 🌳 Tree Implementations

This folder contains clean, standard Python implementations of tree-based data structures and algorithms, focusing on Binary Search Trees (BST) and standard Binary Tree traversals.

All BST files are located in the [BST/](file:///c:/Users/11128/OneDrive/Desktop/Python/DSA/Trees/BST) directory.

---

## 📈 Visual Representations

### 1. Binary Tree Traversals (`BST/traversal.py`)
For the following perfect binary tree of height 3:

```text
       1
      / \
     2   3
    / \ / \
   4  5 6  7
```

- **Pre-order (Root -> Left -> Right):** `1 2 4 5 3 6 7`
- **In-order (Left -> Root -> Right):** `4 2 5 1 6 3 7` (Yields sorted order in a BST)
- **Post-order (Left -> Right -> Root):** `4 5 2 6 7 3 1`

---

### 2. Binary Search Tree (BST) Deletion Scenarios (`BST/deletion_bst.py`)

#### Case 1: Node to delete is a Leaf Node (0 children)
Simply remove the node from the tree.
```text
       50                      50
      /  \                    /  \
    30    70     ───>       30    70
   /
 20 (Delete)
```

#### Case 2: Node to delete has One Child
Connect the parent node directly to the child of the deleted node.
```text
       50                      50
      /  \                    /  \
    30    70     ───>       20    70
   /
 20 (Delete)
```

#### Case 3: Node to delete has Two Children
Find the **Inorder Successor** (smallest node in the right subtree), copy its value to the node to be deleted, and recursively delete the successor.
```text
        50 (Delete)                   60 (Successor copied)
       /  \                          /  \
     30    70          ───>        30    70
          /  \                          /  \
        60    80                      65    80
          \
          65
```

---

## 📚 Concepts Covered

A **Tree** is a non-linear, hierarchical data structure consisting of nodes connected by edges.

### 1. Binary Search Tree (BST) Operations (`BST/bst.py`)
- **Insertion:** Inserts a node into the BST maintaining the invariant: `Left.data < Parent.data < Right.data`.
- **Search:** Locates a node in the tree in $O(\log N)$ average time.

### 2. Ceil and Floor in BST
- **Ceil (`BST/ceil_in_bst.py`):** The smallest key in the BST that is greater than or equal to the target value.
- **Floor (`BST/floor_in_bst.py`):** The largest key in the BST that is less than or equal to the target value.

### 3. BST Deletion (`BST/deletion_bst.py`)
- Implements node removal by handling the three cases of child configurations (no children, one child, two children).

### 4. Tree Traversals (`BST/traversal.py`)
- Implements Depth First Search (DFS) variants: Pre-order, In-order, and Post-order.

---

## ⚡ Complexity Analysis

| Operation | Average Case | Worst Case (Skewed Tree) | Space Complexity (Worst Case) | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Insertion** | $O(\log N)$ | $O(N)$ | $O(N)$ | Worst case occurs when inserting sorted keys. |
| **Search** | $O(\log N)$ | $O(N)$ | $O(N)$ | Space complexity is due to the recursion call stack. |
| **Deletion** | $O(\log N)$ | $O(N)$ | $O(N)$ | Relies on finding successor and traversing down. |
| **Ceil / Floor** | $O(\log N)$ | $O(N)$ | $O(1)$ | Implemented iteratively for $O(1)$ space. |
| **Traversals** | $O(N)$ | $O(N)$ | $O(H)$ | $H$ is the height of the tree ($H = \log N$ average, $H = N$ worst). |

---

## 🌐 Real-World Applications

- **File Systems:** Hierarchical directory nesting.
- **Database Indexing:** B-Trees/B+ Trees are utilized to index database pages for speed.
- **Routing:** Trie structures are used for IP lookup and fast prefix routing.

---

## 🎯 Interview Notes & Cheat Sheet

1. **Inorder Successor / Predecessor:**
   - **Successor:** Go right once, then go left as far as possible.
   - **Predecessor:** Go left once, then go right as far as possible.
2. **Balanced Trees:**
   - To prevent the tree from skewing and degrading to $O(N)$, self-balancing trees like AVL or Red-Black Trees perform structural rotations on insertion/deletion.
3. **Traversal Properties:**
   - Inorder traversal of a BST always yields keys in ascending sorted order.
