cases=eval(input())
output=[]
for i in range(cases):
    n=eval(input())
    word=input()
    seen=set()
    left=0
    ans=[]
    while left<len(word):
        if word[left] in seen:
            ans.append(len(seen)+len(set(word[left:])))
        seen.add(word[left])
        left+=1
    if ans:
        output.append(max(ans))
    else:
        output.append(len(word))
for i in output:
    print(i)
        