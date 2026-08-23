lass Solution(object):
    def reverse(self,head):
        curr = head
        prev = None

        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def isPalindrome(self, head):
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next


        second=self.reverse(slow)
        ptr1=head
        ptr2=second

        while ptr2 is not None:
            if ptr1.val!=ptr2.val:
                return False

            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return True