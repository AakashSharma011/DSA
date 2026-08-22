head = [3,2,0,-4]
pos = 1
class Solution(object):
    def detectCycle(self, head):
        slow=head
        fast=head
        while fast is  not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                ptr1=head
                ptr2=slow
                while ptr1!=ptr2:
                    ptr1=ptr1.next
                    ptr2=ptr2.next
                return ptr1  

        return None

print(Solution().detectCycle(head))