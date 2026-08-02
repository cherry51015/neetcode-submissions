# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=0
        curr=head
        while curr:
            length+=1
            curr=curr.next
        n=length//k
        curr=head
        prev=None
        dummy=ListNode()
        prevgrouptail=dummy
        while n:
            tar=k
            tail=curr
            while tar and curr:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
                tar-=1
            prevgrouptail.next=prev
            tail.next=curr
            prevgrouptail=tail
            n-=1
            
        return dummy.next

                



        
        