class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def detectCycle(head):
    slow = head
    fast = head

    # Step 1: Detect Cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    # No Cycle
    if fast is None or fast.next is None:
        return None

    # Step 2: Find Starting Node
    ptr = head

    while ptr != slow:
        ptr = ptr.next
        slow = slow.next

    return ptr


# ------------------ Input ------------------

n = int(input("Enter number of nodes: "))
arr = list(map(int, input("Enter node values: ").split()))

nodes = []

# Create Nodes
for value in arr:
    nodes.append(ListNode(value))

# Connect Nodes
for i in range(n - 1):
    nodes[i].next = nodes[i + 1]

head = nodes[0]

# Create Cycle
pos = int(input("Enter index where last node should point (-1 for no cycle): "))

if pos != -1:
    nodes[-1].next = nodes[pos]

# Detect Cycle
startNode = detectCycle(head)

if startNode:
    print("Cycle starts at node with value:", startNode.val)
else:
    print("No Cycle")