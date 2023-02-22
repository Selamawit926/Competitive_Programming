class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mods=[0]*60
        tot=0
        for ti in time:
            tot+=mods[-ti%60]
            mods[ti%60]+=1
        return tot