class Solution:
    def romanToInt(self, s: str) -> int:
        save={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        num=0
        i=len(s)-1
        while i>=0:
            if (s[i]=="V" or s[i]=="X") and i>0 and s[i-1]=="I":
                if s[i]=="V":
                    num+=4
                else:
                    num+=9
                i-=2
            elif (s[i]=="L" or s[i]=="C") and i>0 and s[i-1]=="X":
                if s[i]=="L":
                    num+=40
                else:
                    num+=90
                i-=2
            elif (s[i]=="D" or s[i]=="M") and i>0 and s[i-1]=="C":
                if s[i]=="D":
                    num+=400
                else:
                    num+=900
                i-=2
            else:
                num+=save[s[i]]
                i-=1
        return num