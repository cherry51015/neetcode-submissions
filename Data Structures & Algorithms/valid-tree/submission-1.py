class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n!=len(edges)+1:
            return False
        graph=defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        v=set()
        def dfs(node,parent):
            v.add(node)
            for nei in graph[node]:
                if nei not in v:
                    if dfs(nei,node):
                        return True
                elif nei!=parent:
                    return True
            return False
        if dfs(0,0):
            return False
        if len(v)!=n:
            return False
        return True
                
            

        