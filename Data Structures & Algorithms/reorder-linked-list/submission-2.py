# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        shead=slow.next
        slow.next=None
        while shead:
            temp=shead.next
            shead.next=prev
            prev=shead
            shead=temp
        curr=head
        scurr=prev
        dummy=ListNode(0)
        x=dummy
        while scurr:
            temp=curr.next
            curr.next=scurr
            x.next=curr
            x=scurr
            scurr=scurr.next
            curr=temp
        x.next=curr


            


        
            
            
        
        