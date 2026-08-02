"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy=Node(0)
        tail1=dummy

        curr=head
        h={}
        while curr:
            newnode=Node(curr.val)
            tail1.next=newnode
            h[curr]=newnode
            curr=curr.next
            tail1=tail1.next

        curr=head
        tail2=dummy.next
        while curr:
            if curr.random:
                tail2.random=h[curr.random]
            else:
                tail2.random=None
            curr=curr.next
            tail2=tail2.next
        return dummy.next
        
            



        