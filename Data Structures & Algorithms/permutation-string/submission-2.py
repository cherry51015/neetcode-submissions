class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lt=0
        arr1=[0]*26
        arr2=[0]*26
        for ch in s1:
            arr1[ord(ch)-ord('a')]+=1
        for ch in s2[0:len(s1)-1]:
            arr2[ord(ch)-ord('a')]+=1
        for rt in range(len(s1)-1,len(s2)):
            arr2[ord(s2[rt])-ord('a')]+=1
            if arr2!=arr1:
                arr2[ord(s2[lt])-ord('a')]-=1
                lt+=1
            else:
                    return True
            
        return False



        