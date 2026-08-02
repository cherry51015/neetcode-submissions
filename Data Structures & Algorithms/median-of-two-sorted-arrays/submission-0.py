class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=[]
        n=len(nums1)
        m=len(nums2)
        i=0
        j=0
        while i<n and j<m:
            if nums1[i]<nums2[j]:
               nums.append(nums1[i])
               i+=1
            else:
                nums.append(nums2[j])
                j+=1
        while i<n:
            nums.append(nums1[i])
            i+=1
        while j<m:
            nums.append(nums2[j])
            j+=1
        
        lt=0
        n=len(nums)
        rt=n-1
        mid=(lt+rt)//2
        if n%2==1:
            return nums[mid]
        else:
            return (nums[mid]+nums[mid+1])/2



        
        