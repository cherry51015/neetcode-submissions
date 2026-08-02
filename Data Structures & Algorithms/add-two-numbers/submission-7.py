# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        tail=dummy
        c=0
        curr1=l1
        curr2=l2
        while curr1 or curr2 or c:
            x=curr1.val if curr1 else 0
            y=curr2.val if curr2 else 0
            d=x+y+c
            c=d//10
            tail.next=ListNode(d%10)
            if curr1:
                curr1=curr1.next
            if curr2:
                curr2=curr2.next
            tail=tail.next
                
        return dummy.next
            

        