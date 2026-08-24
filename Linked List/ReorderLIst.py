# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):

    def reverse(self, head):
        curr = head
        prev = None

        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def reorderList(self, head):
        if head is None or head.next is None:
            return

        slow = head
        fast = head

        # Find middle
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Split from middle
        second = slow.next
        slow.next = None

        # Reverse second half
        second = self.reverse(second)

        # Alternate merge
        ptr1 = head
        ptr2 = second

        while ptr2:
            ptr1_next = ptr1.next
            ptr2_next = ptr2.next

            ptr1.next = ptr2
            ptr2.next = ptr1_next

            ptr1 = ptr1_next
            ptr2 = ptr2_next