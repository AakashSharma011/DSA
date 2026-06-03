def selection_sort(arr: list[int]) -> list[int]:
    """
    Sorts a list of integers in ascending order using the Selection Sort algorithm.
    
    Time Complexity:
        - Best Case: O(N^2)
        - Average Case: O(N^2)
        - Worst Case: O(N^2)
    Space Complexity: O(1) auxiliary space (in-place sorting).
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == '__main__':
    # Interactive driver code
    try:
        user_input = input("Enter the elements of the array separated by space: ")
        if user_input.strip():
            elements = list(map(int, user_input.split()))
            print(f"Original Array: {elements}")
            sorted_arr = selection_sort(elements)
            print(f"Sorted Array:   {sorted_arr}")
        else:
            print("No elements entered. Running default test:")
            default_test = [64, 25, 12, 22, 11]
            print(f"Original Array: {default_test}")
            print(f"Sorted Array:   {selection_sort(default_test)}")
    except ValueError:
        print("Invalid input. Please enter space-separated integers only.")
