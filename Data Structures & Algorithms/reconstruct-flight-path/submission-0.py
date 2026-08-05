class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        graph=defaultdict(list)
        for i,j in tickets:
            graph[i].append(j)
        ans=[]
        def dfs(node):
            while graph[node]:
                nei=graph[node].pop()
                dfs(nei)
            ans.append(node)
        dfs('JFK')
        return ans[::-1]

        