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
        while curr1 and curr2:
            num=carr+curr1.val+curr2.val
            carr=num//10
            d=num%10
            curr.next=ListNode(d)
            curr=curr.next
            curr1=curr1.next
            curr2=curr2.next
        while curr1:
            num=curr1.val+carr
            carr=num//10
            d=num%10
            curr.next=ListNode(d)
            curr=curr.next
            curr1=curr1.next
        while curr2:
            num=curr2.val+carr
            carr=num//10
            d=num%10
            curr.next=ListNode(d)
            curr=curr.next
            curr2=curr2.next

        if carr:
            curr.next=ListNode(carr)
        return dummy.next

            


        