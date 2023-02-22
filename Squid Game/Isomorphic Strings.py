class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # print(s)
        di={}
        di2={}
        for i in range(len(s)):
            if t[i] in di:
                if s[i] != di[t[i]]:
                    return False
                
            else:
                di[t[i]]=s[i]
                
            if s[i] in di2:
                if t[i] != di2[s[i]]:
                    return False
                
            else:
                di2[s[i]]=t[i]
                
        return True