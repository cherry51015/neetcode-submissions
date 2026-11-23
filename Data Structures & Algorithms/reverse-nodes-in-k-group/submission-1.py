# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        node=head
        length=0
        while node:
            length+=1
            node=node.next
        n=length//k
        dummy=ListNode()
        dummy.next=head
        curr=head
        x=0
        prevfirst=dummy
        first=head
        prev=None
        while x!=n:
            y=0
            while y!=k:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
                y+=1
            prevfirst.next=prev
            prevfirst=first
            prev=None
            first=curr
            
            x+=1
        prevfirst.next=curr
        return dummy.next
        

            

        