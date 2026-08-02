# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
  
        curr=slow.next
        slow.next=None
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        head2=prev
        
        node=head
        rnode=head2
        while node and rnode:
            temp=node.next
            node.next=rnode
            temp2=rnode.next
            rnode.next=temp
            rnode=temp2
            node=temp
        return 


        





