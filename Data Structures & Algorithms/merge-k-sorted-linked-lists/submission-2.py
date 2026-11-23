# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h=[]
        r=len(lists)
        c=len(lists)
        dummy=ListNode()
        curr=dummy
        for i in range(r):
            if lists[i]:
                heapq.heappush(h,(lists[i].val,i,lists[i]))
        while h:
            value,row,node=heapq.heappop(h)
            if node.next:
                heapq.heappush(h,(node.next.val,row,node.next))
            node.next=None
            curr.next=node
            curr=curr.next
        return dummy.next
        


          

        