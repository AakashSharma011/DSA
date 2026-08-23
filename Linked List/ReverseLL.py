class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(head):
    curr = head
    prev = None

    while curr != None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


def print_list(head):
    curr = head

    while curr != None:
        print(curr.data, end=" -> ")
        curr = curr.next

    print("None")


# Create linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("Original:")
print_list(head)

head = reverse(head)

print("Reversed:")
print_list(head)