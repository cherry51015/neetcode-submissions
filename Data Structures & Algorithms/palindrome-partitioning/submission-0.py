class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindrome(a):
            lt=0
            rt=len(a)-1
            while lt<rt:
                if a[lt]!=a[rt]:
                    return False
                lt+=1
                rt-=1
            return True
        ans=[]
        path=[]
        def dfs(start):
            if start==len(s):
                ans.append(path[:])
                return
            for i in range(start,len(s)):
                sub=s[start:i+1]
                if palindrome(sub):
                    path.append(sub) 
                    dfs(i+1)
                    path.pop()
        dfs(0)
        return ans

        