# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len=0
        curr=head
        while curr:
            len+=1
            curr=curr.next
        x=len-n
        if x==0 :
            return head.next
        tar=0
        curr=head
        prev=None
        while curr:
            if tar==x and prev:
                prev.next=curr.next
        
            tar+=1
            prev=curr
            curr=curr.next
        return head

            
        

        