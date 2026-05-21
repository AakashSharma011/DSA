# 🔗 Linked List Implementations

This folder contains clean, standard Python implementations of linear linked data structures: Singly Linked List, Doubly Linked List, and Circular Singly Linked List.

---

## 📚 Concepts Covered

A Linked List is a linear data structure where elements are not stored in contiguous memory locations. Instead, each element (node) consists of:
1. **Data:** The value stored.
2. **Pointer(s):** Reference link(s) to other node(s).

### 1. Singly Linked List (`singly_ll.py`)
- **Concept:** Each node points only to the next node in the chain. The last node points to `None`.
- **Properties:** Forward traversal only. Low memory overhead per node.

### 2. Doubly Linked List (`doubly_ll.py`)
- **Concept:** Each node contains two pointers: `next` pointing to the next node, and `prev` pointing to the previous node.
- **Properties:** Bidirectional traversal. Deletion of a node is easier since you have immediate access to its predecessor, but it consumes more memory.

### 3. Circular Linked List (`circular_ll.py`)
- **Concept:** The last node's `next` pointer refers back to the first node (`head`), forming a continuous cycle.
- **Properties:** Infinite traversal without encountering a boundary. Very useful for circular scheduling.

---

## ⚡ Complexity Analysis

| Linked List Type | Operation | Time Complexity | Space Complexity | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Singly LL** | Access / Search | $O(N)$ | $O(1)$ | Must traverse linearly from Head |
| **Singly LL** | Insert / Delete (Head) | $O(1)$ | $O(1)$ | Re-link Head reference |
| **Singly LL** | Insert / Delete (End) | $O(N)$ | $O(1)$ | Need to traverse to end unless tail pointer is maintained |
| **Doubly LL** | Insert / Delete (Node known) | $O(1)$ | $O(1)$ | No need to search predecessor |
| **Doubly LL** | Bidirectional traversal | $O(N)$ | $O(1)$ | Can traverse backwards using `.prev` |
| **Circular LL** | Full Traversal / Search | $O(N)$ | $O(1)$ | Care must be taken to stop when head is reached again |

---

## 🌐 Real-World Applications

- **Singly Linked List:**
  - **Graph Representation:** Adjacency list representation uses singly linked lists.
  - **Dynamic Memory Allocation:** Used by operating systems to keep track of free blocks.
- **Doubly Linked List:**
  - **Browser Navigation:** Going back (`.prev`) and forward (`.next`) through history.
  - **LRU Cache (Least Recently Used):** A doubly linked list combined with a hash map provides $O(1)$ access and removal.
- **Circular Linked List:**
  - **Round-Robin Scheduling:** Operating systems allocate CPU time-slices to tasks sequentially in a circular loop.
  - **Multiplayer Games:** Cycling active player turns repeatedly.

---

## 🎯 Interview Notes & Cheat Sheet

1. **Cycle Detection (Floyd's Cycle-Finding Algorithm):**
   - The famous "Tortoise and Hare" algorithm uses a slow pointer (1 step) and a fast pointer (2 steps) to detect if a cycle exists in a linked list. Time Complexity: $O(N)$, Space: $O(1)$.
2. **Reverse a Linked List:**
   - A highly common question. Involves keeping track of three pointers: `prev`, `curr`, and `next_node`, and reversing links in place in a single pass.
3. **Dummy Node Technique:**
   - Creating a temporary dummy head node `dummy = Node(0)` simplifies edge cases (like inserting at the beginning or deleting the head node).
4. **Key Differences:**
   - Arrays provide $O(1)$ indexing but expensive $O(N)$ insertions/deletions at arbitrary positions.
   - Linked lists have slow $O(N)$ indexing but fast $O(1)$ pointer-based insertions/deletions.
