# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        node=head
        length=0
        while node:
            length+=1
            node=node.next
        x=length-n
        if x==0:
            return head.next
        curr=head
        prev=None
        target=0
        while curr:
            if target==x:
                prev.next=curr.next
                break
            else:
                prev=curr
                curr=curr.next
            target+=1
        return head
                

        