class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lt=0
        rt=len(numbers)-1
        while lt<rt:
            s=numbers[lt]+numbers[rt]
            if s==target:
                return [lt+1,rt+1]
            elif s<target:
                lt+=1
            else:
                rt-=1
        return -1
        