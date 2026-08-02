class DSU:
    def __init__(self,n):
        self.parent=list(range(n))
        self.size=[1]*n
    def find(self,node):
        if self.parent[node]==node:
            return node
        self.parent[node]=self.find(self.parent[node])
        return self.parent[node]
    def union(self,u,v):
        pu=self.find(u)
        pv=self.find(v)
        if pu==pv:
            return False
        if self.size[pu]<self.size[pv]:
            pu,pv=pv,pu
        self.parent[pv]=pu
        self.size[pu]+=self.size[pv]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu=DSU(len(edges)+1)
        for u,v in edges:
            if not dsu.union(u,v):
                ans=[u,v]
        return ans
        

        