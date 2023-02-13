n=input()
output=[]
for i in range(int(n)):
    length=input()
    s=input()
    left=0
    right=len(s)-1
    while s[left]!=s[right] and left<right:
        left+=1
        right-=1
    output.append((right-left)+1)
for i in output:
    print(i)