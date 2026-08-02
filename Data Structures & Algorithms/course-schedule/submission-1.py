class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        for i,j in prerequisites:
            graph[j].append(i)
        path=set()
        def dfs(node):
            if node in path:
                return False
            path.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            path.remove(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
    

                
        