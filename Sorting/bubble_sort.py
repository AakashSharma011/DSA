def bubble_sort(arr: list[int]) -> list[int]:
    """
    Sorts a list of integers in ascending order using the Bubble Sort algorithm.
    Optimized with a swapped flag to stop early if the list becomes sorted.
    
    Time Complexity:
        - Best Case: O(N) when the array is already sorted.
        - Average Case: O(N^2)
        - Worst Case: O(N^2)
    Space Complexity: O(1) auxiliary space (in-place sorting).
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
    return arr


if __name__ == '__main__':
    # Interactive driver code
    try:
        user_input = input("Enter the elements of the array separated by space: ")
        if user_input.strip():
            elements = list(map(int, user_input.split()))
            print(f"Original Array: {elements}")
            sorted_arr = bubble_sort(elements)
            print(f"Sorted Array:   {sorted_arr}")
        else:
            print("No elements entered. Running default test:")
            default_test = [64, 34, 25, 12, 22, 11, 90]
            print(f"Original Array: {default_test}")
            print(f"Sorted Array:   {bubble_sort(default_test)}")
    except ValueError:
        print("Invalid input. Please enter space-separated integers only.")