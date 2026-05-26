# 🌳 Tree Implementations

This folder contains clean, standard Python implementations of tree-based data structures and algorithms: Binary Search Tree (BST) operations (Insertion, Search, Deletion) and standard Binary Tree traversals (Pre-order, In-order, Post-order).

---

## 📈 Visual Representations

### 1. Binary Tree Traversals (`traversal.py`)
For the following perfect binary tree of height 3:

```text
       1
      / \
     2   3
    / \ / \
   4  5 6  7
```

- **Pre-order (Root -> Left -> Right):** `1 2 4 5 3 6 7`
- **In-order (Left -> Root -> Right):** `4 2 5 1 6 3 7`
- **Post-order (Left -> Right -> Root):** `4 5 2 6 7 3 1`

---

### 2. Binary Search Tree (BST) Deletion Scenarios (`deletion_bst.py`)

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

### 1. Binary Search Tree (BST) Properties
- The left subtree of a node contains only nodes with values less than the node's value.
- The right subtree of a node contains only nodes with values greater than the node's value.
- The left and right subtrees must also be binary search trees.
- **Inorder Traversal** of a BST always yields values in sorted ascending order.

### 2. Standard Traversals
- **Pre-order (DFS - Depth First Search variant):** Useful for cloning/copying trees or generating prefix expressions.
- **In-order:** Yields elements in sorted order for BSTs.
- **Post-order:** Useful for deleting the tree (bottom-up deletion), or evaluating mathematical postfix expressions.

### 3. BST Deletion (`deletion_bst.py`)
Deletion is the most complex basic operation on a BST. It requires maintaining the BST invariant by handling three distinct child scenarios:
- **No children:** Nullify the pointer from the parent.
- **One child:** Link the child to the parent.
- **Two children:** Replace the node's value with its inorder successor (smallest node in right subtree) or inorder predecessor (largest node in left subtree), then recursively delete that successor/predecessor node.

---

## ⚡ Complexity Analysis

| Operation | Average Case | Worst Case (Skewed Tree) | Space Complexity (Worst Case) | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Insertion** | $O(\log N)$ | $O(N)$ | $O(N)$ | Worst case occurs when inserting sorted keys. |
| **Search** | $O(\log N)$ | $O(N)$ | $O(N)$ | Space complexity is due to the recursion call stack. |
| **Deletion** | $O(\log N)$ | $O(N)$ | $O(N)$ | Relies on finding successor and traversing down the tree. |
| **Traversals** | $O(N)$ | $O(N)$ | $O(H)$ | $H$ is the height of the tree ($H = \log N$ average, $H = N$ worst). |

---

## 🌐 Real-World Applications

- **File Systems:** Storing directory and file structures (hierarchical structure).
- **Databases:** B-Trees and B+ Trees are advanced self-balancing trees used to index database tables for $O(\log N)$ retrieval.
- **Routing Tables:** Trie trees are used in networking routers for IP routing lookup.
- **Expression Trees:** Used by compilers to evaluate math equations and parse syntax.

---

## 🎯 Interview Notes & Cheat Sheet

1. **Balanced Trees (Self-Balancing):**
   - Skewed BSTs suffer from $O(N)$ performance. Standard solutions include **AVL Trees** and **Red-Black Trees** which guarantee $O(\log N)$ heights by performing self-balancing rotations during insertions and deletions.
2. **Successor / Predecessor Finding:**
   - Inorder Successor: Go right once, then go left as far as possible.
   - Inorder Predecessor: Go left once, then go right as far as possible.
3. **Recursive vs Iterative:**
   - Recursive tree algorithms are simple and intuitive but consume call stack memory. In interviews, you might be asked to implement traversals (like In-order) iteratively using an explicit Stack.
