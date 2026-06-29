class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def middleNode(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


# ---------------- Input ----------------

n = int(input("Enter number of nodes: "))
arr = list(map(int, input("Enter node values: ").split()))

nodes = []

for value in arr:
    nodes.append(ListNode(value))

for i in range(n - 1):
    nodes[i].next = nodes[i + 1]

head = nodes[0]

mid = middleNode(head)

print("Middle Node:", mid.val)