class Trie:
    def __init__(self):
        self.children=[None]*26
        self.end=False
class PrefixTree:

    def __init__(self):
        self.root=Trie()
        

    def insert(self, word: str) -> None:
        node=self.root
        for i in word:
            ch=ord(i)-ord('a')
            if node.children[ch] is None:
                node.children[ch]=Trie()
            node=node.children[ch]
        node.end=True


    def search(self, word: str) -> bool:
        node=self.root
        for i in word:
            ch=ord(i)-ord('a')
            if node.children[ch] is None:
                return False
            node=node.children[ch]
        return node.end
        

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for i in prefix:
            ch=ord(i)-ord('a')
            if not node.children[ch]:
                return False
            node=node.children[ch]
        return True
        
        