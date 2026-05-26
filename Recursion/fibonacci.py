def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number using recursion.
    
    Time Complexity: O(2^N) - Exponential time due to redundant subproblems.
    Space Complexity: O(N) - Stack frame memory proportional to depth of tree.
    
    Args:
        n (int): Position of the Fibonacci number to find (0-indexed).
        
    Returns:
        int: The nth Fibonacci number.
    """
    if n < 0:
        raise ValueError("Fibonacci position must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    # Interview-friendly test case/run
    try:
        user_input = input("Enter a position: ")
        # Support running automatically for test automation
        n = int(user_input) if user_input.strip() else 6
        result = fibonacci(n)
        print(f"The {n}th Fibonacci number is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
