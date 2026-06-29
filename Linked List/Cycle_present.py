class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def hasCycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# -------- Input --------
n = int(input("Enter number of nodes: "))

arr = list(map(int, input("Enter node values: ").split()))

nodes = []

# Create nodes
for x in arr:
    nodes.append(ListNode(x))

# Connect nodes
for i in range(n - 1):
    nodes[i].next = nodes[i + 1]

head = nodes[0]

# Cycle input
pos = int(input("Enter index where last node should point (-1 for no cycle): "))

if pos != -1:
    nodes[-1].next = nodes[pos]

# Check cycle
if hasCycle(head):
    print("Cycle Present")
else:
    print("Cycle Not Present")