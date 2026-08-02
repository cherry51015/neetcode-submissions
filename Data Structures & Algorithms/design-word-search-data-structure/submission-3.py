class Trie:
    def __init__(self):
        self.children=[None]*26
        self.end=False
class WordDictionary:

    def __init__(self):
        self.root=Trie()
        

    def addWord(self, word: str) -> None:
        node=self.root
        for ch in word:
            i=ord(ch)-ord('a')
            if not node.children[i]:
                node.children[i]=Trie()
            node=node.children[i]
        node.end=True
    def dfs(self,node,index):
        if node.end==True and start==len(s)-1:
            return True
        if (node.end==False and start==len(s)-1) or (node.end==True and start<len(s)-1):
            return False
        for idx in range(start,len(s)):
            i=ord(s[idx])-ord('a')
            if s[idx]==".":
                for x in range(26):
                    if not dfs(node.children[x]):
                        return False
                    
            

    def search(self, word: str) -> bool:
        def dfs(node,idx):
            if idx==len(word):
                return node.end
            if word[idx]!=".":
                child=node.children[ord(word[idx])-ord('a')]
                if child is None:
                    return False
                else:
                    return dfs(child,idx+1)
            for child in node.children:
                if child and dfs(child,idx+1):
                    return True
            return False
        return dfs(self.root,0)