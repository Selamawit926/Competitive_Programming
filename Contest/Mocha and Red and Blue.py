n=eval(input())
ans=[]
for i in range(n):
    squares=eval(input())
    line=input()
    lst=[]
    if len(line)==1:
        if line[0]=="?":
            lst.append("B")
        else:
            lst.append(line[0])
    else:
        left=0
        right=1
        pos1=[]
        pos2=[]
        lst.append(line[0])
        while right<len(line):
            if lst[left]=="?":
                if line[right]=="R":
                    lst[left]="B"
                    lst.append(line[right])
                elif line[right]=="B":
                    lst[left]="R"
                    lst.append(line[right])
                else:
                    pos1.append("B")
                    pos2.append("R")
                    start=0
                    while right<len(line) and line[right]=="?":
                        if pos1[start]=="B":
                            pos1.append("R")
                        else:
                            pos1.append("B")
                        if pos2[start]=="R":
                            pos2.append("B")
                        else:
                            pos2.append("R")
                        start+=1
                        if right+1==len(line):
                            break
                        right+=1
                    

                    lst.pop()
                    # print("here: ",right, "left: ",left)
                    if line[right]=="R":
                        if pos1[-1]=="B":
                            for num in pos1:
                                lst.append(num)
                        else:
                            for num in pos2:
                                lst.append(num)
                        lst.append(line[right])

                    elif line[right]=="B":
                        if pos1[-1]=="R":
                            for num in pos1:
                                lst.append(num)
                            
                        else:
                            for num in pos2:
                                lst.append(num)
                        lst.append(line[right])

                    else:
                        for num in pos1:
                            lst.append(num)

                    left=right-1

            elif lst[left]=="R" and line[right]=="?":
                lst.append("B")
            elif lst[left]=="B" and line[right]=="?":
                lst.append("R")
            else:
                lst.append(line[right])
            left+=1
            right+=1

    ans.append("".join(lst))

for i in ans:
    print(i)