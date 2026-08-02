class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        path=[]
        def dfs(openp,closep):
            if openp==closep==n:
                ans.append("".join(path[:]))
                return
            if openp<n:
                path.append('(')
                dfs(openp+1,closep)
                path.pop()
            if openp>closep:
                path.append(')')
                dfs(openp,closep+1)
                path.pop()
        
        dfs(0,0)
        return ans