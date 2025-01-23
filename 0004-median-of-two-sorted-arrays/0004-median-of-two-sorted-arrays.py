class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        merged = []

        i,j=0,0
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                merged.append(nums1[i])
                i+=1
            else:
                merged.append(nums2[j])
                j+=1

        while i<m:
            merged.append(nums1[i])
            i+=1

        while j<n:
            merged.append(nums2[j])
            j+=1

        k = len(merged)
        if k%2==1:
            median = merged[k//2]
        else: 
            median = (merged[k//2]+merged[(k//2) -1])/2
        
        return median