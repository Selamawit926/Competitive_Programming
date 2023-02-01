n=eval(input())
ans=[]
for i in range(n):
    line=input().split(" ")
    a=int(line[0])
    b=int(line[1])
    newLst=input()
    lst=[]
    for i in newLst:
        lst.append(i)
    di={"0":0,"1":0}
    # print(lst)
    for i in lst:
        if i in di:
            di[i]+=1
    # print(di)
    left=0
    right=len(lst)-1
    while left<=right:
        if lst[left]=="?" and lst[right]!="?":
            lst[left]=lst[right]
            di[lst[right]]+=1
        elif lst[right]=="?" and lst[left]!="?":
            lst[right]=lst[left]
            di[lst[left]]+=1
        left+=1
        right-=1

    if di["0"]>a or di["1"]>b:
        ans.append(-1)
    else:
        # print(lst)
        left=0
        right=len(lst)-1
        palindrome=True
        while left<=right:
            # print(left,right)
            if lst[left]!="?" and lst[right]!="?" and lst[right]==lst[left]:
                left+=1
                right-=1
    
            elif lst[left]!="?" and lst[right]!="?" and lst[left]!=lst[right]:
                palindrome=False
                break
            else:
                if lst[left]=="?" and lst[right]=="?":
                    if a-di["0"]>=b-di["1"]:
                        lst[left]="0"
                        lst[right]="0"
                        if right-left>0:
                            di["0"]+=2
                        else:
                            di["0"]+=1
                    else:
                        lst[left]="1"
                        lst[right]="1"
                        if right-left>0:
                            di["1"]+=2
                        else:
                            di["1"]+=1
                left+=1
                right-=1
        # print(di)
        if not palindrome:
            ans.append(-1)
        elif di["0"]!=a or di["1"]!=b:
            ans.append(-1)
        else:
            output="".join(lst)
            ans.append(output)

for i in ans:
    print(i)               

