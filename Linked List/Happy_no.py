def getNext(n):
    total = 0

    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10

    return total


def isHappy(n):
    slow = n
    fast = n

    while True:
        slow = getNext(slow)                 # 1 step
        fast = getNext(getNext(fast))        # 2 steps

        if slow == fast:
            break

    return slow == 1


# Driver Code
n = int(input("Enter a number: "))

if isHappy(n):
    print("Happy Number")
else:
    print("Not Happy Number")