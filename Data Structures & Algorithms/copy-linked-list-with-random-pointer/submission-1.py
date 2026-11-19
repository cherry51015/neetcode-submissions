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
        x=dummy
        curr=head
        h={}
        while curr:
            x.next=Node(curr.val)
            h[curr]=x.next
            x=x.next
            curr=curr.next
        curr=head
        copy=dummy.next
        while curr:
            if curr.random is None:
                copy.random=None
            else:
                copy.random=h[curr.random]
            curr=curr.next
            copy=copy.next
        return dummy.next

        
        
        



        