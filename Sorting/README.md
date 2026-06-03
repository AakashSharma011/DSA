# 📶 Sorting Algorithms

This folder contains clean, standard Python implementations of fundamental sorting algorithms: Bubble Sort and Selection Sort.

---

## 📈 Visual Representations

### 1. Bubble Sort
In each pass, adjacent elements are compared and swapped if they are in the wrong order. The largest element "bubbles" up to its correct position at the end.
```text
Pass 1: [5, 1, 4, 2, 8]  -->  Compare 5 & 1 (swap)  -->  [1, 5, 4, 2, 8]
        [1, 5, 4, 2, 8]  -->  Compare 5 & 4 (swap)  -->  [1, 4, 5, 2, 8]
        [1, 4, 5, 2, 8]  -->  Compare 5 & 2 (swap)  -->  [1, 4, 2, 5, 8]
        [1, 4, 2, 5, 8]  -->  Compare 5 & 8 (no swap) -->  [1, 4, 2, 5, 8]
(The element 8 is now in its sorted position.)
```

### 2. Selection Sort
Divides the array into sorted and unsorted parts. Repeatedly finds the minimum element from the unsorted part and swaps it with the first element of the unsorted part.
```text
Initial Array: [29, 10, 14, 37, 13]
Pass 1 (Min is 10): Swap 29 & 10  -->  [10 | 29, 14, 37, 13]
Pass 2 (Min is 13): Swap 29 & 13  -->  [10, 13 | 14, 37, 29]
Pass 3 (Min is 14): No swap needed -->  [10, 13, 14 | 37, 29]
Pass 4 (Min is 29): Swap 37 & 29  -->  [10, 13, 14, 29 | 37]
```

---

## 📚 Concepts Covered

Sorting is the process of arranging data in a systematic order (usually ascending or descending).

### 1. Bubble Sort (`bubble_sort.py`)
- **Concept:** Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
- **Optimization:** A boolean flag `swapped` is used. If a full pass completes without any swaps, the list is already sorted, allowing the algorithm to terminate early.

### 2. Selection Sort (`selection_sort.py`)
- **Concept:** Selects the smallest element from the unsorted sub-array and places it at the beginning. It reduces the number of swaps compared to Bubble Sort.

---

## ⚡ Complexity Analysis

| Algorithm | Best Case Time | Average Case Time | Worst Case Time | Space Complexity | Stable? | In-Place? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Bubble Sort** | $O(N)$ (optimized) | $O(N^2)$ | $O(N^2)$ | $O(1)$ | Yes | Yes |
| **Selection Sort** | $O(N^2)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | No | Yes |

---

## 🌐 Real-World Applications

- **Bubble Sort:** Useful when the input is already sorted or nearly sorted, or in systems where code footprint is extremely constrained.
- **Selection Sort:** Useful when writing to memory is highly expensive (since it makes at most $O(N)$ swaps).

---

## 🎯 Interview Notes & Cheat Sheet

1. **Stability:**
   - A sorting algorithm is **stable** if it preserves the relative order of duplicate elements. Bubble Sort is stable because it only swaps if `arr[j] > arr[j+1]`. Selection Sort is **unstable** because swap operations can change the relative order of identical elements.
2. **Number of Swaps:**
   - Bubble Sort can make up to $O(N^2)$ swaps in the worst case.
   - Selection Sort makes at most $O(N)$ swaps, which makes it preferable when write operations are expensive.
3. **Common Interview Questions:**
   - *Sort an array of 0s, 1s, and 2s (Dutch National Flag Algorithm)*.
   - *Merge two sorted arrays with $O(1)$ extra space*.
   - *Find the K-th largest element in an array (QuickSelect)*.
