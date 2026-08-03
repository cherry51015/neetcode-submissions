class Trie:
    def __init__(self):
        self.children=[None]*26
        self.word=None

    
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root=Trie()
        r=len(board)
        c=len(board[0])
        for word in words:
            node=self.root
            for ch in word:
                i=ord(ch)-ord("a")
                if not node.children[i]:
                    node.children[i]=Trie()
                node=node.children[i]
            node.word=word
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        ans=[]
        def dfs(i,j,node):
            ch=board[i][j]
            x=ord(ch)-ord('a')
            if node.children[x] is None:
                return

            node=node.children[x]

            if node.word:
                ans.append(node.word)
                node.word=None

            board[i][j]='#'
       
            for nr,nc in directions:
                nr+=i
                nc+=j
                if 0<=nr<r and 0<=nc<c and board[nr][nc]!="#":
                    if dfs(nr,nc,node):
                        return True
            board[i][j]=ch
            return False
        
        for i in range(r):
            for j in range(c):
                dfs(i,j,self.root)
        return ans
