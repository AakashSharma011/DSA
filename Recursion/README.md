# 🔄 Recursion Implementations

This folder contains clean, standard Python implementations of fundamental recursive algorithms: Factorial Calculation and Fibonacci Sequence.

---

## 📈 Visual Representations

### 1. Factorial Call Stack (`factorial(3)`)
Each recursive call pauses execution of the caller and pushes a new frame onto the system call stack until the base case is reached.

```text
CALL STACK (Push phase)                      RETURN VALUE (Pop phase)
┌──────────────────────────────────────┐     ┌───────────────────────┐
│ factorial(3)                         │     │ returns 3 * 2 = 6     │  ▲
│   └── calls factorial(2)             │     │   ▲                   │  │
│         └── calls factorial(1)       │ ──> │   └── returns 2 * 1=2 │  │ Resolves
│               └── calls factorial(0) │     │         └── returns 1 │  │ upwards
└──────────────────────────────────────┘     └───────────────────────┘
                     │                                     ▲
                     └───────── Base Case Reached ─────────┘
```

### 2. Fibonacci Recursion Tree (`fibonacci(4)`)
Unlike linear recursion (Factorial), Fibonacci results in binary tree-structured recursion. This leads to redundant subproblems.

```text
                         fibonacci(4)
                        /            \
             fibonacci(3)            fibonacci(2)
             /          \            /          \
      fibonacci(2)   fib(1)       fib(1)      fib(0)
      /          \
   fib(1)      fib(0)
```

---

## 📚 Concepts Covered

Recursion is a programming technique where a function calls itself to solve a smaller instance of the same problem. Any recursive function must have two primary parts:
1. **Base Case (Terminating Case):** The condition under which the function stops calling itself. Without a base case, recursion leads to infinite execution and a `RecursionError` (Stack Overflow).
2. **Recursive Case / Relation:** The logic that reduces the problem into smaller subproblems and calls the function recursively.

### 1. Factorial (`factorial.py`)
- **Mathematical Definition:** $N! = N \times (N-1)!$ where $0! = 1$ and $1! = 1$.
- **Mechanism:** Linear recursion. Each call reduces $N$ by 1 until it hits the base case $N \le 1$.

### 2. Fibonacci (`fibonacci.py`)
- **Mathematical Definition:** $F(N) = F(N-1) + F(N-2)$ where $F(0) = 0, F(1) = 1$.
- **Mechanism:** Binary tree recursion. Each call spawns two more calls, creating an exponential growth in the number of execution frames.

---

## ⚡ Complexity Analysis

| Algorithm | File Path | Time Complexity | Space Complexity | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Factorial** | [`factorial.py`](./factorial.py) | $O(N)$ | $O(N)$ | $N$ total stack frames are pushed onto the call stack. |
| **Fibonacci** | [`fibonacci.py`](./fibonacci.py) | $O(2^N)$ | $O(N)$ | Highly inefficient due to redundant calculations. Space complexity is $O(N)$ because the maximum depth of the recursion tree is $N$. |

---

## 🌐 Real-World Applications

- **Backtracking Algorithms:** Used in solving Sudoku, N-Queens, maze pathfinding, and generating permutations/combinations.
- **Divide and Conquer:** Standard algorithms like MergeSort, QuickSort, and Binary Search rely heavily on recursion.
- **Tree and Graph Traversals:** DFS (Depth-First Search) and BST traversals are naturally recursive because trees are recursive structures.

---

## 🎯 Interview Notes & Cheat Sheet

1. **Stack Overflow:**
   - In Python, the default recursion limit is 1000. If your recursion goes deeper, it raises `RecursionError`.
   - Limit can be modified using `sys.setrecursionlimit(limit)` but should generally be avoided by writing iterative alternatives or utilizing tail call optimization where supported.
2. **Memoization (Dynamic Programming):**
   - The recursive Fibonacci implementation is slow ($O(2^N)$). We can optimize it to $O(N)$ time and $O(N)$ space using **Memoization** (storing values in a hash map/array to avoid recalculating) or to $O(N)$ time and $O(1)$ space using an **Iterative Bottom-Up** approach.
3. **Tail Recursion:**
   - A recursive function is tail-recursive if the recursive call is the final statement executed by the function. Python does **not** perform Tail Call Optimization (TCO) out-of-the-box, unlike some functional programming languages (Lisp, Haskell).
