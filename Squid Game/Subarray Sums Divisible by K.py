class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count=curr=0
        mods=[1]+[0]*k
        for num in nums:
            curr=(curr+num)%k
            count+=mods[curr]
            mods[curr]+=1

        return count