# 🕸️ Graph Implementations

This folder contains clean, standard Python implementations of graph data structures.

---

## 📈 Visual Representations

### Adjacency List
```text
0 -> [1, 2]
1 -> [0, 3, 4]
2 -> [0, 4]
3 -> [1]
4 -> [1, 2]
```

### Adjacency Matrix
```text
  0 1 2 3 4
0 0 1 1 0 0
1 1 0 0 1 1
2 1 0 0 0 1
3 0 1 0 0 0
4 0 1 1 0 0
```

---

## 📚 Concepts Covered

A Graph is a non-linear data structure consisting of nodes (vertices) and edges that connect them.

### 1. Adjacency List (`adjacency_list.py`)
- **Concept:** Represents a graph as a dictionary or array of lists. Each key/index represents a vertex, and the corresponding list contains its neighbors.
- **Properties:** Space-efficient for sparse graphs. Fast to iterate over neighbors of a vertex.

### 2. Adjacency Matrix (`adjacency_matrix.py`)
- **Concept:** A 2D array of size V x V where `matrix[i][j]` is 1 if there is an edge between vertex `i` and vertex `j`, and 0 otherwise.
- **Properties:** Fast $O(1)$ edge lookup. Consumes $O(V^2)$ space, making it better suited for dense graphs.

---

## ⚡ Complexity Analysis

| Graph Representation | Space Complexity | Add Vertex | Add Edge | Remove Edge | Query Edge |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Adjacency List** | $O(V + E)$ | $O(1)$ | $O(1)$ | $O(V)$ | $O(V)$ |
| **Adjacency Matrix** | $O(V^2)$ | $O(V^2)$ | $O(1)$ | $O(1)$ | $O(1)$ |

---

## 🎯 Interview Notes & Cheat Sheet

1. **When to use Adjacency List vs Matrix:**
   - Default to **Adjacency List** for most interview problems since real-world graphs are typically sparse, and algorithms like BFS/DFS are faster ($O(V+E)$).
   - Use **Adjacency Matrix** when the graph is dense (number of edges $E \approx V^2$) or when you need fast $O(1)$ edge weight lookups between any two vertices.
2. **Common Algorithms:**
   - **BFS (Breadth-First Search):** Used for finding the shortest path in unweighted graphs.
   - **DFS (Depth-First Search):** Used for cycle detection, topological sorting, and exploring all paths.
