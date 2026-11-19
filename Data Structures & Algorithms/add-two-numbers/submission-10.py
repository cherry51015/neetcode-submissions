# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=l1
        curr2=l2
        carr=0
        dummy=ListNode(0)
        curr=dummy
        while curr1 or curr2 or carr:
            c1=curr1.val if curr1 else 0
            c2=curr2.val if curr2 else 0

            num=carr+c1+c2
            carr=num//10
            d=num%10
            curr.next=ListNode(d)
            curr=curr.next
            if curr1:
                curr1=curr1.next
            if curr2:
                curr2=curr2.next
        return dummy.next

            


        