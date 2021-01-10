class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        x=0
        if len(s)==len(t):
            for i in s:
                if i in t and s.count(i)==t.count(i):
                    x+=1
                else:
                    return False

            if x==len(s):
                return True
        else:
            return False
        
# s="anagram"
# t="nagaram"
# s1=[i for i in s]
# t1=[i for i in t]

# if len(s)==len(t):
#     for i in range(0,len(s1)):
#         for j in range(i+1,len(s1)):
#             if s1[i]>s1[j]:
#                 s1[i],s1[j]=s1[j],s1[i]


#     for i in range(0,len(t1)):
#         for j in range(i+1,len(t1)):
#             if t1[i]>t1[j]:
#                 t1[i],t1[j]=t1[j],t1[i]

#     x=0
#     for i in range(0,len(s1)):
#         if s1[i]==t1[i]:
#             x+=1

#     if x==len(s):
#         print(True)
# else:
#     print(False)

