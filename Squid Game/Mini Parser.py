class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        s=deque(list(s))
        s.append(" ")
        return self.helper(s)
        
    def helper(self,s):
        num=""
        while 48<=ord(s[0])<=57 or ord(s[0])==45:
            num+=s.popleft()
        if num:
            return NestedInteger(int(num))
        s.popleft()
        lst=NestedInteger()
        while s[0]!=']':
            lst.add(self.helper(s))
            if s[0]==',':
                s.popleft()
        s.popleft()
        return lst