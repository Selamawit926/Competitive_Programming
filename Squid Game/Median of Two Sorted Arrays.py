class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst=nums1+nums2
        lst.sort()
        if len(lst)%2==0:
            mid=(len(lst)-1)//2
            tot=lst[mid]+lst[mid+1]
            return tot/2
        else:
            mid=(len(lst)-1)//2
            return lst[mid]