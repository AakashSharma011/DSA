class Solution(object):
    def rotateRight(self, head, k):
        if head is None or head.next is None or k == 0:
            return head

        # Find length and last node
        n = 1
        tail = head

        while tail.next:
            tail = tail.next
            n += 1

        # Reduce unnecessary rotations
        k = k % n

        if k == 0:
            return head

        # Make circular
        tail.next = head

        # Find new tail
        steps = n - k
        new_tail = head

        for _ in range(steps - 1):
            new_tail = new_tail.next

        # New head
        new_head = new_tail.next

        # Break the circle
        new_tail.next = None

        return new_head