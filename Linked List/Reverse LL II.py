class Solution(object):
    def reverseBetween(self, head, left, right):
        if head is None or left ==right:
            return head
        
        t=head
        before=None
        pos=1

        while t is not None and pos<left:
            before=t
            t=t.next
            pos+=1

        left_node=t

        curr=t
        prev=None
        times=right-left+1
        while times>0:
            next_node = curr.next
            
            curr.next=prev
            prev=curr
            curr= next_node

            times-=1
        
        if before is not None:
            before.next=prev
        else:
            head=prev
        
        left_node.next=curr
        return head
        