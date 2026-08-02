class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r=len(heights)
        c=len(heights[0])
        pacific=[]
        atlantic=[]
        for i in range(r):
            for j in range(c):
                if i==0 or j==0:
                    pacific.append((i,j))
                if i==r-1 or j==c-1:
                    atlantic.append((i,j))
        directions=[(0,1),(0,-1),(1,0),(-1,0)] 
        p=set()
        a=set()
        def pdfs(i,j):
            if (i,j) in p:
                return 
            p.add((i,j))
            for di,dj in directions:
                ni=i+di
                nj=j+dj
                if 0<=ni<r and 0<=nj<c and heights[ni][nj]>=heights[i][j]:
                    pdfs(ni,nj)
                      
            return 
       
        for i,j in pacific:
            pdfs(i,j)
            
        def adfs(i,j):
            if (i,j) in a:
                return 
            a.add((i,j))
            for di,dj in directions:
                ni=i+di
                nj=j+dj
                if 0<=ni<r and 0<=nj<c and heights[ni][nj]>=heights[i][j]:
                    adfs(ni,nj)
            return 

        for i,j in atlantic:
            adfs(i,j)
                
        ans=[]
        for i,j in p:
            if (i,j) in a:
                ans.append([i,j])
        return ans




        
        
        
                



        
        
        