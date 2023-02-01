n=eval(input())
ans=[]
for i in range(n):
    jumps=input().split(" ")
    pointer=count=maxi=0
    for word in jumps:
        while pointer<len(word):
            if word[pointer]=="L":
                count+=1
            else:
                maxi=max(maxi,count+1)
                count=0
            pointer+=1

        maxi=max(maxi,count+1)
    ans.append(maxi)
    
for i in ans:
    print(i)
