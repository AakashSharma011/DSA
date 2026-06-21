# 🚀 Data Structures and Algorithms (DSA) in Python

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![DSA Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange.svg)]()

Welcome to the **Data Structures and Algorithms (DSA) in Python** repository! This project serves as a comprehensive, well-structured, and highly optimized reference library for fundamental computer science data structures and algorithms. 

Designed specifically for placement preparation, technical interview review, and self-paced learning, this repository emphasizes **clean implementation**, **optimal time/space complexities**, and **recruiter-friendly documentation**.

---

## 🎯 Why This Repository Exists

Understanding DSA is the bedrock of writing efficient software. The goals of this project are:
1. **Clean Code & Best Practices:** Well-documented Python code conforming to industry standards, using type-hints and proper encapsulation.
2. **Interview Preparedness:** Direct mapping of implementation structures to frequent LeetCode, HackerRank, and FAANG/MAANG interview patterns.
3. **Core Foundations:** Building deep intuition on memory management, pointer manipulation, and sequential versus non-sequential linear/hierarchical architectures.

---

## 📂 Repository Structure

The codebase is organized modularly by topic to ensure scalability as more concepts are added:

```text
DSA/
│
├── Stack & Queue/         # Linear Data Structures with constrained access
│   ├── stack.py           # Last-In-First-Out (LIFO) stack
│   ├── queue.py           # First-In-First-Out (FIFO) queue
│   ├── circular_queue.py  # Ring buffer implementation of queue
│   ├── dequeue.py         # Double-ended queue (Deque)
│   └── README.md          # Technical concepts & time complexities
│
├── Linked List/           # Dynamic node-pointer based sequences
│   ├── singly_ll.py       # Forward-linked chain
│   ├── doubly_ll.py       # Bidirectional linked nodes
│   ├── circular_ll.py     # Circularly linked nodes (ends join head)
│   └── README.md          # Visualizations & operations complexity
│
├── Recursion/             # Self-calling functions and recursive paradigms
│   ├── factorial.py       # Linear recursive factorial
│   ├── fibonacci.py       # Tree-recursive Fibonacci sequence
│   └── README.md          # Call stack visualizations & recursion depth notes
│
├── Trees/                 # Hierarchical nodes and traversals
│   ├── BST/               # Binary Search Tree specific implementations
│   │   ├── bst.py         # BST basic insertion and search
│   │   ├── deletion_bst.py# Node deletion algorithm in BST
│   │   ├── ceil_in_bst.py # Ceil node finder in BST
│   │   ├── floor_in_bst.py# Floor node finder in BST
│   │   └── traversal.py   # Pre-order, In-order, and Post-order traversals
│   └── README.md          # Tree diagrams, traversal lists, and complexities
│
├── Sorting/               # Data arrangement algorithms
│   ├── bubble_sort.py     # Optimized bubble sort implementation
│   ├── selection_sort.py  # Standard selection sort implementation
│   └── README.md          # Sorting details & stability cheat sheets
│
├── Graphs/                # Non-linear connected architectures
│   ├── adjacency_list.py  # Adjacency list representation
│   ├── adjacency_matrix.py# Adjacency matrix representation
│   └── README.md          # Graph representations, search notes & complexity
│
├── .gitignore             # Standard Python ignore rules
└── README.md              # Project overview & roadmap (this file)
```

---

## 📊 Learning Progress Tracker

Below is the status of implementations currently covered in the repository.

| Category | Topic / Structure | File Path | Status | Key Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **Stack & Queue** | Stack (LIFO) | [`stack.py`](./Stack%20%26%20Queue/stack.py) | 🟢 Complete | Push/Pop: $O(1)$ |
| **Stack & Queue** | Queue (FIFO) | [`queue.py`](./Stack%20%26%20Queue/queue.py) | 🟢 Complete | Enqueue/Dequeue: $O(1)$ |
| **Stack & Queue** | Circular Queue | [`circular_queue.py`](./Stack%20%26%20Queue/circular_queue.py) | 🟢 Complete | Enqueue/Dequeue: $O(1)$ |
| **Stack & Queue** | Double Ended Queue | [`dequeue.py`](./Stack%20%26%20Queue/dequeue.py) | 🟢 Complete | Insert/Delete (Ends): $O(1)$ |
| **Linked List** | Singly Linked List | [`singly_ll.py`](./Linked%20List/singly_ll.py) | 🟢 Complete | Traverse: $O(N)$, Insert/Delete: $O(1)$ |
| **Linked List** | Doubly Linked List | [`doubly_ll.py`](./Linked%20List/doubly_ll.py) | 🟢 Complete | Bidirectional traverse: $O(N)$ |
| **Linked List** | Circular Linked List | [`circular_ll.py`](./Linked%20List/circular_ll.py) | 🟢 Complete | Ring structure |
| **Recursion** | Factorial | [`factorial.py`](./Recursion/factorial.py) | 🟢 Complete | Time: $O(N)$ \| Space: $O(N)$ |
| **Recursion** | Fibonacci | [`fibonacci.py`](./Recursion/fibonacci.py) | 🟢 Complete | Time: $O(2^N)$ \| Space: $O(N)$ |
| **Trees** | Binary Search Tree | [`bst.py`](./Trees/BST/bst.py) | 🟢 Complete | Insert/Search: $O(\log N)$ average |
| **Trees** | BST Deletion | [`deletion_bst.py`](./Trees/BST/deletion_bst.py) | 🟢 Complete | Delete Node: $O(\log N)$ average |
| **Trees** | BST Ceil | [`ceil_in_bst.py`](./Trees/BST/ceil_in_bst.py) | 🟢 Complete | Ceil: $O(\log N)$ average |
| **Trees** | BST Floor | [`floor_in_bst.py`](./Trees/BST/floor_in_bst.py) | 🟢 Complete | Floor: $O(\log N)$ average |
| **Trees** | Tree Traversal | [`traversal.py`](./Trees/BST/traversal.py) | 🟢 Complete | Pre/In/Post traversal: $O(N)$ |
| **Sorting** | Bubble Sort | [`bubble_sort.py`](./Sorting/bubble_sort.py) | 🟢 Complete | Time: $O(N)$ best, $O(N^2)$ worst |
| **Sorting** | Selection Sort | [`selection_sort.py`](./Sorting/selection_sort.py) | 🟢 Complete | Time: $O(N^2)$ best/worst |
| **Graphs** | Adjacency List | [`adjacency_list.py`](./Graphs/adjacency_list.py) | 🟢 Complete | Space: $O(V + E)$ |
| **Graphs** | Adjacency Matrix | [`adjacency_matrix.py`](./Graphs/adjacency_matrix.py) | 🟢 Complete | Space: $O(V^2)$ |

---

## 💡 Learning Goals & Interview Preparation Notes

### 🧠 Core Concepts To Focus On:
- **Pointer Manipulation:** Managing references (`next` and `prev`) in linked lists without causing dangling pointers or cycles.
- **Ring Buffer Logic:** Implementing index wrapping `(index + 1) % size` to optimize space in Circular Queues.
- **Recursion Limits:** Being aware of recursion depth and the stack trace when implementing recursive solutions (e.g. Factorial, Fibonacci).
- **BST Balancing:** Understanding that simple BST operations degrade to $O(N)$ in skewed trees, which leads to the necessity of AVL or Red-Black Trees.
- **Graph Representation Choice:** Adjacency List is optimal for sparse graphs (most interview problems); Adjacency Matrix is best for dense graphs or fast edge weight lookups.

### ⏱️ Time Complexity Quick Cheat-Sheet
- **Arrays/Lists:** Access: $O(1)$ | Search: $O(N)$ | Insertion: $O(N)$
- **Linked Lists:** Access: $O(N)$ | Search: $O(N)$ | Insertion (at head/given node): $O(1)$
- **Stack / Queue:** All insertion/deletion operations: $O(1)$
- **Binary Search Tree:** Average search/insert/delete: $O(\log N)$ | Worst-case: $O(N)$
- **Graph BFS / DFS:** $O(V + E)$ using Adjacency List, $O(V^2)$ using Adjacency Matrix.

---

## 🛠️ Contribution Guidelines

Contributions are welcome! If you want to add new data structures, solve classical algorithms problems, or improve documentation:

1. **Fork the Repository**
2. **Create a Feature Branch:** `git checkout -b feature/AmazingDataStructure`
3. **Commit Your Changes:** `git commit -m 'Add some AmazingDataStructure'`
4. **Push to the Branch:** `git push origin feature/AmazingDataStructure`
5. **Open a Pull Request**

Please ensure your code is clean, utilizes proper docstrings, and includes inline comments explaining the logic.

---

## 🗺️ Roadmap & Future Plans
- [x] Add Binary Search Tree (BST) operations and tree traversals
- [x] Add basic Recursion implementations (Factorial, Fibonacci)
- [x] Implement basic Graph representations (Adjacency List, Adjacency Matrix)
- [x] Add elementary Sorting algorithms (Bubble Sort, Selection Sort)
- [ ] Add advanced Graph Algorithms (BFS, DFS, Dijkstra, Kruskal's)
- [ ] Add advanced Sorting & Searching (QuickSort, MergeSort, Binary Search)
- [ ] Add Dynamic Programming (DP) paradigms

---

*Made with 💻 and 🐍 for interview preparation and clean engineering.*
