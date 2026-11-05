class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        m=len(nums1)
        n=len(nums2)
        h=(m+n+1)//2
        oh=m+n-h
        lt=0
        rt=m
        while lt<=rt:
            mid1=(lt+rt)//2
            mid2=h-mid1
            
            l1=float('-inf') if mid1==0 else nums1[mid1-1]
            l2=float('-inf') if mid2==0 else nums2[mid2-1]
            r1=float('inf') if mid1==m else nums1[mid1]
            r2=float('inf') if mid2==n else nums2[mid2]

            if l1>r2:
                rt=mid1-1
            elif r1<l2:
                lt=mid1+1
            elif l1<=r2 and r1>=l2:
                if (m+n)%2!=0:
                    return max(l1,l2)
                else:
                    return ((min(r1,r2)+max(l1,l2))/2)








        