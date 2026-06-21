def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer n using recursion.
    
    Time Complexity: O(N) - N recursive calls.
    Space Complexity: O(N) - Stack frame memory for recursion.
    
    Args:
        n (int): A non-negative integer.
        
    Returns:
        int: The factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive relation


if __name__ == '__main__':
    # Interview-friendly test case/run
    try:
        user_input = input("Enter a non-negative integer: ")
        # Support running automatically for test automation
        n = int(user_input) if user_input.strip() else 5
        result = factorial(n)
        print(f"The factorial of {n} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
