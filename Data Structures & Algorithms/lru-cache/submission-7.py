class ListNode:
    def __init__(self,key=0,value=0):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None
class LRUCache:

    def __init__(self, capacity: int):
        self.head=ListNode()
        self.tail=ListNode()
        self.h={}
        self.head.next=self.tail
        self.tail.prev=self.head
        self.capacity=capacity

    def insert(self,key,value):
        if key in self.h:
            node=self.h[key]
        else:
            node=ListNode(key,value)
        node.next=self.head.next
        node.prev=self.head
        node.prev.next=node
        node.next.prev=node
    def delete(self,key):
        node=self.h[key]
        node.prev.next=node.next
        node.next.prev=node.prev
       

    def get(self, key: int) -> int:
        if key not in self.h:
            return -1
        self.delete(key)
        self.insert(key,self.h[key].value)
        return self.h[key].value

        

    def put(self, key: int, value: int) -> None:
        if key not in self.h:
            node=ListNode(key,value)
            self.h[key]=node
        else:
            self.delete(key)
            self.h[key].value=value
        self.insert(key,value)

        while len(self.h)>self.capacity:
            node=self.tail.prev
            self.delete(node.key)
            del self.h[node.key]
        
       
        
