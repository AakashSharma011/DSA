
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


# Helper function to create linked list
def create_linked_list(arr):
    dummy = ListNode()
    current = dummy

    for num in arr:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


# Helper function to print linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()


# Test
arr = [1, 1, 2, 3, 3, 4, 4, 5]

head = create_linked_list(arr)

print("Original List:")
print_linked_list(head)

sol = Solution()
head = sol.deleteDuplicates(head)

print("After Removing Duplicates:")
print_linked_list(head)