class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=0
        fast=0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        ptr1=0
        ptr2=slow
        while ptr1!=ptr2:
            ptr1=nums[ptr1]
            ptr2=nums[ptr2]
        return ptr1
    

        