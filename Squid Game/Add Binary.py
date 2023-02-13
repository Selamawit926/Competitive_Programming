class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)>len(b):
            b="0"*(len(a)-len(b))+b
        elif len(b)>len(a):
            a="0"*(len(b)-len(a))+a
        carry=0
        lst=[]
        for i in range(len(a)-1,-1,-1):
            if a[i]=="1" and b[i]=="1":
                if carry==1:
                    lst.append("1")
                else:
                    lst.append("0")
                carry=1
            elif a[i]=="0" and b[i]=="0":
                if carry==1:
                    lst.append("1")
                    carry=0
                else:
                    lst.append("0")
            else:
                if carry==1:
                    lst.append("0")
                    carry=1
                else:
                    lst.append("1")
        if carry==1:
            lst.append("1")
        lst.reverse()
        return "".join(lst)