class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        h={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        path=[]
        ans=[]
        def dfs(start):
            if digits=="":
                return []
            if start==len(digits):
                ans.append("".join(path[:]))
                return
            if digits[start] not in h:
                return 
            for i in range(len(h[digits[start]])):
                path.append(h[digits[start]][i])
                dfs(start+1)
                path.pop()
        dfs(0)
        return ans

















































































            

