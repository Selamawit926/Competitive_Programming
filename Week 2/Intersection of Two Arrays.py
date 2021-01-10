class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        lst=[]
        for i in range(0,len(nums1)):
            if nums1[i] in nums2 and nums1[i] not in lst:
                lst.append(nums1[i])
                
        return lst