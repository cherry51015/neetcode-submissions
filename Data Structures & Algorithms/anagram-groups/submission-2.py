class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h={}
        for i in strs:
            count=[0]*26
            for j in i:
                count[ord(j)-ord('a')]+=1
            if tuple(count) in h:
                h[tuple(count)].append(i)
            else:
                h[tuple(count)]=[i]
           
        return list(h.values())
        
        