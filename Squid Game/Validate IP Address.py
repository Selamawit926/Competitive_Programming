class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if not queryIP:return "Neither"
        query=set(queryIP)
        curr=[]
        # print(ord('A'),ord('F'),ord('a'),ord('0'))
        if "." in query:
            curr=queryIP.split(".")
            if len(curr)>4 or len(curr)<4: return "Neither"
            for i in curr:
                for j in i:
                    if ord(j)<ord('0') or ord(j)>ord('9'):
                        return 'Neither'
                if not i or int(i)>255 or i[0]=='0' and len(i)>1:
                    return "Neither"
            return "IPv4"
        if ":" in query:
            curr=queryIP.split(":")
            if len(curr)>8 or len(curr)<8: return "Neither"
            for i in curr:
                for j in i:
                    if ord('F')<ord(j)<ord('a') or ord('9')<ord(j)<ord('A') or ord(j)>ord('f') or ord(j)<ord('0'):
                        return 'Neither'
                if not i or len(i)>=5:
                    return "Neither"
            return "IPv6"