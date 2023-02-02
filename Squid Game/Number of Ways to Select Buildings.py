class Solution:
    def numberOfWays(self, s: str) -> int:
        ways=ones=zeros=0
        zerosA=onesA=0
        for i in s:
            if i=="0":
                zeros+=1
                zerosA+=ones
                ways+=onesA
            else:
                ones+=1
                onesA+=zeros
                ways+=zerosA
        return ways