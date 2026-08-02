class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        graph=defaultdict(list)
        i=0
        while i<len(wordList):
            idx=0
            word=wordList[i]
            while idx<len(word):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new=word[:idx]+ch+word[idx+1:]
                    if new==word:
                        continue
                    if new in wordList:
                        graph[word].append(new)
                idx+=1
            i+=1
        if len(graph[beginWord])==0:
            return 0
        q=deque([])
        q.append(beginWord)
        count=1
        v=set()
        while q:
            n=len(q)
            for _ in range(n):
                w=q.popleft()
                v.add(w)
                for nei in graph[w]:
                    if nei not in v:
                        if nei==endWord:
                           return count+1
                        q.append(nei)
            count+=1

        return 0




                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        
