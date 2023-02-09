class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        valid=[]
        self.helper(s,[],valid,0)
        return valid
            
            
    def helper(self,s,curr,valid,i):
        if i>=len(s):
            if len(curr)==4:
                address=".".join(curr)
                valid.append(address)
            return
        j=i
        while j<len(s):
            num=s[i:j+1]
            if len(num)>3 or int(num)>255:
                break
            if num=="0":
                self.helper(s,curr+["0"],valid,j+1)
                break
            else:
                self.helper(s,curr+[num],valid,j+1)
            j+=1
        return