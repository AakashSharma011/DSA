# 🥞 Stack & Queue Implementations

This folder contains clean, standard Python implementations of linear data structures with constrained access methods: Stack, Queue, Circular Queue, and Double-Ended Queue (Deque).

---

## 📈 Visual Representations

### Stack (LIFO - Last In, First Out)
```text
   |      |
   | [30] |  <- Top / Pop / Push
   | [20] |
   | [10] |
   +------+
```

### Queue (FIFO - First In, First Out)
```text
           [Enqueue] -> [Rear]  [30] [20] [10]  [Front] -> [Dequeue]
```

### Deque (Double-Ended Queue)
```text
   [Insert/Delete] <-> [Front]  [30] [20] [10]  [Rear] <-> [Insert/Delete]
```

---

## 📚 Concepts Covered

Linear data structures organize elements sequentially. Stacks and Queues constrain where insertion and deletion can occur to guarantee specific retrieval patterns.

### 1. Stack (LIFO - Last In, First Out)
- **Concept:** Elements are added and removed from the same end, called the **Top**.
- **Operations:** 
  - `push(value)`: Add an element to the top.
  - `pop()`: Remove and return the top element.
  - `peek()`: View the top element without removing it.

### 2. Queue (FIFO - First In, First Out)
- **Concept:** Elements are added at the **Rear** (enqueue) and removed from the **Front** (dequeue).
- **Operations:**
  - `insert(value)` / `enqueue(value)`: Add an element to the rear.
  - `delete()` / `dequeue()`: Remove and return the front element.

### 3. Circular Queue (Ring Buffer)
- **Concept:** A queue that utilizes a fixed-size array where the last position connects back to the first position. This avoids the waste of memory in basic array-based queues after elements are dequeued.
- **Formulas:**
  - Full Condition: `(rear + 1) % size == front`
  - Empty Condition: `front == -1`
  - Rear Wrap-around: `rear = (rear + 1) % size`

### 4. Deque (Double-Ended Queue)
- **Concept:** A sequence container that allows insertion and deletion from both the **Front** and the **Rear** ends.
- **Operations:**
  - `insertAtFront(value)`, `insertAtLast(value)`
  - `deleteAtFront()`, `deleteAtEnd()`

---

## ⚡ Complexity Analysis

| Data Structure | Operation | Time Complexity | Space Complexity | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Stack** | Push | $O(1)$ | $O(N)$ | $O(1)$ amortized if using dynamic array |
| **Stack** | Pop | $O(1)$ | $O(1)$ | Accesses top element instantly |
| **Queue** | Enqueue | $O(1)$ | $O(N)$ | Appends at rear |
| **Queue** | Dequeue | $O(1)$ | $O(1)$ | $O(N)$ in standard python list pop(0) due to shift. This is resolved with circular arrays or linked lists. |
| **Circular Queue** | Enqueue / Dequeue | $O(1)$ | $O(\text{fixed\_size})$ | Highly efficient memory footprint |
| **Deque** | Insert / Delete (either end) | $O(1)$ | $O(N)$ | Combines LIFO and FIFO qualities |

---

## 🌐 Real-World Applications

- **Stack:**
  - **Undo/Redo Mechanisms:** Tracking states in word processors or design software.
  - **Call Stack:** Managing function execution inside language runtimes.
  - **Browser History:** Storing visited URLs to allow backtracking.
  - **Expression Parsing:** Compilers resolving syntax (e.g. parenthesis matching, postfix evaluation).

- **Queue:**
  - **CPU Scheduling:** Managing ready tasks in multi-tasking operating systems.
  - **Print Spooler:** Standard printer request buffering.
  - **Message Queues:** Asynchronous message brokers (RabbitMQ, Kafka) handling high load requests.

- **Circular Queue:**
  - **Traffic Lights:** Cycle management.
  - **Audio/Video Streaming:** Playing media while buffering new packets sequentially.

- **Deque:**
  - **Job-Stealing Algorithms:** Distributed scheduling (A-Steal scheduler).
  - **Undo-Redo History Limits:** Preserving the last $N$ operations while purging older ones.

---

## 🎯 Interview Notes & Cheat Sheet

1. **Stack using List in Python:**
   - Standard Python list `.append()` and `.pop()` operate in $O(1)$ amortized time.
   - However, inserting/removing from the beginning `.insert(0, value)` takes $O(N)$ time.
2. **Standard Queue Shift:**
   - Using a normal list for a queue where `.pop(0)` is used incurs $O(N)$ complexity because all subsequent elements must be shifted in memory.
   - For high-performance queues in Python, use `collections.deque`.
3. **Common Interview Questions:**
   - *Implement Stack using Queues* and vice-versa.
   - *Valid Parentheses* (e.g., LeetCode 20) - always solved using a Stack.
   - *Sliding Window Maximum* - solved efficiently using a Monotonic Deque.
   - *Min Stack* - maintaining minimum value at $O(1)$ time alongside standard stack operations.
