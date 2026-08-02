class Node:
    def __init__(self,key=0,value=0):
        self.key=key
        self.value=value
        self.prev=None
        self.nxt=None

class LRUCache:

    def __init__(self, capacity: int):
        self.head=Node()
        self.tail=Node()
        self.cap=capacity
        self.h={}
        self.head.nxt=self.tail
        self.tail.prev=self.head

    def insert(self,n):
        temp=self.tail.prev
        temp.nxt=n
        self.tail.prev=n
        n.nxt=self.tail
        n.prev=temp

    def remove(self,n):
        p=n.prev
        t=n.nxt
        if p and t:
           p.nxt=t
           t.prev=p



    def get(self, key: int) -> int:
        if key in self.h:
            node=self.h[key]
            self.remove(node)
            self.insert(node)
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        n=Node(key,value)
        if key in self.h:
            self.remove(self.h[key])
            del self.h[key]
        self.insert(n)
        self.h[key]=n
        if len(self.h)>self.cap:
            del self.h[self.head.nxt.key]
            self.remove(self.head.nxt)

        

        
        

        
